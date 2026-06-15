"use client"

const EVENTS = [
  { date: "Jan 2023", party: "UMNO", event: "Zahid wins president uncontested; Khairy & Hishammuddin purged", impact: "Consolidated. Reformist faction eliminated." },
  { date: "May 2025", party: "PKR", event: "Nurul Izzah defeats Rafizi for Deputy President", impact: "Anwar loyalist beats reformist; Rafizi later quits PKR" },
  { date: "May 2025", party: "BN/PH", event: "Tengku Zafrul leaves UMNO for PKR", impact: "BN loses senior minister; PH gains" },
  { date: "May 2026", party: "PKR", event: "Rafizi & Nik Nazmi quit, form BERSAMA", impact: "Biggest defection; PH loses 2 MPs" },
  { date: "Feb 2026", party: "BERSATU", event: "Hamzah faction expelled; forms WAWASAN", impact: "PN loses 6 MPs to new party" },
  { date: "Jun 2026", party: "PAS", event: "PAS ends political cooperation with BERSATU", impact: "PN severely fractured but remains intact" },
  { date: "Jun 2026", party: "PN", event: "Ahmad Samsuri (PAS) replaces Hamzah (BERSATU) as Opposition Leader", impact: "PAS asserts dominance within PN" },
]

export default function LeadershipChallengeSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Leadership Challenge Risk</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Party internal dynamics &amp; succession pressure</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <p className="text-xs text-muted-foreground mb-2">Sources: <a href="https://en.wikipedia.org/wiki/2023_United_Malays_National_Organisation_leadership_election" target="_blank" className="underline">UMNO election 2023</a> &middot; <a href="https://en.wikipedia.org/wiki/People%27s_Justice_Party_(Malaysia)" target="_blank" className="underline">PKR page</a> &middot; <a href="https://en.wikipedia.org/wiki/Next_Malaysian_general_election" target="_blank" className="underline">Next GE page</a></p>

          <div className="border border-foreground/10 rounded-lg overflow-hidden">
            <table className="w-full text-xs">
              <thead>
                <tr className="border-b bg-muted/30">
                  <th className="py-2 px-3 text-left font-medium">Date</th>
                  <th className="py-2 px-3 text-left font-medium">Party</th>
                  <th className="py-2 px-3 text-left font-medium">Event</th>
                  <th className="py-2 px-3 text-left font-medium">Impact</th>
                </tr>
              </thead>
              <tbody>
                {EVENTS.map((e, i) => (
                  <tr key={i} className="border-b last:border-0 hover:bg-muted/20">
                    <td className="py-2 px-3 whitespace-nowrap">{e.date}</td>
                    <td className="py-2 px-3 whitespace-nowrap">{e.party}</td>
                    <td className="py-2 px-3">{e.event}</td>
                    <td className="py-2 px-3 text-muted-foreground">{e.impact}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-3">
            <div className="p-3">
              <h3 className="text-xs font-semibold mb-2">Government Bloc</h3>
              <div className="space-y-2 text-xs">
                <div className="p-2 bg-muted/20 rounded">
                  <p className="font-medium">UMNO: Stable (authoritarian)</p>
                  <p className="text-muted-foreground">Zahid purged all challengers. No-contest motion ensures smooth 2026 election. But reformists (Khairy) applying to return.</p>
                </div>
                <div className="p-2 bg-muted/20 rounded">
                  <p className="font-medium">PKR: Anwar succession question</p>
                  <p className="text-muted-foreground">Nurul Izzah (Anwar's daughter) won deputy presidency, positioning as heir. Rafizi's exit removed main internal challenger.</p>
                </div>
                <div className="p-2 bg-muted/20 rounded">
                  <p className="font-medium">DAP/AMANAH: Stable</p>
                  <p className="text-muted-foreground">No leadership challenges. DAP July 2025 congress to decide fate of leaders in unity govt.</p>
                </div>
              </div>
            </div>
            <div className="p-3">
              <h3 className="text-xs font-semibold mb-2">Opposition Bloc</h3>
              <div className="space-y-2 text-xs">
                <div className="p-2 bg-muted/20 rounded">
                  <p className="font-medium">PAS: Aging leadership</p>
                  <p className="text-muted-foreground">Hadi Awang (78) still president. No visible succession plan. Ahmad Samsuri emerging as de facto leader after becoming Opposition Leader.</p>
                </div>
                <div className="p-2 bg-muted/20 rounded">
                  <p className="font-medium">BERSATU: Imploding</p>
                  <p className="text-muted-foreground">Lost 6 MPs to defection + Hamzah faction expelled. PAS cut ties. Muhyiddin's leadership weakened. New WAWASAN party formed.</p>
                </div>
                <div className="p-2 bg-muted/20 rounded">
                  <p className="font-medium">New parties (BERSAMA, WAWASAN)</p>
                  <p className="text-muted-foreground">Both formed in 2026 by defectors. Too new to assess internal dynamics, but they split the vote further.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
