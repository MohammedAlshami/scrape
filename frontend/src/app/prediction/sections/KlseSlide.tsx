"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine } from "recharts"
import { ChartContainer } from "./shared"
import { useCsv } from "./useData"

export default function KlseSlide() {
  const raw = useCsv<any>("/data/insights/market/klse_monthly.csv")
  const data = raw.filter(r => r.month?.startsWith("20") && r.avg_close).map(r => ({
    month: r.month,
    close: parseFloat(r.avg_close),
  })).filter(r => !isNaN(r.close) && r.close > 0).slice(-120)

  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">KLSE / KLCI Index</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">FBM KLCI monthly close — election cycle correlation</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://finance.yahoo.com/quote/%5EKLSE/" target="_blank" className="underline">Yahoo Finance</a> &middot; <a href="/data/insights/market/klse_monthly.csv" className="underline">Download CSV</a></p>
          {data.length > 0 ? (
            <ChartContainer config={{ close: { label: "KLCI", color: "var(--chart-4)" } }}>
              <LineChart data={data}>
                <CartesianGrid vertical={false} />
                <XAxis dataKey="month" tick={{ fontSize: 8 }} interval={11} />
                <YAxis domain={[1400, 1900]} tick={{ fontSize: 9 }} />
                <Tooltip />
                <ReferenceLine y={1495} stroke="red" strokeDasharray="3" label={{ value: "GE15", fontSize: 9, position: "right" }} />
                <Line dataKey="close" stroke="var(--chart-4)" strokeWidth={2} dot={false} />
              </LineChart>
            </ChartContainer>
          ) : <div className="flex items-center justify-center h-full text-muted-foreground text-sm">Loading KLCI data...</div>}
          <div className="mt-3 text-xs space-y-1">
            <p><strong>GE15 impact:</strong> KLCI fell from ~1,500 to ~1,450 before GE15, recovered after hung parliament resolved.</p>
            <p><strong>Current:</strong> ~1,620 (Jun 2026). Up from 1,454 (Dec 2023).</p>
            <p className="text-muted-foreground">KLCI tends to rally in the 3-6 months before elections. A sustained rally through mid-2027 supports the full-term scenario.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
