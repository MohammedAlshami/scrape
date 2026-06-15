"use client"

const RESHUFFLES = [
  { date: "3 Dec 2022", scope: "Initial cabinet", changes: "28 ministers formed. Anwar holds Finance. DPMs: Zahid (UMNO) & Fadillah (GPS).", signal: "Baseline" },
  { date: "12 Dec 2023", scope: "Major (10 portfolios)", changes: "Defence, Foreign Affairs, Health, Higher Education swapped. Digital ministry created. Fadillah gets Energy Transition.", signal: "1-yr mark refresh" },
  { date: "30 May 2025", scope: "Individual", changes: "Tengku Zafrul switches from BN to PH, keeps MITI portfolio.", signal: "Party realignment" },
  { date: "17 Jun 2025", scope: "Resignation", changes: "Rafizi Ramli resigns as Economy Minister.", signal: "Pre-defection signal" },
  { date: "4 Jul 2025", scope: "Resignation", changes: "Nik Nazmi resigns as Natural Resources Minister.", signal: "Pre-defection signal" },
  { date: "8 Nov 2025", scope: "Resignation", changes: "Ewon Benedick leaves Entrepreneur portfolio.", signal: "UPKO leaving PH" },
  { date: "17 Dec 2025", scope: "Major (re-shuffle)", changes: "Economy, Religious Affairs, FT, MITI, Natural Resources, Youth & Sports, Human Resources all changed. PKR gains more posts.", signal: "Pre-election positioning" },
]

export default function CabinetReshuffleSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Cabinet Reshuffles</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Frequency as instability signal — Anwar government (Dec 2022-Jun 2026)</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://en.wikipedia.org/wiki/Anwar_Ibrahim_cabinet" target="_blank" className="underline">Anwar Ibrahim cabinet (Wikipedia)</a></p>

          <div className="border border-foreground/10 rounded-lg overflow-hidden">
            <table className="w-full text-xs">
              <thead>
                <tr className="border-b bg-muted/30">
                  <th className="py-2 px-3 text-left font-medium">Date</th>
                  <th className="py-2 px-3 text-left font-medium">Scope</th>
                  <th className="py-2 px-3 text-left font-medium">Key Changes</th>
                  <th className="py-2 px-3 text-left font-medium">Signal</th>
                </tr>
              </thead>
              <tbody>
                {RESHUFFLES.map((r, i) => (
                  <tr key={i} className="border-b last:border-0 hover:bg-muted/20">
                    <td className="py-2 px-3 whitespace-nowrap">{r.date}</td>
                    <td className="py-2 px-3 whitespace-nowrap">{r.scope}</td>
                    <td className="py-2 px-3 text-xs leading-relaxed">{r.changes}</td>
                    <td className="py-2 px-3 text-muted-foreground">{r.signal}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="mt-3 grid grid-cols-1 md:grid-cols-3 gap-2">
            <div className="p-3 border border-foreground/10 rounded-lg">
              <p className="text-lg font-bold">7</p>
              <p className="text-xs text-muted-foreground">reshuffle events in 3.5 years</p>
            </div>
            <div className="p-3 border border-foreground/10 rounded-lg">
              <p className="text-lg font-bold">2</p>
              <p className="text-xs text-muted-foreground">major reshuffles (Dec 2023, Dec 2025)</p>
            </div>
            <div className="p-3 border border-foreground/10 rounded-lg">
              <p className="text-lg font-bold">3</p>
              <p className="text-xs text-muted-foreground">ministers resigned/defected (2025)</p>
            </div>
          </div>

          <div className="mt-2 text-xs text-muted-foreground">
            <p><strong>Interpretation:</strong> Two major reshuffles in 3 years is moderate frequency. The cluster of resignations in 2025 (Rafizi, Nik Nazmi, Ewon) signals growing instability. However, Anwar has maintained core control — Finance, Defence, Home, IGP all stayed with trusted hands.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
