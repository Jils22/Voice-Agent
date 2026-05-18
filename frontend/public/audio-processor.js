class MicProcessor extends AudioWorkletProcessor {
  constructor(opts) {
    super();
    this._tgtSR     = opts.processorOptions?.targetSR || 16000;
    this._ratio     = sampleRate / this._tgtSR;
    this._pcmBuf    = [];
    this._energy    = 0;

    // ── Local VAD state ──────────────────────────────────────────
    // Used ONLY for instant interrupt detection — not for gating PCM.
    // Deepgram cloud VAD handles actual transcript boundaries.
    // ── Local VAD state ──────────────────────────────────────────
    this._IDLE_THRESH    = 0.025;  // Background noise gate when agent is silent
    this._AGENT_THRESH   = 0.040;  // Interrupt threshold while agent speaks (ultra-responsive barge-in)
    this._IDLE_FRAMES    = 8;      // ~64ms  — quick pickup when idle
    this._AGENT_FRAMES   = 8;      // ~64ms  — instantaneous confirmation window
    
    this._SILENCE_FRAMES = 60;     
    this._speechCount    = 0;
    this._silenceCount   = 0;
    this._inSpeech       = false;
    this._agentOn        = false;  

    this.port.onmessage = ({ data }) => {
      if (data.type === 'agent_speaking') {
        this._agentOn = data.v;
        // Reset ALL counters on mode change to avoid carryover state
        this._speechCount  = 0;
        this._silenceCount = 0;
        this._inSpeech     = false;
      }
    };
  }

  process(inputs) {
    const ch = inputs[0]?.[0];
    if (!ch || ch.length === 0) return true;

    // ── RMS energy ────────────────────────────────────────────────
    let sum = 0;
    for (let i = 0; i < ch.length; i++) sum += ch[i] * ch[i];
    const rms = Math.sqrt(sum / ch.length);

    // Smooth energy for UI bar
    this._energy = this._energy * 0.85 + rms * 0.15;
    this.port.postMessage({ type: 'energy', v: this._energy });

    // ── Dynamic VAD Thresholds (Principle: Intelligent Barge-in) ──
    const thresh = this._agentOn ? this._AGENT_THRESH : this._IDLE_THRESH;
    const frames = this._agentOn ? this._AGENT_FRAMES : this._IDLE_FRAMES;

    if (rms > thresh) {
      this._speechCount++;
      this._silenceCount = 0;

      if (this._speechCount >= frames && !this._inSpeech) {
        this._inSpeech = true;
        this.port.postMessage({ type: 'speech_start' });
      }
    } else {
      this._speechCount = Math.max(0, this._speechCount - 1);
      if (this._inSpeech) {
        this._silenceCount++;
        if (this._silenceCount >= this._SILENCE_FRAMES) {
          this._inSpeech   = false;
          this._silenceCount = 0;
        }
      }
    }

    // ── Downsample Float32@48kHz → Int16@16kHz ────────────────────
    // Send PCM continuously regardless of speech state.
    // Deepgram cloud noise rejection handles filtering.
    for (let i = 0; i < ch.length; i += this._ratio) {
      const idx = Math.round(i);
      if (idx < ch.length) this._pcmBuf.push(ch[idx]);
    }

    while (this._pcmBuf.length >= 4096) {
      const slice = this._pcmBuf.splice(0, 4096);
      const i16   = new Int16Array(4096);
      for (let i = 0; i < 4096; i++)
        i16[i] = Math.max(-32768, Math.min(32767, slice[i] * 32767));
      this.port.postMessage({ type: 'pcm', buf: i16.buffer }, [i16.buffer]);
    }

    return true;
  }
}

registerProcessor('pcm-processor', MicProcessor);
