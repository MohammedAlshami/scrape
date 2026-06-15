"use client"

import { cn } from "@/lib/utils"

const SESSIONS = [
  { meeting: "2022 Special", dates: "19-20 Dec 2022" },
  { meeting: "2023 1st", dates: "13 Feb - 4 Apr 2023" },
  { meeting: "2023 2nd", dates: "22 May - 15 Jun 2023" },
  { meeting: "2023 Special", dates: "11-19 Sep 2023" },
  { meeting: "2023 3rd (Budget)", dates: "9 Oct - 30 Nov 2023" },
  { meeting: "2024 1st", dates: "26 Feb - 27 Mar 2024" },
  { meeting: "2024 2nd", dates: "24 Jun - 18 Jul 2024" },
  { meeting: "2024 3rd (Budget)", dates: "14 Oct - 12 Dec 2024" },
  { meeting: "2025 1st", dates: "3 Feb - 6 Mar 2025" },
  { meeting: "2025 Special", dates: "5 May 2025" },
  { meeting: "2025 2nd", dates: "21 Jul - 28 Aug 2025" },
  { meeting: "2025 3rd (Budget)", dates: "6 Oct - 4 Dec 2025" },
  { meeting: "2026 1st", dates: "19 Jan - 3 Mar 2026" },
  { meeting: "2026 2nd", dates: "22 Jun - 16 Jul 2026" },
  { meeting: "2026 3rd (Budget)", dates: "5 Oct - 8 Dec 2026" },
]

export default function ParliamentSessionsSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Parliament Sessions & Dissolution Windows</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">15th Parliament sitting calendar (2022-2026)</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://en.wikipedia.org/wiki/Members_of_the_Dewan_Rakyat,_15th_Malaysian_Parliament" target="_blank" className="underline">Wikipedia</a></p>
          <div className="border border-foreground/10 rounded-lg overflow-hidden mb-3">
            <table className="w-full text-xs">
              <thead><tr className="border-b bg-muted/30">
                <th className="py-1.5 px-3 text-left">Meeting</th><th className="py-1.5 px-3 text-left">Dates</th><th className="py-1.5 px-3 text-left">Can Dissolve?</th>
              </tr></thead>
              <tbody>{SESSIONS.map((s, i) => {
                const canDissolve = s.meeting.includes("Budget") ? "Avoid (Budget)" : s.dates.includes("Jun") || s.dates.includes("Jul") ? "Yes" : "Yes"
                return (
                <tr key={i} className="border-b last:border-0 hover:bg-muted/20">
                  <td className="py-1.5 px-3">{s.meeting}</td>
                  <td className="py-1.5 px-3">{s.dates}</td>
                  <td className={cn("py-1.5 px-3 text-xs", canDissolve === "Avoid (Budget)" ? "text-red-600" : "text-green-600")}>{canDissolve}</td>
                </tr>
              )})}</tbody>
            </table>
          </div>
          <div className="text-xs text-muted-foreground space-y-1">
            <p><strong>Key insight:</strong> PM can dissolve at any time, but traditionally avoids during Budget session (Oct-Dec). The 2026 2nd sitting (22 Jun - 16 Jul) and 2027 sittings are the most likely dissolution windows. Budget 2027 (Oct-Dec 2027) would be the last opportunity before the Feb 2028 deadline.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
