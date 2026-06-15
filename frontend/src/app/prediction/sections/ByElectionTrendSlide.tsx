"use client"

import { LineChart, BarChart, Bar, Line, XAxis, YAxis, CartesianGrid, Tooltip } from "recharts"
import { ChartContainer } from "./shared"

const BY_EL_DATA = [
  { date: "Aug 2023", seat: "K. Terengganu", govt: 23.6, pn: 76.4, type: "Federal" },
  { date: "Sep 2023", seat: "Pulai", govt: 61.6, pn: 37.8, type: "Federal" },
  { date: "Sep 2023", seat: "Simpang Jeram", govt: 56.5, pn: 42.2, type: "State" },
  { date: "Oct 2023", seat: "Pelangai", govt: 62.4, pn: 37.3, type: "State" },
  { date: "Dec 2023", seat: "Kemaman", govt: 29.9, pn: 70.1, type: "Federal" },
  { date: "May 2024", seat: "KKB", govt: 57.2, pn: 41.4, type: "State" },
  { date: "Jul 2024", seat: "Sg. Bakap", govt: 41.4, pn: 58.6, type: "State" },
  { date: "Aug 2024", seat: "Nenggiri", govt: 61.4, pn: 38.7, type: "State" },
  { date: "Apr 2025", seat: "Ayer Kuning", govt: 60.7, pn: 33.2, type: "State" },
]

export default function ByElectionTrendSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">By-Election Results Trend</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Govt vs Opposition vote share in recent by-elections</p>
        </div>
        <div className="flex-1 min-h-0">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://en.wikipedia.org/wiki/List_of_parliamentary_by-elections_in_Malaysia" target="_blank" className="underline">Wikipedia (by-elections)</a> &middot; <a href="/data/insights/elections/by_elections_2023_2026.csv" className="underline">Download CSV</a></p>
          <ChartContainer config={{ govt: { label: "Govt %", color: "var(--chart-1)" }, pn: { label: "PN %", color: "var(--chart-2)" } }}>
            <BarChart data={BY_EL_DATA} margin={{ top: 10, right: 20, left: 0, bottom: 30 }}>
              <CartesianGrid vertical={false} />
              <XAxis dataKey="seat" tick={{ fontSize: 9 }} interval={0} angle={-35} textAnchor="end" height={50} />
              <YAxis domain={[0, 80]} tick={{ fontSize: 9 }} />
              <Tooltip />
              <Bar dataKey="govt" fill="var(--chart-1)" radius={[2, 2, 0, 0]} />
              <Bar dataKey="pn" fill="var(--chart-2)" radius={[2, 2, 0, 0]} />
            </BarChart>
          </ChartContainer>
          <div className="mt-2 grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
            <div className="p-2 bg-green-50 rounded"><strong>Nenggiri</strong> (Aug 24): BN flipped Kelantan seat (BN 61.4%, +14.6pp)</div>
            <div className="p-2 bg-red-50 rounded"><strong>Sg. Bakap</strong> (Jul 24): PN held Penang (PN 58.6%, +5.9pp)</div>
            <div className="p-2 bg-green-50 rounded"><strong>Ayer Kuning</strong> (Apr 25): BN held Perak (BN 60.7%, +22pp)</div>
            <div className="p-2 bg-amber-50 rounded"><strong>Trend</strong>: Govt won 6/9 by-elections since 2023</div>
          </div>
        </div>
      </div>
    </section>
  )
}
