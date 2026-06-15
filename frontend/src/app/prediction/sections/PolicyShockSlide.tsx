"use client"

const SHOCKS = [
  { date: "Jun 2024", event: "Diesel subsidy removed", reaction: "Protests from transport/logistics sector. Opposition campaigned on 'broken promise'." },
  { date: "Jul 2025", event: "SST expansion announced", reaction: "Oust Anwar rally (18,000 protesters). Listed as a top grievance." },
  { date: "Jul 2025", event: "RON95 subsidy reduction planned", reaction: "Mass protests forced govt to REVERSE — cut to RM1.99/L instead. Cash handout distributed." },
  { date: "Mar 2026", event: "Hormuz crisis — oil at $120+", reaction: "Subsidy costs ballooned to RM3.2bn/month. Govt scrambled to secure tanker passage." },
  { date: "Apr 2026", event: "N9 MB crisis — 14 BN reps withdraw support", reaction: "PH-BN cooperation collapsed in Negeri Sembilan. Early state election called." },
  { date: "May 2026", event: "Rafizi Ramli & Nik Nazmi quit PKR", reaction: "Major blow to PH reformist brand. Vacated seats triggered by-elections." },
  { date: "Jun 2026", event: "PAS ends cooperation with BERSATU", reaction: "Opposition coalition fractured. PN effectively split but both stay in coalition." },
]

export default function PolicyShockSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Policy Shock Events</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Sudden unpopular reforms vs reversals</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <p className="text-xs text-muted-foreground mb-2">Sources: <a href="https://en.wikipedia.org/wiki/2025_Oust_Anwar_rally" target="_blank" className="underline">Oust Anwar rally</a> &middot; <a href="https://en.wikipedia.org/wiki/Anwar_Ibrahim" target="_blank" className="underline">Anwar page</a> &middot; <a href="https://en.wikipedia.org/wiki/2026_in_Malaysia" target="_blank" className="underline">2026 in Malaysia</a></p>
          <div className="space-y-2 max-w-4xl">
            {SHOCKS.map((s, i) => (
              <div key={i} className="p-3">
                <div className="flex items-start gap-3">
                  <span className="text-xs font-mono text-muted-foreground shrink-0 w-16 pt-0.5">{s.date}</span>
                  <div className="min-w-0">
                    <p className="text-xs font-semibold">{s.event}</p>
                    <p className="text-xs text-muted-foreground mt-0.5">{s.reaction}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
          <div className="mt-3 p-3 border border-red-200 bg-red-50/30 rounded-lg">
            <p className="text-xs font-medium text-red-700">Pattern: The government has consistently reversed unpopular reforms when faced with street pressure. This creates a moral hazard — protesters know they can force policy U-turns. Anwar needs a fresh mandate before this dynamic worsens.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
