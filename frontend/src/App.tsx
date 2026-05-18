import { useEffect, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { useVoiceAgent } from "./hooks/useVoiceAgent";
import { VoiceOrb } from "./components/VoiceOrb";
import { ChatBubble } from "./components/ChatBubble";
import { LanguageTabs } from "./components/LanguageTabs";

export default function App() {
  const {
    messages,
    interimText,
    status,
    vadEnergy,
    callActive,
    startCall,
    stopCall,
    isMuted,
    toggleMute,
    currentLang,
    setCurrentLang,
  } = useVoiceAgent();

  const chatRef = useRef<HTMLDivElement>(null);

  // Auto-scroll transcript
  useEffect(() => {
    if (chatRef.current) {
      chatRef.current.scrollTop = chatRef.current.scrollHeight;
    }
  }, [messages, interimText]);

  const handleToggle = () => {
    if (!callActive) {
      startCall(currentLang);
    } else {
      stopCall();
    }
  };

  const getStatusLabel = () => {
    if (!callActive) return "Ready";
    if (status === "listening") return "Listening...";
    if (status === "processing") return "Thinking...";
    if (status === "speaking") return "Speaking...";
    if (status === "interrupting") return "Interrupting...";
    if (status === "recovering") return "Recovering...";
    return "Connecting...";
  };

  return (
    <div className="voice-root">
      {/* Background gradient handled in index.css */}
      <div className="bg-gradient" />

      {/* Header (Minimal) */}
      <header style={{ padding: '24px', zIndex: 2, display: 'flex', alignItems: 'center', gap: '12px' }}>
        <div style={{ width: 40, height: 40, borderRadius: '50%', background: 'var(--bubble-user)', display: 'grid', placeItems: 'center', fontWeight: 'bold' }}>S</div>
        <div style={{ fontSize: '1.2rem', fontWeight: 600 }}>Suvit Support</div>
      </header>

      {/* Hero Section */}
      <section className="hero">
        <VoiceOrb status={callActive ? status : "idle"} vadEnergy={callActive ? vadEnergy : 0} />
        <motion.p
          key={status + callActive}
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          className="status-label"
        >
          {getStatusLabel()}
        </motion.p>
      </section>

      {/* Transcript Panel */}
      <motion.section className="transcript-panel" layout ref={chatRef}>
        {messages.length === 0 && !callActive ? (
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100%', opacity: 0.5, gap: '12px' }}>
            <span style={{ fontSize: '2rem' }}>📞</span>
            <p>Press the call button to begin</p>
          </div>
        ) : (
          <AnimatePresence>
            {messages.map((msg, idx) => (
              <ChatBubble key={idx} message={msg} />
            ))}
          </AnimatePresence>
        )}

        {/* Interim Text */}
        {interimText && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 0.6 }}
            style={{
              padding: '12px 18px',
              borderRadius: '16px',
              borderBottomRightRadius: '4px',
              background: 'var(--bubble-user)',
              alignSelf: 'flex-end',
              fontStyle: 'italic',
              fontSize: '0.95rem'
            }}
          >
            {interimText}...
          </motion.div>
        )}
      </motion.section>

      {/* Controls Dock */}
      <footer className="controls-dock">
        <LanguageTabs current={currentLang} onChange={setCurrentLang} disabled={callActive} />
        
        <button
          onClick={handleToggle}
          className={`icon-btn call-btn ${callActive ? 'active' : ''}`}
        >
          {callActive ? '📵' : '📞'}
        </button>

        <button
          onClick={toggleMute}
          disabled={!callActive}
          className="icon-btn"
          style={{ background: callActive && isMuted ? 'rgba(239, 68, 68, 0.2)' : undefined, borderColor: callActive && isMuted ? '#ef4444' : undefined }}
        >
          {isMuted ? '🔇' : '🎤'}
        </button>
      </footer>
    </div>
  );
}