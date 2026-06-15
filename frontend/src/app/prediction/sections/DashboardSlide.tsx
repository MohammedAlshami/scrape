"use client"

import { LineChart, ComposedChart, Bar, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from "recharts"
import { ChartContainer, APPROVAL_DATA, ECONOMY_DATA, SEATS_DATA } from "./shared"

export function ApprovalChartSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">PM Approval Trend</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Anwar Ibrahim — Merdeka Center surveys</p>
        </div>
        <div className="flex-1 min-h-0">
          <ChartContainer config={{ approval: { label: "Approval", color: "var(--chart-1)" } }}>
            <LineChart data={APPROVAL_DATA.filter(d => d.pm === "Anwar")}>
              <CartesianGrid vertical={false} />
              <XAxis dataKey="date" tick={{ fontSize: 11 }} />
              <YAxis domain={[40, 70]} tick={{ fontSize: 11 }} />
              <Tooltip />
              <Line dataKey="approval" stroke="var(--chart-1)" strokeWidth={2.5} dot={{ r: 5 }} />
            </LineChart>
          </ChartContainer>
          <p className="text-xs text-muted-foreground mt-2">Source: <a href="https://merdeka.org" target="_blank" className="underline">Merdeka Center Survey Reports</a> &middot; <a href="/data/insights/polls/approval_ratings.csv" className="underline">Download CSV</a></p>
          <p className="text-xs mt-2">Anwar&apos;s approval recovered from 50% (Nov 2023) to 55% (Jun 2025). Rising approval favors waiting — PMs call elections on the upswing.</p>
        </div>
      </div>
    </section>
  )
}

export function GDPInflationSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">GDP Growth &amp; Inflation</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Annual data — DOSM</p>
        </div>
        <div className="flex-1 min-h-0">
          <ChartContainer config={{ gdp: { label: "GDP %", color: "var(--chart-1)" }, inflation: { label: "Inflation %", color: "var(--chart-2)" } }}>
            <ComposedChart data={ECONOMY_DATA}>
              <CartesianGrid vertical={false} />
              <XAxis dataKey="year" tick={{ fontSize: 11 }} />
              <YAxis tick={{ fontSize: 11 }} />
              <Tooltip />
              <Bar dataKey="gdp" fill="var(--chart-1)" radius={[4, 4, 0, 0]} />
              <Line dataKey="inflation" stroke="var(--chart-2)" strokeWidth={2.5} dot={{ r: 4 }} />
            </ComposedChart>
          </ChartContainer>
          <p className="text-xs text-muted-foreground mt-2">Source: <a href="https://api.data.gov.my" target="_blank" className="underline">DOSM</a></p>
          <p className="text-xs mt-2">GDP grew 5.1% in 2024, projected ~4.5% for 2026. Inflation low at 1.4-2.0% — stable economy, no crisis forcing snap election.</p>
        </div>
      </div>
    </section>
  )
}

export function ParliamentSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Parliament Composition</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">15th Parliament — 222 seats</p>
        </div>
        <div className="flex-1 min-h-0">
          <div className="h-full flex flex-col items-center justify-center">
            <ResponsiveContainer width="100%" height="70%">
              <PieChart>
                <Pie data={SEATS_DATA} dataKey="seats" cx="50%" cy="50%" outerRadius="80%" label={({ name, ...d }) => `${name} ${(d as any).seats}`}>
                  {SEATS_DATA.map((e, i) => <Cell key={i} fill={e.fill} />)}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
            <p className="text-xs text-muted-foreground mt-2">Source: <a href="https://en.wikipedia.org/wiki/Members_of_the_Dewan_Rakyat,_15th_Malaysian_Parliament" target="_blank" className="underline">Wikipedia</a> &middot; <a href="/data/insights/elections/ge15_pendulum.csv" className="underline">CSV</a></p>
            <p className="text-xs text-muted-foreground">Govt bloc: ~151 seats (PH 77 + BN 30 + GPS 23 + GRS 5 + WARISAN 3 + others). Opposition: ~69. Vacant: 2. Source: Wikipedia.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
