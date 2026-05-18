
import { motion } from 'framer-motion';
import { Message } from '../hooks/useVoiceAgent';

interface ChatBubbleProps {
  message: Message;
}

export function ChatBubble({ message }: ChatBubbleProps) {
  if (message.role === 'system') {
    return (
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        style={{
          alignSelf: 'center',
          color: 'var(--text-muted)',
          fontSize: '0.8rem',
          padding: '4px 0',
        }}
      >
        {message.text}
      </motion.div>
    );
  }

  const isUser = message.role === 'user';

  return (
    <motion.div
      initial={{ opacity: 0, y: 12, scale: 0.97 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={{ opacity: 0, y: -8, scale: 0.95 }}
      transition={{ duration: 0.3, ease: [0.25, 0.46, 0.45, 0.94] }}
      className={isUser ? 'bubble-user' : 'bubble-agent'}
    >
      {message.text}
      {message.language && (
        <span className="lang-badge">
          {message.language.toUpperCase()}
        </span>
      )}
    </motion.div>
  );
}
