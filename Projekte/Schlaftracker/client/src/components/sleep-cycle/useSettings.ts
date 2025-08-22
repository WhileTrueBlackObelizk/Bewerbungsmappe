import { useState, useEffect } from 'react';

interface Settings {
  cycleDuration: number;
  fallAsleepBuffer: number;
}

const DEFAULT_SETTINGS: Settings = {
  cycleDuration: 90, // 90 minutes per cycle
  fallAsleepBuffer: 15 // 15 minutes to fall asleep
};

export function useSettings() {
  const [settings, setSettings] = useState<Settings>(DEFAULT_SETTINGS);

  useEffect(() => {
    // Load settings from localStorage on component mount
    const savedSettings = localStorage.getItem('sleepCycleSettings');
    if (savedSettings) {
      try {
        const parsed = JSON.parse(savedSettings);
        setSettings({ ...DEFAULT_SETTINGS, ...parsed });
      } catch (error) {
        console.error('Failed to parse saved settings:', error);
      }
    }
  }, []);

  const updateSettings = (newSettings: Settings) => {
    setSettings(newSettings);
    localStorage.setItem('sleepCycleSettings', JSON.stringify(newSettings));
  };

  return { settings, updateSettings };
}