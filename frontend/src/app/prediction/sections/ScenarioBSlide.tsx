"use client"

export default function ScenarioBSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-4">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Scenario B: Snap 2026 Election</h2>
          <p className="text-base md:text-lg text-muted-foreground mt-1">October-December 2026 &mdash; Probability: 20%</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto grid grid-cols-1 md:grid-cols-2 gap-6 auto-rows-min">
          <div>
            <h3 className="text-sm font-semibold mb-3">Supporting Evidence</h3>
            <ul className="space-y-3">
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>Oil at $120+ due to Iran war &mdash; call election before peace deal crashes prices to $60-70</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>RON95 full subsidy removal still pending &mdash; call BEFORE voters feel the pain</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>Opposition maximally fragmented (PAS-BERSATU split, WAWASAN new, BERSAMA just formed)</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>Oust Anwar rally (Jul 2025) showed govt vulnerable &mdash; seek fresh mandate while still winnable</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold mb-3">Counter-Arguments &amp; Risks</h3>
            <ul className="space-y-3">
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>Redelineation not done &mdash; new boundaries could help PH gain seats</li>
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>PH-BN already competing in Johor/NS state polls &mdash; risky to generalize to federal level</li>
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>Constitutional term still has ~2 years left &mdash; early election looks opportunistic</li>
            </ul>
            <h3 className="text-sm font-semibold mt-6 mb-3">Historical Precedent</h3>
            <ul className="space-y-2">
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>GE10 (1999): Called early amid Reformasi &mdash; Mahathir won reduced majority</li>
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>GE15 (2022): Called ~10mo early due to political crisis &mdash; first hung parliament</li>
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>GE14 (2018): Called early after redelineation &mdash; first regime change in history</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  )
}
