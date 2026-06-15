"use client"

import { cn } from "@/lib/utils"

const EVENTS = [
  { date: "Dec 2022", event: "Unity govt formed: PH+BN+GPS+GRS", impact: "~148 seats, stable majority" },
  { date: "Jan 2023", event: "UMNO no-contest motion passed", impact: "Zahid secured as president, critics purged" },
  { date: "Dec 2023", event: "First major cabinet reshuffle", impact: "Digital ministry created, Health swapped" },
  { date: "Jun 2024", event: "6 BERSATU MPs defect to support govt", impact: "Govt majority strengthened to ~153" },
  { date: "May 2025", event: "Tengku Zafrul leaves UMNO for PKR", impact: "BN weakened, PH strengthened" },
  { date: "Sep 2025", event: "RON95 reform shelved after protest", impact: "Govt showed vulnerability to street pressure" },
  { date: "Dec 2025", event: "Second major reshuffle", impact: "PKR gains more portfolios" },
  { date: "Apr 2026", event: "14 BN reps withdraw support in N9", impact: "PH-BN cooperation fraying at state level" },
  { date: "May 2026", event: "Rafizi & Nik Nazmi quit PKR", impact: "PH loses reformist wing; new BERSAMA party" },
  { date: "Jun 2026", event: "PAS ends cooperation with BERSATU", impact: "PN coalition fractured but both stay in" },
]

export default function CoalitionStabilitySlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Coalition Stability Index</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Internal fractures within the unity government</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <p className="text-xs text-muted-foreground mb-2">Sources: <a href="https://en.wikipedia.org/wiki/Anwar_Ibrahim_cabinet" target="_blank" className="underline">Cabinet page</a> &middot; <a href="https://en.wikipedia.org/wiki/2023_United_Malays_National_Organisation_leadership_election" target="_blank" className="underline">UMNO election</a></p>

          <div className="border border-foreground/10 rounded-lg overflow-hidden">
            <table className="w-full text-xs">
              <thead>
                <tr className="border-b bg-muted/30">
                  <th className="py-2 px-3 text-left font-medium">Date</th>
                  <th className="py-2 px-3 text-left font-medium">Event</th>
                  <th className="py-2 px-3 text-left font-medium">Impact on Stability</th>
                </tr>
              </thead>
              <tbody>
                {EVENTS.map((e, i) => (
                  <tr key={i} className={cn("border-b last:border-0 hover:bg-muted/20", 
                    e.impact.includes("fractured") || e.impact.includes("weakened") || e.impact.includes("fraying") ? "bg-red-50/20" : 
                    e.impact.includes("strengthened") ? "bg-green-50/20" : ""
                  )}>
                    <td className="py-2 px-3 whitespace-nowrap font-medium">{e.date}</td>
                    <td className="py-2 px-3">{e.event}</td>
                    <td className="py-2 px-3 text-muted-foreground">{e.impact}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="mt-3 grid grid-cols-1 md:grid-cols-3 gap-2">
            <div className="border border-green-200 bg-green-50/30 rounded-lg p-3">
              <p className="text-xs font-bold text-green-700">Strengthening Factors</p>
              <ul className="text-xs text-green-600 mt-1 space-y-0.5">
                <li>+ Comfortable ~151 seat majority</li>
                <li>+ BERSATU defectors bolstered govt</li>
                <li>+ BN still formally in coalition</li>
                <li>+ GPS/GRS reliable partners</li>
              </ul>
            </div>
            <div className="border border-amber-200 bg-amber-50/30 rounded-lg p-3">
              <p className="text-xs font-bold text-amber-700">Warning Signs</p>
              <ul className="text-xs text-amber-600 mt-1 space-y-0.5">
                <li>- BN state chapters rebelling (N9, Johor)</li>
                <li>- Rafizi defection created BERSAMA</li>
                <li>- Tengku Zafrul switch weakens BN</li>
                <li>- PH-BN competing in state polls</li>
              </ul>
            </div>
            <div className="border border-blue-200 bg-blue-50/30 rounded-lg p-3">
              <p className="text-xs font-bold text-blue-700">GE16 Scenario</p>
              <p className="text-xs text-blue-600 mt-1">If PH-BN contest against each other nationally, opposition wins. A pre-election electoral pact is critical for govt survival.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
