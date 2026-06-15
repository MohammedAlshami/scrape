"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine } from "recharts"
import { ChartContainer } from "./shared"
import { useCsv } from "./useData"

export default function BrentSlide() {
  const raw = useCsv<any>("/data/insights/economy/brent_crude_daily.csv")
  const data = raw.filter(r => r.price_usd && parseFloat(r.price_usd) > 0).map(r => ({
    date: (r.date || "").slice(0, 7),
    price: parseFloat(r.price_usd),
  })).filter(r => r.date && !isNaN(r.price) && r.price > 30 && r.price < 150)
    .reduce((acc: any[], curr) => {
      if (!acc.length || acc[acc.length-1].date !== curr.date) acc.push(curr)
      return acc
    }, [])

  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Brent Crude Oil Price</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Global oil price cycle & Malaysia's fiscal exposure</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://finance.yahoo.com/quote/BZ=F/" target="_blank" className="underline">Yahoo Finance</a> &middot; <a href="/data/insights/economy/brent_crude_daily.csv" className="underline">Download CSV</a></p>
          {data.length > 0 ? (
            <ChartContainer config={{ price: { label: "Brent $/bbl", color: "var(--chart-1)" } }}>
              <LineChart data={data}>
                <CartesianGrid vertical={false} />
                <XAxis dataKey="date" tick={{ fontSize: 8 }} interval={11} />
                <YAxis domain={[30, 140]} tick={{ fontSize: 9 }} />
                <Tooltip />
                <ReferenceLine y={80} stroke="var(--border)" strokeDasharray="3" label={{ value: "Avg ~$80", fontSize: 8, position: "right" }} />
                <Line dataKey="price" stroke="var(--chart-1)" strokeWidth={2} dot={false} />
              </LineChart>
            </ChartContainer>
          ) : <div className="flex items-center justify-center h-full text-muted-foreground text-sm">Loading Brent data ({raw.length} raw rows)...</div>}
          <div className="mt-3 text-xs space-y-1">
            <p><strong>COVID crash:</strong> $30 (Apr 2020). <strong>Recovery:</strong> $80-90 (2021-2023).</p>
            <p><strong>Iran war:</strong> Surged to $120+ (Mar 2026) after Hormuz blockade.</p>
            <p className="text-muted-foreground">$120 oil = higher Petronas dividends but higher subsidy costs. Peace deal would crash oil to $60-70.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
