"use client"

import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts"
import { ChartContainer } from "./shared"

const DATA = [
  { year: "2019", cpi: 0.7, fuel: 2.08, food: 1.5, housing: 1.2 },
  { year: "2020", cpi: -1.1, fuel: 2.08, food: 0.8, housing: 0.5 },
  { year: "2021", cpi: 2.5, fuel: 2.05, food: 2.8, housing: 1.0 },
  { year: "2022", cpi: 3.4, fuel: 2.05, food: 5.6, housing: 2.1 },
  { year: "2023", cpi: 2.5, fuel: 2.05, food: 4.2, housing: 1.8 },
  { year: "2024", cpi: 1.8, fuel: 2.05, food: 2.5, housing: 1.5 },
  { year: "2025", cpi: 1.2, fuel: 1.99, food: 2.0, housing: 1.2 },
  { year: "2026e", cpi: 2.0, fuel: 2.35, food: 3.0, housing: 2.0 },
]

export default function CostOfLivingSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Cost of Living Pressure Index</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Composite: CPI, fuel, food &amp; housing components</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Sources: <a href="https://api.data.gov.my/data-catalogue?id=cpi_annual_inflation" target="_blank" className="underline">DOSM CPI Data</a> &middot; <a href="https://storage.data.gov.my/commodities/fuelprice.csv" target="_blank" className="underline">Fuel Price Raw</a> &middot; <a href="/data/insights/economy/inflation_overall.csv" className="underline">Download CPI CSV</a></p>
          <ChartContainer config={{ cpi: { label: "CPI Inflation %", color: "var(--chart-1)" }, food: { label: "Food Inflation %", color: "var(--chart-2)" }, housing: { label: "Housing Inflation %", color: "var(--chart-3)" } }}>
            <LineChart data={DATA}>
              <CartesianGrid vertical={false} />
              <XAxis dataKey="year" tick={{ fontSize: 10 }} />
              <YAxis domain={[-2, 7]} tick={{ fontSize: 10 }} />
              <Tooltip />
              <Legend iconType="circle" wrapperStyle={{ fontSize: "10px" }} />
              <Line dataKey="cpi" stroke="var(--chart-1)" strokeWidth={2} dot={{ r: 3 }} />
              <Line dataKey="food" stroke="var(--chart-2)" strokeWidth={2} dot={{ r: 3 }} />
              <Line dataKey="housing" stroke="var(--chart-3)" strokeWidth={2} dot={{ r: 3 }} />
            </LineChart>
          </ChartContainer>
          <div className="mt-3 space-y-1 text-xs">
            <p><strong>Food inflation</strong> has been the biggest driver, peaking at 5.6% in 2022. It remains above headline CPI.</p>
            <p><strong>Fuel price</strong>: RON95 was held at RM2.05 from 2021-2024 via subsidies. Budi95 (Sep 2025) cut it to RM1.99 but capped at 300L/month.</p>
            <p className="text-muted-foreground">The Oust Anwar rally (Jul 2025) was triggered by cost of living concerns. This is the #1 voter issue heading into GE16.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
