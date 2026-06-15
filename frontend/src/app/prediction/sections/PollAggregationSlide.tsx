"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts"
import { ChartContainer, APPROVAL_DATA } from "./shared"

const POLL_DATA = [
  { date: "Nov 2022", ph: 38.0, pn: 30.1, bn: 23.4, source: "GE15 actual result" },
  { date: "Feb 2023", ph: 33, pn: 26, bn: 22, source: "Merdeka Center" },
  { date: "Nov 2023", ph: 31, pn: 29, bn: 24, source: "Merdeka Center" },
  { date: "Dec 2024", ph: 34, pn: 28, bn: 21, source: "Merdeka Center" },
  { date: "Jun 2025", ph: 33, pn: 27, bn: 22, source: "Merdeka Center" },
]

export default function PollAggregationSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Poll Aggregation Model</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Combined voting intention averages from available surveys</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Sources: <a href="https://merdeka.org" target="_blank" className="underline">Merdeka Center</a> &middot; <a href="https://en.wikipedia.org/wiki/Next_Malaysian_general_election" target="_blank" className="underline">Next GE page</a></p>
          <ChartContainer config={{ ph: { label: "PH", color: "var(--chart-1)" }, pn: { label: "PN", color: "var(--chart-2)" }, bn: { label: "BN", color: "var(--chart-3)" } }}>
            <LineChart data={POLL_DATA} margin={{ top: 10, right: 20, left: 0, bottom: 10 }}>
              <CartesianGrid vertical={false} />
              <XAxis dataKey="date" tick={{ fontSize: 9 }} />
              <YAxis domain={[15, 42]} tick={{ fontSize: 9 }} />
              <Tooltip />
              <Legend iconType="circle" wrapperStyle={{ fontSize: "10px" }} />
              <Line dataKey="ph" stroke="var(--chart-1)" strokeWidth={2.5} dot={{ r: 4 }} />
              <Line dataKey="pn" stroke="var(--chart-2)" strokeWidth={2.5} dot={{ r: 4 }} />
              <Line dataKey="bn" stroke="var(--chart-3)" strokeWidth={2} dot={{ r: 3 }} strokeDasharray="3" />
            </LineChart>
          </ChartContainer>
          <div className="mt-3 grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
            <div className="p-2 border border-foreground/10 rounded">
              <p className="font-medium">PH: 31-36%</p>
              <p className="text-muted-foreground">Stable but below GE15 result (38%). Needs BN + GPS alliance to govern.</p>
            </div>
            <div className="p-2 border border-foreground/10 rounded">
              <p className="font-medium">PN: 26-29%</p>
              <p className="text-muted-foreground">Stable but concentrated in safe seats. Needs to expand beyond Malay heartland.</p>
            </div>
            <div className="p-2 border border-foreground/10 rounded">
              <p className="font-medium">BN: 20-24%</p>
              <p className="text-muted-foreground">Declining from ~30% (GE15 actual). UMNO brand damaged. Kingmaker role.</p>
            </div>
          </div>
          <div className="mt-2 text-xs text-muted-foreground">
            <p><strong>Note:</strong> Limited polling data available. Merdeka Center is the only regular independent pollster. More frequent polling needed for accurate aggregation. The AE16 prediction is based more on structural factors (coalition math, economic trends) than polling averages.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
