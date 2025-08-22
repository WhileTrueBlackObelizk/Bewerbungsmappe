import { useCallback } from 'react';

interface Settings {
  cycleDuration: number;
  fallAsleepBuffer: number;
}

export function useSleepCalculator(settings: Settings) {
  const calculateSleepTimes = useCallback((inputTime: string, mode: 'bedtime' | 'waketime') => {
    const [hours, minutes] = inputTime.split(':').map(Number);
    const results = [];
    
    // Generate 4-8 sleep cycles
    for (let cycles = 4; cycles <= 8; cycles++) {
      const totalSleepTime = cycles * settings.cycleDuration;
      let resultHours: number;
      let resultMinutes: number;

      if (mode === 'bedtime') {
        // Calculate bedtime: wake time - sleep time - buffer
        const totalMinutesToSubtract = totalSleepTime + settings.fallAsleepBuffer;
        let totalMinutes = hours * 60 + minutes - totalMinutesToSubtract;
        
        // Handle negative time (previous day)
        if (totalMinutes < 0) {
          totalMinutes += 24 * 60; // Add 24 hours
        }
        
        resultHours = Math.floor(totalMinutes / 60);
        resultMinutes = totalMinutes % 60;
      } else {
        // Calculate wake time: bedtime + buffer + sleep time
        const totalMinutesToAdd = totalSleepTime + settings.fallAsleepBuffer;
        let totalMinutes = hours * 60 + minutes + totalMinutesToAdd;
        
        // Handle time overflow (next day)
        if (totalMinutes >= 24 * 60) {
          totalMinutes -= 24 * 60; // Subtract 24 hours
        }
        
        resultHours = Math.floor(totalMinutes / 60);
        resultMinutes = totalMinutes % 60;
      }

      const timeString = `${resultHours.toString().padStart(2, '0')}:${resultMinutes.toString().padStart(2, '0')}`;

      results.push({
        time: timeString,
        cycles: cycles
      });
    }

    return results;
  }, [settings]);

  return { calculateSleepTimes };
}