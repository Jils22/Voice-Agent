
import { motion } from 'framer-motion';

interface LanguageTabsProps {
  current: string;
  onChange: (lang: string) => void;
  disabled: boolean;
}

const tabs = ['en', 'hi', 'gu'];
const labels: Record<string, string> = { en: 'English', hi: 'Hindi', gu: 'Gujarati' };

export function LanguageTabs({ current, onChange, disabled }: LanguageTabsProps) {
  return (
    <div className="tab-container" style={{ opacity: disabled ? 0.6 : 1, pointerEvents: disabled ? 'none' : 'auto' }}>
      {tabs.map((tab) => {
        const isActive = current === tab;
        return (
          <button
            key={tab}
            onClick={() => onChange(tab)}
            className={`tab-btn ${isActive ? 'active' : ''}`}
            disabled={disabled}
          >
            {isActive && (
              <motion.div
                layoutId="tab-indicator"
                className="tab-indicator"
                transition={{ type: 'spring', stiffness: 400, damping: 30 }}
              />
            )}
            <span style={{ position: 'relative', zIndex: 1 }}>{labels[tab]}</span>
          </button>
        );
      })}
    </div>
  );
}
