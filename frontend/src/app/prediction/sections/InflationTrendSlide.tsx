"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine } from "recharts"
import { ChartContainer } from "./shared"
import { useCsv } from "./useData"

type InflationRow = { year: string; division: string; inflation_rate_pct: string }

export default function InflationTrendSlide() {
  const raw = useCsv<InflationRow>("/data/insights/economy/inflation_overall.csv")
  const data = raw.filter(r => parseInt(r.year) >= 2010).map(r => ({
    year: r.year,
    inflation: parseFloat(r.inflation_rate_pct),
  }))

  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Inflation Trends</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">CPI headline inflation — DOSM</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://api.data.gov.my/data-catalogue?id=cpi_annual_inflation" target="_blank" className="underline">DOSM Data Catalogue</a> &middot; <a href="/data/insights/economy/inflation_overall.csv" className="underline">Download CSV</a></p>
          <ChartContainer config={{ inflation: { label: "Inflation %", color: "var(--chart-2)" } }}>
            <LineChart data={data}>
              <CartesianGrid vertical={false} />
              <XAxis dataKey="year" tick={{ fontSize: 10 }} />
              <YAxis domain={[-2, 6]} tick={{ fontSize: 10 }} />
              <Tooltip />
              <ReferenceLine y={2} stroke="var(--border)" strokeDasharray="3" label={{ value: "BNM target 2%", position: "right", fontSize: 9 }} />
              <Line dataKey="inflation" stroke="var(--chart-2)" strokeWidth={2.5} dot={{ r: 4 }} />
            </LineChart>
          </ChartContainer>
          <div className="mt-3 space-y-1 text-xs">
            <p><strong>Current:</strong> 1.2% (2025) — below BNM&apos;s 2% target. Forecast ~2.0% for 2026.</p>
            <p><strong>Peak:</strong> 5.4% (2008 oil crisis), 3.8% (2017), 3.4% (2022 post-COVID).</p>
            <p className="text-muted-foreground">Low inflation is partly artificial — kept low by fuel subsidies. If RON95 subsidy is removed, inflation could spike 2-3pp, which would be a major election issue.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
