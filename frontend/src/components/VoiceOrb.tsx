
import { motion } from 'framer-motion';
import { Status } from '../hooks/useVoiceAgent';

const stateColors: Record<Status, string> = {
  idle: '#6366f1',
  listening: '#22d3ee',
  processing: '#f59e0b',
  speaking: '#10b981',
  interrupting: '#ef4444',
  recovering: '#8b5cf6',
};

interface OrbProps {
  status: Status;
  vadEnergy: number; // 0-100
}

export function VoiceOrb({ status, vadEnergy }: OrbProps) {
  const baseSize = 100;
  const maxGrow = 90; // Increased max growth for more dynamic scale
  // Convert vadEnergy (0-100) to a 0-1 scale, apply an exponential curve for punchier reaction
  const rawVolume = Math.min(1, Math.max(0, vadEnergy / 100));
  const volume = Math.pow(rawVolume, 1.5); 
  const dynamicSize = baseSize + volume * maxGrow;
  
  const color = stateColors[status] || stateColors.idle;

  return (
    <div style={{ position: 'relative', width: 200, height: 200, display: 'grid', placeItems: 'center' }}>
      {/* Outer ripple ring */}
      <motion.div
        animate={{ scale: [1, 1.5, 1], opacity: [0.3, 0, 0.3] }}
        transition={{ duration: 2, repeat: Infinity, ease: 'easeOut' }}
        style={{
          position: 'absolute',
          width: dynamicSize,
          height: dynamicSize,
          borderRadius: '50%',
          border: `2px solid ${color}`,
        }}
      />
      {/* Secondary ripple ring for more depth */}
      <motion.div
        animate={{ scale: [1, 1.3, 1], opacity: [0.5, 0.1, 0.5] }}
        transition={{ duration: 1.5, repeat: Infinity, ease: 'easeInOut', delay: 0.5 }}
        style={{
          position: 'absolute',
          width: dynamicSize * 0.9,
          height: dynamicSize * 0.9,
          borderRadius: '50%',
          border: `1px solid ${color}`,
        }}
      />
      {/* Core orb */}
      <motion.div
        animate={{ scale: dynamicSize / baseSize }}
        transition={{ type: 'spring', stiffness: 500, damping: 15 }}
        style={{
          width: baseSize,
          height: baseSize,
          borderRadius: '50%',
          background: color,
          opacity: 0.85,
          boxShadow: `0 0 ${20 + volume * 60}px ${color}88`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center'
        }}
      >
        {status === 'idle' && <span style={{ fontSize: '2rem', opacity: 0.5, transform: `scale(${baseSize / dynamicSize})` }}>🎙️</span>}
      </motion.div>
    </div>
  );
}
