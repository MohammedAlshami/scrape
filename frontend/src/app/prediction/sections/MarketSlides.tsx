"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine } from "recharts"
import { ChartContainer, ECONOMY_DATA } from "./shared"

const OPR_DATA = [
  { year: "2019", opr: 3.0 }, { year: "2020", opr: 1.75 }, { year: "2021", opr: 1.75 },
  { year: "2022", opr: 2.75 }, { year: "2023", opr: 3.0 }, { year: "2024", opr: 3.0 },
  { year: "2025", opr: 2.75 }, { year: "2026e", opr: 2.75 },
]

export function OPRSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">OPR & Monetary Policy</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">BNM Overnight Policy Rate — cost of borrowing signal</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://storage.data.gov.my/finsector/interest_rates.csv" target="_blank" className="underline">DOSM/BNM</a> &middot; <a href="/data/insights/economy/opr_base_rate.csv" className="underline">Download CSV</a></p>
          <ChartContainer config={{ opr: { label: "OPR %", color: "var(--chart-1)" } }}>
            <LineChart data={OPR_DATA}>
              <CartesianGrid vertical={false} />
              <XAxis dataKey="year" tick={{ fontSize: 10 }} />
              <YAxis domain={[0, 4]} tick={{ fontSize: 10 }} />
              <Tooltip />
              <ReferenceLine y={2.75} stroke="var(--border)" strokeDasharray="3" label={{ value: "Current: 2.75%", fontSize: 9, position: "right" }} />
              <Line dataKey="opr" stroke="var(--chart-1)" strokeWidth={2.5} dot={{ r: 5 }} type="stepAfter" />
            </LineChart>
          </ChartContainer>
          <div className="mt-3 text-xs space-y-1">
            <p><strong>COVID emergency:</strong> Cut to 1.75% (Jul 2020) — record low. <strong>Normalization:</strong> Hiked to 3.0% (May-Sep 2023). <strong>Current:</strong> 2.75% (cut Jan 2025).</p>
            <p className="text-muted-foreground">OPR affects mortgage rates, car loans, business borrowing — directly impacts voter cost of living. Stable OPR favors incumbents; rate hikes before an election hurt govt popularity.</p>
          </div>
        </div>
      </div>
    </section>
  )
}

export function KLSEOilFXSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Oil, Ringgit & Stock Market</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">External economic signals & election cycle</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <p className="text-xs text-muted-foreground mb-2">Sources: <a href="https://finance.yahoo.com/quote/BZ=F/" target="_blank" className="underline">Yahoo Finance (Brent)</a> &middot; <a href="https://finance.yahoo.com/quote/%5EKLSE/" target="_blank" className="underline">KLSE</a> &middot; <a href="https://storage.data.gov.my/finsector/exchangerates.csv" target="_blank" className="underline">DOSM FX</a></p>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-2 h-3/5">
            <div className="flex flex-col">
              <span className="text-xs font-medium mb-1 shrink-0">KLCI Index (year-end close)</span>
              <div className="flex-1 min-h-0">
                <ChartContainer config={{ klse: { label: "KLCI", color: "var(--chart-4)" } }}>
                  <LineChart data={ECONOMY_DATA}>
                    <CartesianGrid vertical={false} />
                    <XAxis dataKey="year" tick={{ fontSize: 8 }} />
                    <YAxis domain={[1400, 1700]} tick={{ fontSize: 8 }} />
                    <Tooltip />
                    <ReferenceLine y={1495} stroke="red" strokeDasharray="3" label={{ value: "GE15", fontSize: 8 }} />
                    <Line dataKey="klse" stroke="var(--chart-4)" strokeWidth={2} dot={{ r: 3 }} />
                  </LineChart>
                </ChartContainer>
              </div>
            </div>
            <div className="flex flex-col">
              <span className="text-xs font-medium mb-1 shrink-0">Economy Dashboard</span>
              <div className="flex-1 text-xs space-y-2 p-2">
                <div className="p-2 border border-foreground/10 rounded">
                  <p className="font-medium">Ringgit (MYR/USD)</p>
                  <p className="text-muted-foreground">2023: 4.60 | 2024: 4.70 | 2025: 4.12 | 2026: ~4.20</p>
                  <p className="text-muted-foreground">Strengthened from 4.80 low (Feb 2024) to 4.12 (Dec 2025). Strong ringgit lowers import costs — positive for voters.</p>
                </div>
                <div className="p-2 border border-foreground/10 rounded">
                  <p className="font-medium">Brent Crude Oil</p>
                  <p className="text-muted-foreground">2023: ~$82 | 2024: ~$80 | 2025: ~$75 | Mar 2026: $120+ (Hormuz crisis)</p>
                  <p className="text-muted-foreground">Oil spike is a double-edged sword: boosts Petronas revenue but inflates subsidy costs (RM3.2bn/month). Peace deal would crash prices.</p>
                </div>
                <div className="p-2 border border-amber-200 bg-amber-50/30 rounded">
                  <p className="font-medium text-amber-700">GE16 Signal</p>
                  <p className="text-amber-600">KLCI tends to rally before elections. If market rises through mid-2027, it signals confidence in govt continuity. A crash would force early election.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
