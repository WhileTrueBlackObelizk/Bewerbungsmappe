import * as React from "react";
import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Toggle } from "@/components/ui/toggle";
import { Moon, Sun, Clock, AlarmClock } from "lucide-react";
import { TimeInput } from "./TimeInput";
import { SettingsPanel } from "./SettingsPanel";
import { SleepTimeResults } from "./SleepTimeResults";
import { AlarmSystem } from "./AlarmSystem";
import { useSleepCalculator } from "./useSleepCalculator";
import { useSettings } from "./useSettings";

export function SleepCycleCalculator() {
  const [mode, setMode] = useState<"bedtime" | "waketime">("bedtime");
  const [selectedTime, setSelectedTime] = useState("");
  const [showSettings, setShowSettings] = useState(false);

  const { settings, updateSettings } = useSettings();
  const { calculateSleepTimes } = useSleepCalculator(settings);

  const [results, setResults] = useState<
    Array<{ time: string; cycles: number }>
  >([]);
  const [alarmTime, setAlarmTime] = useState<string>("");

  useEffect(() => {
    if (selectedTime) {
      const times = calculateSleepTimes(selectedTime, mode);
      setResults(times);
    } else {
      setResults([]);
    }
  }, [selectedTime, mode, calculateSleepTimes]);

  const handleSetAlarm = (time: string) => {
    setAlarmTime(time);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-red-950/20 to-black flex items-center justify-center p-2 sm:p-4">
      <div className="w-full max-w-sm sm:max-w-md lg:max-w-lg">
        <Card className="red-glow border-red-900/30 bg-black/60 backdrop-blur-sm h-fit">
          <CardHeader className="text-center pb-3 sm:pb-6">
            <CardTitle className="flex items-center justify-center gap-2 text-red-100 text-lg sm:text-xl">
              <Moon className="h-5 w-5 sm:h-6 sm:w-6 text-red-400" />
              <span className="hidden sm:inline">Perfect Sleep</span>
              <span className="sm:hidden">Sleep Cycle</span>
            </CardTitle>
          </CardHeader>

          <CardContent className="space-y-4 sm:space-y-6 p-4 sm:p-6 pt-0">
            <div className="flex justify-center">
              <div className="flex bg-red-950/40 rounded-lg p-1 border border-red-900/30 w-full max-w-xs">
                <Toggle
                  pressed={mode === "bedtime"}
                  onPressedChange={() => setMode("bedtime")}
                  className="flex items-center justify-center gap-1 sm:gap-2 data-[state=on]:bg-red-800/50 data-[state=on]:text-red-100 flex-1 text-xs sm:text-sm"
                >
                  <Moon className="h-3 w-3 sm:h-4 sm:w-4" />
                  <span className="hidden xs:inline">Bedtime</span>
                  <span className="xs:hidden">Bed</span>
                </Toggle>
                <Toggle
                  pressed={mode === "waketime"}
                  onPressedChange={() => setMode("waketime")}
                  className="flex items-center justify-center gap-1 sm:gap-2 data-[state=on]:bg-red-800/50 data-[state=on]:text-red-100 flex-1 text-xs sm:text-sm"
                >
                  <Sun className="h-3 w-3 sm:h-4 sm:w-4" />
                  <span className="hidden xs:inline">Wake Time</span>
                  <span className="xs:hidden">Wake</span>
                </Toggle>
              </div>
            </div>

            <TimeInput
              mode={mode}
              value={selectedTime}
              onChange={setSelectedTime}
            />

            <div className="max-h-64 sm:max-h-80 overflow-y-auto">
              <SleepTimeResults
                results={results}
                mode={mode}
                onSetAlarm={handleSetAlarm}
              />
            </div>

            <div className="flex justify-center">
              <Button
                variant="outline"
                onClick={() => setShowSettings(!showSettings)}
                className="flex items-center gap-2 border-red-700 text-red-200 hover:bg-red-900/30 red-glow-hover text-xs sm:text-sm"
                size="sm"
              >
                <Clock className="h-3 w-3 sm:h-4 sm:w-4" />
                Settings
              </Button>
            </div>

            {showSettings && (
              <div className="max-h-48 sm:max-h-60 overflow-y-auto">
                <SettingsPanel
                  settings={settings}
                  onUpdateSettings={updateSettings}
                />
              </div>
            )}

            <AlarmSystem
              alarmTime={alarmTime}
              onClearAlarm={() => setAlarmTime("")}
            />
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
