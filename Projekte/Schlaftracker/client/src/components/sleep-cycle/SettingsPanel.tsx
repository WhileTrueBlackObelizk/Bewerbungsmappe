import * as React from 'react';
import { Label } from '@/components/ui/label';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Settings } from 'lucide-react';

interface SettingsProps {
  settings: {
    cycleDuration: number;
    fallAsleepBuffer: number;
  };
  onUpdateSettings: (settings: { cycleDuration: number; fallAsleepBuffer: number }) => void;
}

export function SettingsPanel({ settings, onUpdateSettings }: SettingsProps) {
  const handleCycleDurationChange = (duration: number) => {
    onUpdateSettings({ ...settings, cycleDuration: duration });
  };

  const handleBufferChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = parseInt(e.target.value);
    if (value >= 0) {
      onUpdateSettings({ ...settings, fallAsleepBuffer: value });
    }
  };

  return (
    <Card className="bg-red-950/30 border-red-900/30 red-glow">
      <CardHeader className="pb-2 sm:pb-4">
        <CardTitle className="flex items-center gap-2 text-sm sm:text-base text-red-100">
          <Settings className="h-3 w-3 sm:h-4 sm:w-4 text-red-400" />
          Sleep Settings
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-3 sm:space-y-4 p-3 sm:p-6 pt-0">
        <div className="space-y-2">
          <Label className="text-red-200 text-xs sm:text-sm">Sleep Cycle Duration</Label>
          <div className="flex gap-2">
            <Button
              variant={settings.cycleDuration === 90 ? "default" : "outline"}
              size="sm"
              onClick={() => handleCycleDurationChange(90)}
              className={`flex-1 text-xs ${
                settings.cycleDuration === 90 
                  ? 'bg-red-700 hover:bg-red-600 text-red-100' 
                  : 'border-red-700 text-red-200 hover:bg-red-900/30'
              }`}
            >
              90 min
            </Button>
            <Button
              variant={settings.cycleDuration === 45 ? "default" : "outline"}
              size="sm"
              onClick={() => handleCycleDurationChange(45)}
              className={`flex-1 text-xs ${
                settings.cycleDuration === 45 
                  ? 'bg-red-700 hover:bg-red-600 text-red-100' 
                  : 'border-red-700 text-red-200 hover:bg-red-900/30'
              }`}
            >
              45 min
            </Button>
          </div>
          <p className="text-xs text-red-300">
            {settings.cycleDuration === 90 
              ? 'Standard: Ein vollständiger Schlafzyklus (Leicht-, Tief- und REM-Schlaf)'
              : 'Kurz: Halber Zyklus für Power-Naps oder bei Schlafmangel'
            }
          </p>
        </div>

        <div className="space-y-2">
          <Label htmlFor="fallAsleepBuffer" className="text-red-200 text-xs sm:text-sm">Einschlafzeit (Minuten)</Label>
          <Input
            id="fallAsleepBuffer"
            type="number"
            value={settings.fallAsleepBuffer}
            onChange={handleBufferChange}
            min="0"
            max="60"
            step="5"
            className="bg-red-950/40 border-red-800 text-red-100 focus:border-red-600 text-sm h-8 sm:h-9"
          />
          <p className="text-xs text-red-300">
            Zeit, die du brauchst, um nach dem Hinlegen einzuschlafen.
          </p>
        </div>
      </CardContent>
    </Card>
  );
}