"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine } from "recharts"
import { ChartContainer } from "./shared"
import { useCsv, type EconomyRow } from "./useData"

export default function UnemploymentSlide() {
  const raw = useCsv<EconomyRow>("/data/insights/combined/election_timing_factors.csv")
  const data = raw.filter(r => r.unemployment_pct && parseInt(r.year) >= 2015).map(r => ({
    year: r.year,
    rate: parseFloat(r.unemployment_pct),
  }))

  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Unemployment Rate</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Labour market health & voter sentiment indicator</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://api.data.gov.my/data-catalogue?id=lfs_month" target="_blank" className="underline">DOSM Labour Force</a> &middot; <a href="/data/insights/economy/unemployment_monthly.csv" className="underline">Download CSV</a></p>
          {data.length > 0 ? (
            <ChartContainer config={{ rate: { label: "Unemployment %", color: "var(--chart-3)" } }}>
              <LineChart data={data}>
                <CartesianGrid vertical={false} />
                <XAxis dataKey="year" tick={{ fontSize: 10 }} />
                <YAxis domain={[0, 6]} tick={{ fontSize: 10 }} />
                <Tooltip />
                <ReferenceLine y={3} stroke="var(--border)" strokeDasharray="3" label={{ value: "~3% natural rate", fontSize: 9, position: "right" }} />
                <Line dataKey="rate" stroke="var(--chart-3)" strokeWidth={2.5} dot={{ r: 4 }} />
              </LineChart>
            </ChartContainer>
          ) : <div className="flex items-center justify-center h-full text-muted-foreground text-sm">Loading...</div>}
          <div className="mt-3 text-xs space-y-1">
            <p><strong>Current:</strong> ~3.0% (2026) — near full employment. <strong>COVID peak:</strong> 5.3% (2020).</p>
            <p className="text-muted-foreground">Low unemployment supports the incumbent — voters with jobs are less likely to vote for change. Historically, elections during low unemployment favor the government.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
