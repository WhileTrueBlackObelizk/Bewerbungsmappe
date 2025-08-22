import * as React from 'react';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Moon, Sun } from 'lucide-react';

interface TimeInputProps {
  mode: 'bedtime' | 'waketime';
  value: string;
  onChange: (value: string) => void;
}

export function TimeInput({ mode, value, onChange }: TimeInputProps) {
  const handleTimeChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    onChange(e.target.value);
  };

  return (
    <div className="space-y-2">
      <Label className="flex items-center gap-2 text-red-200 text-xs sm:text-sm">
        {mode === 'bedtime' ? <Moon className="h-3 w-3 sm:h-4 sm:w-4 text-red-400" /> : <Sun className="h-3 w-3 sm:h-4 sm:w-4 text-red-400" />}
        <span className="hidden sm:inline">
          {mode === 'bedtime' ? 'When do you want to wake up?' : 'When do you want to go to bed?'}
        </span>
        <span className="sm:hidden">
          {mode === 'bedtime' ? 'Wake up time?' : 'Bedtime?'}
        </span>
      </Label>
      <Input
        type="time"
        value={value}
        onChange={handleTimeChange}
        className="text-center text-base sm:text-lg bg-red-950/40 border-red-800 text-red-100 focus:border-red-600 red-glow h-10 sm:h-12"
        placeholder="Select time"
      />
    </div>
  );
}