import { useCallback, useEffect, useRef, useState } from "react";

export type Message = {
    role: "user" | "agent" | "system";
    text: string;
    language?: string;
};

// Full 6-state machine (Principle 21)
export type Status = 
  | "idle" 
  | "listening" 
  | "processing" 
  | "speaking" 
  | "interrupting" 
  | "recovering";

const VALID_TRANSITIONS: Record<Status, Status[]> = {
    idle:         ['listening'],
    listening:    ['processing', 'idle'],
    processing:   ['speaking', 'interrupting', 'listening'],
    speaking:     ['listening', 'interrupting', 'idle'],
    interrupting: ['recovering'],
    recovering:   ['listening'],
};

export function useVoiceAgent() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [status, setStatus] = useState<Status>("idle");
    const [vadEnergy, setVadEnergy] = useState<number>(0);
    const [currentLang, setCurrentLang] = useState<string>("en");
    const [callActive, setCallActive] = useState<boolean>(false);
    const [isMuted, setIsMuted] = useState<boolean>(false);
    const [interimText, setInterimText] = useState<string>("");

    const wsRef = useRef<WebSocket | null>(null);
    const micCtxRef = useRef<AudioContext | null>(null);
    const workletNodeRef = useRef<AudioWorkletNode | null>(null);
    const streamRef = useRef<MediaStream | null>(null);
    const analyserRef = useRef<AnalyserNode | null>(null);
    
    const agentSpeakingRef = useRef<boolean>(false);
    const interruptSentRef = useRef<boolean>(false);

    // Playback context
    const playContextRef = useRef<AudioContext | null>(null);
    const gainNodeRef = useRef<GainNode | null>(null);
    const nextPlayTimeRef = useRef<number>(0);

    const safeTransition = useCallback((to: Status) => {
        setStatus(prev => {
            if (VALID_TRANSITIONS[prev].includes(to)) {
                return to;
            }
            console.warn(`Invalid state transition: ${prev} → ${to}`);
            return prev;
        });
    }, []);

    const setAgentSpeaking = useCallback((isSpeaking: boolean) => {
        agentSpeakingRef.current = isSpeaking;
        if (isSpeaking) {
            interruptSentRef.current = false;
            safeTransition("speaking");
        }
        if (workletNodeRef.current) {
            workletNodeRef.current.port.postMessage({ type: 'agent_speaking', v: isSpeaking });
        }
    }, [safeTransition]);

    const stopPlayback = useCallback(() => {
        if (playContextRef.current && playContextRef.current.state !== "closed") {
            playContextRef.current.close().catch(() => {});
        }
        playContextRef.current = null;
        gainNodeRef.current = null;
        nextPlayTimeRef.current = 0;
        setAgentSpeaking(false);
    }, [setAgentSpeaking]);

    const ensurePlayCtx = useCallback(async () => {
        if (playContextRef.current && playContextRef.current.state !== "closed") {
            if (playContextRef.current.state === "suspended") await playContextRef.current.resume();
            return;
        }
        playContextRef.current = new AudioContext({ sampleRate: 16000 });
        gainNodeRef.current = playContextRef.current.createGain();
        gainNodeRef.current.gain.value = 1.0;
        gainNodeRef.current.connect(playContextRef.current.destination);
        nextPlayTimeRef.current = 0;
        await playContextRef.current.resume();
    }, []);

    const disconnect = useCallback((shouldResetMessages: boolean = false) => {
        setCallActive(false);
        
        if (workletNodeRef.current) {
            workletNodeRef.current.disconnect();
            workletNodeRef.current = null;
        }
        if (analyserRef.current) {
            analyserRef.current.disconnect();
            analyserRef.current = null;
        }
        if (micCtxRef.current) {
            micCtxRef.current.close().catch(() => {});
            micCtxRef.current = null;
        }
        if (streamRef.current) {
            streamRef.current.getTracks().forEach((track) => track.stop());
            streamRef.current = null;
        }
        
        stopPlayback();

        if (wsRef.current) {
            if (wsRef.current.readyState === WebSocket.OPEN) {
                wsRef.current.send(JSON.stringify({ type: "call_end" }));
            }
            wsRef.current.close();
            wsRef.current = null;
        }

        safeTransition("idle");
        setVadEnergy(0);
        setIsMuted(false);
        if(shouldResetMessages) setMessages([]);
    }, [stopPlayback, safeTransition]);

    const connect = useCallback(async (languageSelection: string) => {
        const protocol = window.location.protocol === "https:" ? "wss" : "ws";
        const ws = new WebSocket(`${protocol}://${window.location.host}/ws/call`);
        ws.binaryType = "arraybuffer"; 
        wsRef.current = ws;

        await new Promise<void>((resolve, reject) => {
            ws.addEventListener("open", () => {
                ws.send(JSON.stringify({ type: "call_start", language: languageSelection }));
                resolve();
            }, { once: true });
            ws.addEventListener("error", () => reject(new Error("WS connection failed")), { once: true });
        });

        ws.onmessage = async (event) => {
            if (event.data instanceof ArrayBuffer) {
                // Remove strict speaking check for initial greeting/buffers
                await ensurePlayCtx();
                if (!playContextRef.current || !gainNodeRef.current) return;

                const i16Array = new Int16Array(event.data);
                if (i16Array.length === 0) return; // Safeguard against empty audio packets
                
                const f32Array = new Float32Array(i16Array.length);
                for (let i = 0; i < i16Array.length; i++) f32Array[i] = i16Array[i] / 32768.0;

                const audioBuf = playContextRef.current.createBuffer(1, f32Array.length, 16000);
                audioBuf.getChannelData(0).set(f32Array);

                const src = playContextRef.current.createBufferSource();
                src.buffer = audioBuf;
                src.connect(gainNodeRef.current);

                const now = playContextRef.current.currentTime;
                const when = Math.max(now + 0.01, nextPlayTimeRef.current);
                src.start(when);
                nextPlayTimeRef.current = when + audioBuf.duration;
                return;
            }

            const message = JSON.parse(event.data);
            switch (message.type) {
                case "call_accepted":
                    safeTransition("listening");
                    break;
                case "transcript":
                    setMessages(prev => [...prev, { role: "user", text: message.user, language: message.language }]);
                    setInterimText("");
                    safeTransition("processing");
                    break;
                case "transcript_update":
                    setInterimText(message.text);
                    break;
                case "tts_start":
                    setAgentSpeaking(true);
                    ensurePlayCtx();
                    break;
                case "tts_end":
                    setAgentSpeaking(false);
                    safeTransition("listening");
                    break;
                case "clear_queue":
                    stopPlayback();
                    // If we were speaking and got clear_queue, we are interrupting
                    safeTransition("recovering");
                    setTimeout(() => safeTransition("listening"), 300);
                    break;
                case "error":
                    setMessages(prev => [...prev, { role: "system", text: "⚠ " + message.message }]);
                    safeTransition("listening");
                    break;
            }
        };

        return ws;
    }, [ensurePlayCtx, setAgentSpeaking, stopPlayback, safeTransition]);

    const startCall = useCallback(async (lang: string) => {
        setMessages([]);
        setCallActive(true);
        setCurrentLang(lang);
        
        try {
            const ws = await connect(lang);

            const stream = await navigator.mediaDevices.getUserMedia({ 
                audio: { echoCancellation: true, noiseSuppression: true, autoGainControl: false, sampleRate: 48000 } 
            });
            streamRef.current = stream;

            const micCtx = new AudioContext({ sampleRate: 48000 });
            micCtxRef.current = micCtx;

            await micCtx.audioWorklet.addModule("/audio-processor.js?v=" + Date.now());
            const srcNode = micCtx.createMediaStreamSource(stream);

            const analyser = micCtx.createAnalyser();
            analyser.fftSize = 256;
            srcNode.connect(analyser);
            analyserRef.current = analyser;

            const processor = new AudioWorkletNode(micCtx, "pcm-processor", {
                processorOptions: { targetSR: 16000 }
            });
            workletNodeRef.current = processor;

            processor.port.onmessage = ({ data }) => {
                if (data.type === "energy") {
                    setVadEnergy(Math.min(100, data.v * 1200));
                } else if (data.type === "pcm") {
                    if (ws.readyState === WebSocket.OPEN) {
                        ws.send(data.buf); 
                    }
                } else if (data.type === 'speech_start') {
                    // Principle: Mute must be absolute. 
                    // Do not interrupt if user is muted OR if we just started speaking (Echo protection)
                    if (!isMuted && agentSpeakingRef.current && !interruptSentRef.current && ws.readyState === WebSocket.OPEN) {
                        interruptSentRef.current = true;
                        ws.send(JSON.stringify({ type: 'interrupt' }));
                        // Instantly transition to interrupting
                        safeTransition("interrupting");
                        stopPlayback();
                    }
                }
            };

            srcNode.connect(processor);
        } catch (err: any) {
            setMessages(prev => [...prev, { role: "system", text: "⚠ Connection Error: " + err.message }]);
            disconnect(false);
        }
    }, [connect, disconnect, stopPlayback, safeTransition]);

    const toggleMute = useCallback(() => {
        if (!streamRef.current) return;
        const newState = !isMuted;
        setIsMuted(newState);
        streamRef.current.getAudioTracks().forEach(track => {
            track.enabled = !newState; 
        });
    }, [isMuted]);

    useEffect(() => {
        return () => {
            disconnect(false);
        };
    }, [disconnect]);

    return {
        messages,
        interimText,
        status,
        vadEnergy,
        callActive,
        analyserRef,
        startCall,
        stopCall: () => disconnect(false),
        isMuted,
        toggleMute,
        currentLang,
        setCurrentLang,
    };
}
