"use client"

import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ReferenceLine } from "recharts"
import { ChartContainer } from "./shared"

const POLICY_EVENTS = [
  { date: "Jun 2024", event: "Diesel subsidy removed (Peninsular)", type: "reform", impact: "Saved RM4bn/yr" },
  { date: "Jul 2025", event: "Oust Anwar rally — 18,000 protest", type: "protest", impact: "Govt reversed RON95 cut" },
  { date: "Jul 2025", event: "SST expanded (new tax brackets)", type: "reform", impact: "Broadened tax base" },
  { date: "Sep 2025", event: "RON95 capped 300L/month (Budi95)", type: "reform", impact: "Saved ~RM4.2bn/yr" },
  { date: "Sep 2025", event: "RM100 cash handout to all adults", type: "relief", impact: "Cost RM2.2bn" },
  { date: "Oct 2025", event: "Toll price freeze announced", type: "relief", impact: "Pre-election gesture" },
  { date: "Mar 2026", event: "Hormuz crisis — fuel costs spike", type: "shock", impact: "RM3.2bn/month subsidy" },
]

export default function MajorPolicySlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Major Policy Announcements</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Subsidy reforms, tax changes &amp; wage policies</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto space-y-3">
          <p className="text-xs text-muted-foreground">Source: <a href="https://en.wikipedia.org/wiki/Anwar_Ibrahim" target="_blank" className="underline">Anwar Ibrahim page</a> &middot; <a href="https://en.wikipedia.org/wiki/Economy_of_Malaysia" target="_blank" className="underline">Economy of Malaysia</a></p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div className="p-3">
              <h3 className="text-sm font-semibold mb-2">RON95 Subsidy Reform (Sep 2025)</h3>
              <ul className="space-y-1 text-xs">
                <li><strong>Budi95 program:</strong> RON95 capped at RM1.99/L for 300L/month (top 15% excluded).</li>
                <li><strong>Original plan:</strong> Remove subsidy for top 15% earners (saved RM8bn) — <span className="text-red-600">SHELVED</span> after public backlash.</li>
                <li><strong>Actual saving:</strong> ~RM4.2bn/yr (half of original target).</li>
                <li><strong>Reference:</strong> <a href="https://en.wikipedia.org/wiki/Anwar_Ibrahim" target="_blank" className="underline text-blue-500">Anwar page</a>, Reuters Sep 2025</li>
              </ul>
            </div>

            <div className="p-3">
              <h3 className="text-sm font-semibold mb-2">Diesel Subsidy Removal (Jun 2024)</h3>
              <ul className="space-y-1 text-xs">
                <li><strong>Reform:</strong> Diesel subsidy removed in Peninsular Malaysia. Sabah/Sarawak exempted.</li>
                <li><strong>Saving:</strong> RM4bn annually.</li>
                <li><strong>Impact:</strong> Diesel went from RM2.15 to market price (~RM3.35). Subsidized rate kept for fishermen, public transport.</li>
                <li><strong>Reference:</strong> <a href="https://en.wikipedia.org/wiki/Anwar_Ibrahim" target="_blank" className="underline text-blue-500">Anwar page</a>, AP News Jun 2024</li>
              </ul>
            </div>

            <div className="p-3">
              <h3 className="text-sm font-semibold mb-2">SST Expansion (Jul 2025)</h3>
              <ul className="space-y-1 text-xs">
                <li><strong>Reform:</strong> Sales &amp; Services Tax broadened — new categories taxed.</li>
                <li><strong>Rationale:</strong> Broaden revenue base without introducing GST (politically toxic after 2018).</li>
                <li><strong>Impact:</strong> Listed as a grievance in the Oust Anwar rally (Jul 2025).</li>
                <li><strong>Reference:</strong> <a href="https://en.wikipedia.org/wiki/2025_Oust_Anwar_rally" target="_blank" className="underline text-blue-500">Oust Anwar rally page</a></li>
              </ul>
            </div>

            <div className="p-3">
              <h3 className="text-sm font-semibold mb-2">Wage &amp; Civil Service Policies</h3>
              <ul className="space-y-1 text-xs">
                <li><strong>Minimum wage:</strong> Raised to RM1,500 (effective 2023). Next revision expected before GE16.</li>
                <li><strong>Civil service:</strong> Anwar announced salary review for 1.6M public sector workers (2025).</li>
                <li><strong>Post-maternity allowance:</strong> New benefit for working mothers (announced 2026).</li>
                <li><strong>Reference:</strong> News articles, DayakDaily Jun 2026</li>
              </ul>
            </div>
          </div>

          <div className="p-3">
            <h3 className="text-sm font-semibold mb-2">Policy Announcement Timeline</h3>
            <div className="space-y-2">
              {POLICY_EVENTS.filter(e => e.type === "reform" || e.type === "relief").map((e, i) => (
                <div key={i} className="flex items-start gap-2 text-xs">
                  <span className="text-muted-foreground font-mono shrink-0 w-16">{e.date}</span>
                  <span className="font-medium">{e.event}</span>
                  <span className="text-muted-foreground shrink-0">— {e.impact}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
