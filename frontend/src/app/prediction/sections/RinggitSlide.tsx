"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine } from "recharts"
import { ChartContainer } from "./shared"
import { useCsv } from "./useData"

export default function RinggitSlide() {
  const raw = useCsv<any>("/data/insights/economy/myr_usd_monthly.csv")
  const data = raw.filter(r => r.myr_per_usd && parseFloat(r.myr_per_usd) > 0).map(r => {
    const val = parseFloat(r.myr_per_usd)
    return {
      date: (r.date || "").slice(0, 7),
      rate: val,
    }
  }).filter(r => r.date && !isNaN(r.rate) && r.rate > 0.1 && r.rate < 1)

  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Ringgit Exchange Rate</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">MYR/USD monthly — import costs & voter sentiment</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://storage.data.gov.my/finsector/exchangerates.csv" target="_blank" className="underline">DOSM/Bank Negara</a> &middot; <a href="/data/insights/economy/myr_usd_monthly.csv" className="underline">Download CSV</a></p>
          {data.length > 0 ? (
            <ChartContainer config={{ rate: { label: "MYR per USD (inverse)", color: "var(--chart-2)" } }}>
              <LineChart data={data}>
                <CartesianGrid vertical={false} />
                <XAxis dataKey="date" tick={{ fontSize: 8 }} interval={35} />
                <YAxis domain={[0.2, 0.3]} tick={{ fontSize: 9 }} tickFormatter={(v) => `${(1/v).toFixed(2)}`} />
                <Tooltip />
                <ReferenceLine y={0.238} stroke="green" strokeDasharray="3" />
                <Line dataKey="rate" stroke="var(--chart-2)" strokeWidth={2} dot={false} />
              </LineChart>
            </ChartContainer>
          ) : <div className="flex items-center justify-center h-full text-muted-foreground text-sm">Loading FX data...</div>}
          <div className="mt-3 text-xs space-y-1">
            <p><strong>Note:</strong> Chart shows inverse rate (USD per MYR). Higher = stronger ringgit. Current ~4.20 MYR/USD.</p>
            <p><strong>Range:</strong> Weakened from 4.12 (Jan 2023) to 4.80 (Feb 2024), strengthened back to 4.12 (Dec 2025).</p>
            <p className="text-muted-foreground">Strong ringgit lowers import costs — directly benefits voters. Positive signal for incumbent. Sharp weakening would hurt.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
