"use client"

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine } from "recharts"
import { ChartContainer } from "./shared"
import { useCsv, type EconomyRow } from "./useData"

export default function GDPTrendSlide() {
  const data = useCsv<EconomyRow>("/data/insights/combined/election_timing_factors.csv")
  const gdpData = data.filter(r => r.gdp_real && parseInt(r.year) >= 2010).map(r => ({
    year: r.year,
    gdp: parseFloat(r.gdp_real),
  }))
  const avg = gdpData.length ? (gdpData.reduce((s, r) => s + r.gdp, 0) / gdpData.length).toFixed(1) : "4.0"

  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">GDP Growth Trend</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Recent growth vs historical average</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://api.data.gov.my/data-catalogue?id=gdp_gni_annual_real" target="_blank" className="underline">DOSM Data Catalogue</a> &middot; <a href="/data/insights/economy/gdp_annual.csv" className="underline">Download CSV</a></p>
          {gdpData.length > 0 ? (
            <ChartContainer config={{ gdp: { label: "GDP Growth %", color: "var(--chart-1)" } }}>
              <BarChart data={gdpData}>
                <CartesianGrid vertical={false} />
                <XAxis dataKey="year" tick={{ fontSize: 10 }} />
                <YAxis domain={[-8, 10]} tick={{ fontSize: 10 }} />
                <Tooltip />
                <ReferenceLine y={0} stroke="var(--border)" />
                <ReferenceLine y={parseFloat(avg)} stroke="var(--chart-2)" strokeDasharray="4" label={{ value: `Avg ${avg}%`, position: "right", fontSize: 10 }} />
                <Bar dataKey="gdp" fill="var(--chart-1)" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ChartContainer>
          ) : (
            <div className="flex items-center justify-center h-full text-muted-foreground text-sm">Loading GDP data...</div>
          )}
          <div className="mt-3 space-y-1 text-xs">
            <p><strong>Historical average (2010-2025):</strong> {avg}%</p>
            <p><strong>2024:</strong> 5.1% — above average. <strong>2025:</strong> 5.2%. <strong>2026e:</strong> 5.0%.</p>
            <p className="text-muted-foreground">GDP recovered sharply from COVID (-5.6% in 2020). Current growth is healthy but moderating. No recession signal that would force a snap election.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
