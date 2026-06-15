"use client"

const GE10_15 = [
  { ge: "GE10", y: 1999, act: "29 Nov 1999", diss: "~10 Nov", pm: "Mahathir", to: 71.2, event: "Asian Financial Crisis + Anwar sacked", why: "Snap election to regain legitimacy amid Reformasi" },
  { ge: "GE11", y: 2004, act: "21 Mar 2004", diss: "2 Mar", pm: "Abdullah", to: 73.0, event: "Mahathir retired after 22 yrs", why: "New PM sought mandate; won record 198/219" },
  { ge: "GE12", y: 2008, act: "8 Mar 2008", diss: "13 Feb", pm: "Abdullah", to: 75.4, event: "Anwar eligible to return", why: "Called early; BN lost 2/3 majority" },
  { ge: "GE13", y: 2013, act: "5 May 2013", diss: "3 Apr", pm: "Najib", to: 84.6, event: "Opposition wave (PR)", why: "Near full term; BN lost popular vote" },
  { ge: "GE14", y: 2018, act: "9 May 2018", diss: "7 Apr", pm: "Najib", to: 82.3, event: "1MDB scandal", why: "After redelineation; first regime change" },
  { ge: "GE15", y: 2022, act: "19 Nov 2022", diss: "10 Oct", pm: "Ismail Sabri", to: 74.1, event: "Sheraton Move; 3 PMs in 4 yrs", why: "Political crisis; first hung parliament" },
]

export default function HistoryTableSlide() {
  return (
    <section id="history" className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Elections Over Time</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">When they were supposed to happen vs when they actually did</p>
        </div>
        <div className="flex-1 min-h-0 flex flex-col">
          <p className="text-xs md:text-sm text-muted-foreground mb-4 shrink-0">Source: <a href="https://en.wikipedia.org/wiki/Elections_in_Malaysia" target="_blank" className="underline">Wikipedia</a> &middot; <a href="/data/insights/elections/ge_turnout.csv" className="underline">Download CSV</a></p>
          <div className="flex-1 min-h-0 overflow-auto flex items-start">
            <table className="w-full text-sm md:text-base">
              <thead className="sticky top-0 bg-background">
                <tr className="border-b-2 text-left">
                  <th className="py-4 pr-6 font-semibold text-sm">GE</th>
                  <th className="py-4 pr-6 font-semibold text-sm">Year</th>
                  <th className="py-4 pr-6 font-semibold text-sm">Dissolved</th>
                  <th className="py-4 pr-6 font-semibold text-sm">Polling</th>
                  <th className="py-4 pr-6 font-semibold text-sm">PM</th>
                  <th className="py-4 pr-6 font-semibold text-sm">Turnout</th>
                  <th className="py-4 pr-6 font-semibold text-sm">Major Event</th>
                  <th className="py-4 pr-6 font-semibold text-sm">Why Called</th>
                </tr>
              </thead>
              <tbody>
                {GE10_15.map((r, i) => (
                  <tr key={i} className="border-b hover:bg-muted/20">
                    <td className="py-7 pr-6 font-bold whitespace-nowrap text-base">{r.ge}</td>
                    <td className="py-7 pr-6 whitespace-nowrap text-base">{r.y}</td>
                    <td className="py-7 pr-6 whitespace-nowrap text-base">{r.diss}</td>
                    <td className="py-7 pr-6 whitespace-nowrap text-base">{r.act}</td>
                    <td className="py-7 pr-6 whitespace-nowrap text-base">{r.pm}</td>
                    <td className="py-7 pr-6 whitespace-nowrap font-semibold text-base">{r.to}%</td>
                    <td className="py-7 pr-6 text-base max-w-[220px]">{r.event}</td>
                    <td className="py-7 pr-6 text-base max-w-[280px] leading-relaxed">{r.why}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
  )
}
