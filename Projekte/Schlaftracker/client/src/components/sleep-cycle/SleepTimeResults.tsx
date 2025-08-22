import * as React from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { AlarmClock } from 'lucide-react';

interface SleepTimeResultsProps {
  results: Array<{ time: string; cycles: number }>;
  mode: 'bedtime' | 'waketime';
  onSetAlarm: (time: string) => void;
}

export function SleepTimeResults({ results, mode, onSetAlarm }: SleepTimeResultsProps) {
  if (results.length === 0) {
    return null;
  }

  const title = mode === 'bedtime' 
    ? 'Recommended bedtimes:' 
    : 'Recommended wake times:';

  return (
    <div className="space-y-2 sm:space-y-3">
      <h3 className="font-semibold text-center text-red-200 text-sm sm:text-base">{title}</h3>
      <div className="space-y-2 grid gap-2">
        {results.map((result, index) => (
          <Card key={index} className="border-l-4 border-l-red-500 bg-red-950/30 border-red-900/30 red-glow">
            <CardContent className="p-2 sm:p-3">
              <div className="flex items-center justify-between gap-2">
                <div className="flex-1 min-w-0">
                  <div className="font-mono text-base sm:text-lg font-bold text-red-100 truncate">
                    {result.time}
                  </div>
                  <div className="text-xs sm:text-sm text-red-300">
                    {result.cycles} cycles ({result.cycles * 1.5}h)
                  </div>
                </div>
                <Button
                  size="sm"
                  onClick={() => onSetAlarm(result.time)}
                  className="flex items-center gap-1 bg-red-700 hover:bg-red-600 text-red-100 red-glow-hover text-xs sm:text-sm shrink-0"
                >
                  <AlarmClock className="h-3 w-3 sm:h-4 sm:w-4" />
                  <span className="hidden xs:inline">Set Alarm</span>
                  <span className="xs:hidden">Set</span>
                </Button>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}