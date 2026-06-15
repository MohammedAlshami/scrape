"use client"

export default function ScenarioASlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-4">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Scenario A: Full Term</h2>
          <p className="text-base md:text-lg text-muted-foreground mt-1">October-November 2027 &mdash; Probability: 55% <span className="text-green-600 font-medium">(Recommended)</span></p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto grid grid-cols-1 md:grid-cols-2 gap-6 auto-rows-min">
          <div>
            <h3 className="text-sm font-semibold mb-3">Supporting Evidence</h3>
            <ul className="space-y-3">
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>Anwar publicly said &ldquo;tunggu pilihan raya dua tahun lagi&rdquo; (Jul 2025) &mdash; consistent with full term</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>Approval recovering 50%&rarr;55% &mdash; waiting lets it rise further</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>SW monsoon (May-Sep) is best campaigning weather, no major festivals</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>State elections due mid-2027 &mdash; can synchronize or hold GE16 after</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>Redelineation only possible after Mar 2026, takes 12-18 months</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>PN in disarray (PAS-BERSATU split) &mdash; no need to rush</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold mb-3">Counter-Arguments &amp; Risks</h3>
            <ul className="space-y-3">
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>PH-BN pact fraying at state level (N9 crisis, Johor going solo) &mdash; may not survive to 2027</li>
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>Oil price crash after Iran peace deal reduces Petronas dividends</li>
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>Rafizi&rsquo;s BERSAMA could consolidate by 2027 and split PH vote</li>
            </ul>
            <h3 className="text-sm font-semibold mt-6 mb-3">Historical Precedent</h3>
            <ul className="space-y-2">
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>GE11 (2004): New PM sought mandate early, won landslide</li>
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>GE13 (2013): Najib ran near full term, won seats despite losing popular vote</li>
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>Pattern: Stable PMs with comfortable majorities run close to term</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  )
}
