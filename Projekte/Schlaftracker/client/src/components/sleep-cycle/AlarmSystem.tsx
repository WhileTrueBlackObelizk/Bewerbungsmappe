import * as React from 'react';
import { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { AlarmClock, Bell, BellOff } from 'lucide-react';

interface AlarmSystemProps {
  alarmTime: string;
  onClearAlarm: () => void;
}

export function AlarmSystem({ alarmTime, onClearAlarm }: AlarmSystemProps) {
  const [isAlarmActive, setIsAlarmActive] = useState(false);
  const [timeUntilAlarm, setTimeUntilAlarm] = useState<string>('');

  useEffect(() => {
    if (!alarmTime) {
      setIsAlarmActive(false);
      return;
    }

    const interval = setInterval(() => {
      const now = new Date();
      const [hours, minutes] = alarmTime.split(':').map(Number);
      const alarmDate = new Date();
      alarmDate.setHours(hours, minutes, 0, 0);

      // If alarm time is past today, set it for tomorrow
      if (alarmDate <= now) {
        alarmDate.setDate(alarmDate.getDate() + 1);
      }

      const timeDiff = alarmDate.getTime() - now.getTime();
      const hoursUntil = Math.floor(timeDiff / (1000 * 60 * 60));
      const minutesUntil = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));

      setTimeUntilAlarm(`${hoursUntil}h ${minutesUntil}m`);

      // Check if it's time to trigger the alarm
      if (timeDiff <= 0) {
        triggerAlarm();
      }
    }, 1000);

    setIsAlarmActive(true);
    return () => clearInterval(interval);
  }, [alarmTime]);

  const triggerAlarm = () => {
    // In a real app, this would trigger system notifications
    // For now, we'll just show an alert
    alert('Wake up! Your alarm is ringing!');
    setIsAlarmActive(false);
    onClearAlarm();
  };

  const handleClearAlarm = () => {
    setIsAlarmActive(false);
    onClearAlarm();
  };

  if (!alarmTime) {
    return null;
  }

  return (
    <Card className="border-red-600/50 bg-red-950/40 red-glow">
      <CardContent className="p-3 sm:p-4">
        <div className="flex items-center justify-between gap-2">
          <div className="flex items-center gap-2 sm:gap-3 flex-1 min-w-0">
            <div className="flex items-center gap-1 sm:gap-2">
              {isAlarmActive ? (
                <Bell className="h-4 w-4 sm:h-5 sm:w-5 text-red-400 animate-pulse" />
              ) : (
                <BellOff className="h-4 w-4 sm:h-5 sm:w-5 text-red-600" />
              )}
              <div className="min-w-0">
                <div className="font-mono text-base sm:text-lg font-bold text-red-100 truncate">
                  {alarmTime}
                </div>
                {isAlarmActive && (
                  <div className="text-xs sm:text-sm text-red-300">
                    in {timeUntilAlarm}
                  </div>
                )}
              </div>
            </div>
          </div>
          <Button
            variant="outline"
            size="sm"
            onClick={handleClearAlarm}
            className="flex items-center gap-1 border-red-700 text-red-200 hover:bg-red-900/30 red-glow-hover text-xs sm:text-sm shrink-0"
          >
            <BellOff className="h-3 w-3 sm:h-4 sm:w-4" />
            <span className="hidden xs:inline">Clear</span>
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}