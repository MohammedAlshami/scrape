"use client"

export default function ScenarioESlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-4">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Scenario E: Late Deadline</h2>
          <p className="text-base md:text-lg text-muted-foreground mt-1">January-February 2028 &mdash; Probability: 5%</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto grid grid-cols-1 md:grid-cols-2 gap-6 auto-rows-min">
          <div>
            <h3 className="text-sm font-semibold mb-3">Supporting Factors</h3>
            <ul className="space-y-3">
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>Maximum time in power &mdash; the economy has the longest possible recovery window</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>Redelineation fully implemented &mdash; new constituency boundaries benefit the government</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>The opposition is expected to be fully fragmented by then</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold mb-3">Why It Is Unlikely</h3>
            <ul className="space-y-3">
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>Northeast monsoon peaks (Dec-Jan) cause severe flooding &mdash; Baram polling was suspended during GE15</li>
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>Chinese New Year (Jan-Feb) disrupts campaigning especially in urban constituencies</li>
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>The constitutional deadline (17 Feb 2028) is absolute &mdash; there is zero margin for any error</li>
            </ul>
            <h3 className="text-sm font-semibold mt-6 mb-3">Historical Context</h3>
            <ul className="space-y-2">
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>No Malaysian general election has ever been held at the absolute constitutional deadline</li>
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>GE11 (2004): Shortest campaign ever at 8 days &mdash; tight timelines are possible but risky</li>
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>GE15 (Nov 2022): Held during NE monsoon &mdash; Baram polling stations were flooded and delayed</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  )
}
