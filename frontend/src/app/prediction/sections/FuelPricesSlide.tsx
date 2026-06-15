"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ReferenceLine } from "recharts"
import { ChartContainer } from "./shared"

const DATA = [
  { date: "Jan 2019", ron95: 2.08, ron97: 2.58, diesel: 2.18 },
  { date: "Jan 2020", ron95: 2.08, ron97: 2.58, diesel: 2.18 },
  { date: "Jan 2021", ron95: 2.05, ron97: 2.45, diesel: 2.15 },
  { date: "Jun 2022", ron95: 2.05, ron97: 3.75, diesel: 2.15 },
  { date: "Jan 2023", ron95: 2.05, ron97: 3.35, diesel: 2.15 },
  { date: "Jan 2024", ron95: 2.05, ron97: 3.47, diesel: 2.15 },
  { date: "Jun 2024", ron95: 2.05, ron97: 3.35, diesel: 2.15 },
  { date: "Sep 2025", ron95: 1.99, ron97: 3.55, diesel: 2.15 },
  { date: "Mar 2026", ron95: 2.35, ron97: 4.10, diesel: 2.15 },
]

export default function FuelPricesSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Fuel Prices &amp; Subsidy Burden</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">RON95, RON97 &amp; diesel — subsidy impact on government &amp; voters</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://storage.data.gov.my/commodities/fuelprice.csv" target="_blank" className="underline">DOSM Fuel Price Raw</a> &middot; <a href="/data/insights/economy/fuel_prices_weekly.csv" className="underline">Download Processed CSV</a></p>
          <ChartContainer config={{ ron95: { label: "RON95 RM/L", color: "var(--chart-1)" }, ron97: { label: "RON97 RM/L", color: "var(--chart-2)" }, diesel: { label: "Diesel RM/L", color: "var(--chart-3)" } }}>
            <LineChart data={DATA}>
              <CartesianGrid vertical={false} />
              <XAxis dataKey="date" tick={{ fontSize: 9 }} interval={1} />
              <YAxis domain={[1.5, 4.5]} tick={{ fontSize: 10 }} />
              <Tooltip />
              <Legend iconType="circle" wrapperStyle={{ fontSize: "10px" }} />
              <ReferenceLine y={2.05} stroke="var(--border)" strokeDasharray="3" label={{ value: "RON95 subsidy cap", fontSize: 9, position: "right" }} />
              <Line dataKey="ron95" stroke="var(--chart-1)" strokeWidth={2.5} dot={{ r: 4 }} />
              <Line dataKey="ron97" stroke="var(--chart-2)" strokeWidth={2} dot={{ r: 3 }} />
              <Line dataKey="diesel" stroke="var(--chart-3)" strokeWidth={2} dot={{ r: 3 }} />
            </LineChart>
          </ChartContainer>
          <div className="mt-3 space-y-1 text-xs">
            <p><strong>Subsidy cost:</strong> RM52bn (2022) on fuel alone — 74% of total subsidies. Diesel reform (Jun 2024) saved RM4bn/yr. RON95 partial reform (Sep 2025) saved ~RM4.2bn/yr.</p>
            <p><strong>Hormuz crisis (Mar 2026)</strong>: Monthly subsidy cost ballooned to RM3.2bn. Oil at $120+.</p>
            <p className="text-muted-foreground"><strong>Election implication:</strong> Full RON95 removal is still pending — the biggest fiscal reform. Govt has incentive to call GE16 before removing it.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
