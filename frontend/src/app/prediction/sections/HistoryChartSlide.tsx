"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from "recharts"
import { ChartContainer } from "./shared"

const DATA = [
  { ge: "GE10", days: 19, turnout: 71.2 }, { ge: "GE11", days: 17, turnout: 73.0 },
  { ge: "GE12", days: 24, turnout: 75.4 }, { ge: "GE13", days: 32, turnout: 84.6 },
  { ge: "GE14", days: 32, turnout: 82.3 }, { ge: "GE15", days: 40, turnout: 74.1 },
]

export default function HistoryChartSlide() {
  return (
    <section id="history-chart" className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Election Timing Trend</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Dissolution-to-polling days &amp; voter turnout (GE10-GE15)</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://en.wikipedia.org/wiki/Elections_in_Malaysia" target="_blank" className="underline">Wikipedia</a></p>
          <ChartContainer config={{ days: { label: "Days", color: "var(--chart-1)" }, turnout: { label: "Turnout %", color: "#e74c3c" } }}>
            <LineChart data={DATA} margin={{ top: 10, right: 20, left: 0, bottom: 5 }}>
              <CartesianGrid vertical={false} />
              <XAxis dataKey="ge" tick={{ fontSize: 11 }} />
              <YAxis yAxisId="left" domain={[10, 50]} tick={{ fontSize: 10 }} />
              <YAxis yAxisId="right" orientation="right" domain={[65, 90]} tick={{ fontSize: 10 }} />
              <Tooltip />
              <Line yAxisId="left" dataKey="days" stroke="var(--chart-1)" strokeWidth={2} dot={{ r: 5 }} name="Days" />
              <Line yAxisId="right" dataKey="turnout" stroke="#e74c3c" strokeWidth={2} dot={{ r: 5 }} name="Turnout %" strokeDasharray="4" />
            </LineChart>
          </ChartContainer>
          <p className="text-xs mt-2 text-muted-foreground">Dissolution-to-polling doubled (19d→40d). Turnout peaked at 84.6% (GE13). Every GE since 1999 called early except GE11, GE13.</p>
        </div>
      </div>
    </section>
  )
}
