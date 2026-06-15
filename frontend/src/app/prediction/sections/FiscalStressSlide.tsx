"use client"

import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine } from "recharts"
import { ChartContainer } from "./shared"
import { useCsv, type FiscalRow } from "./useData"

export function DebtDeficitSlide() {
  const data = useCsv<FiscalRow>("/data/insights/economy/fiscal_data.csv")
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Government Debt &amp; Deficit</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Debt ceiling pressure &amp; fiscal consolidation progress</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://en.wikipedia.org/wiki/Economy_of_Malaysia" target="_blank" className="underline">Wikipedia (Economy of Malaysia)</a> &middot; <a href="/data/insights/economy/fiscal_data.csv" className="underline">Download CSV</a></p>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-3 h-3/5">
            <div className="flex flex-col">
              <span className="text-xs font-medium mb-1">Government Debt (% of GDP)</span>
              <div className="flex-1 min-h-0">
                <ChartContainer config={{ debt_pct: { label: "Debt % of GDP", color: "var(--chart-1)" } }}>
                  <BarChart data={data}>
                    <CartesianGrid vertical={false} />
                    <XAxis dataKey="year" tick={{ fontSize: 9 }} />
                    <YAxis domain={[50, 75]} tick={{ fontSize: 9 }} />
                    <Tooltip />
                    <ReferenceLine y={65} stroke="red" strokeDasharray="3" label={{ value: "Legal limit 65%", fontSize: 8, position: "right" }} />
                    <Bar dataKey="debt_pct" fill="var(--chart-1)" radius={[2, 2, 0, 0]} />
                  </BarChart>
                </ChartContainer>
              </div>
            </div>
            <div className="flex flex-col">
              <span className="text-xs font-medium mb-1">Budget Deficit (% of GDP)</span>
              <div className="flex-1 min-h-0">
                <ChartContainer config={{ deficit_pct: { label: "Deficit %", color: "var(--chart-2)" } }}>
                  <BarChart data={data}>
                    <CartesianGrid vertical={false} />
                    <XAxis dataKey="year" tick={{ fontSize: 9 }} />
                    <YAxis domain={[0, 8]} tick={{ fontSize: 9 }} />
                    <Tooltip />
                    <ReferenceLine y={3} stroke="var(--border)" strokeDasharray="3" label={{ value: "Maastricht 3%", fontSize: 8, position: "right" }} />
                    <Bar dataKey="deficit_pct" fill="var(--chart-2)" radius={[2, 2, 0, 0]} />
                  </BarChart>
                </ChartContainer>
              </div>
            </div>
          </div>
          <div className="mt-3 space-y-1 text-xs">
            <p><strong>Debt:</strong> 66.86% of GDP (2024), above the self-imposed 65% legal limit. Projected to reach ~70% by 2025-2027.</p>
            <p><strong>Deficit:</strong> Narrowed from 6.2% (2020 COVID) to 3.5% (2026 budget). Fiscal consolidation is happening but slowly.</p>
            <p className="text-muted-foreground"><strong>Election implication:</strong> Limited fiscal space. Debt at 70% constrains pre-election spending. Credit rating stable (A-/A3) but at risk if deficit doesn&apos;t narrow.</p>
          </div>
        </div>
      </div>
    </section>
  )
}

export function SubsidyBurdenSlide() {
  const data = useCsv<FiscalRow>("/data/insights/economy/fiscal_data.csv")
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Fuel Subsidy Burden</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Annual subsidy costs &amp; reform progress</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://en.wikipedia.org/wiki/Economy_of_Malaysia" target="_blank" className="underline">Wikipedia</a> &middot; <a href="https://en.wikipedia.org/wiki/Anwar_Ibrahim" target="_blank" className="underline">Anwar page</a> &middot; <a href="/data/insights/economy/fiscal_data.csv" className="underline">Download CSV</a></p>
          <ChartContainer config={{ subsidy_bn: { label: "Subsidy RM bn", color: "var(--chart-3)" } }}>
            <BarChart data={data}>
              <CartesianGrid vertical={false} />
              <XAxis dataKey="year" tick={{ fontSize: 10 }} />
              <YAxis domain={[20, 80]} tick={{ fontSize: 10 }} />
              <Tooltip />
              <Bar dataKey="subsidy_bn" fill="var(--chart-3)" radius={[4, 4, 0, 0]} />
            </BarChart>
          </ChartContainer>
          <div className="mt-3 space-y-1 text-xs">
            <p><strong>2022 peak:</strong> RM70.3bn total subsidies (RM52bn on fuel alone — 74% of total). Source: Economy of Malaysia page.</p>
            <p><strong>Diesel reform (Jun 2024):</strong> Saved RM4bn/yr. Peninsular Malaysia only — Sabah/Sarawak exempted. Source: Anwar Ibrahim page, AP News.</p>
            <p><strong>RON95 reform (Sep 2025):</strong> Budi95 at RM1.99/L, capped at 300L/month. Saved ~RM4.2bn/yr (revised down from RM8bn).</p>
            <p><strong>Full RON95 top-15% removal:</strong> Still <strong>pending</strong> — would save RM8bn+ but was shelved after public backlash (CNA, Oct 2024).</p>
            <p className="text-muted-foreground"><strong>Election implication:</strong> The govt has incentive to call GE16 BEFORE full RON95 removal. Voters haven&apos;t felt the full pain yet.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
