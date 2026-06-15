"use client"

export default function ScenarioCSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-4">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Scenario C: Synchronized with State Elections</h2>
          <p className="text-base md:text-lg text-muted-foreground mt-1">July-August 2027 &mdash; Probability: 15%</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto grid grid-cols-1 md:grid-cols-2 gap-6 auto-rows-min">
          <div>
            <h3 className="text-sm font-semibold mb-3">Supporting Evidence</h3>
            <ul className="space-y-3">
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>6 state assemblies expire mid-2027 &mdash; concurrent elections save costs and reduce voter fatigue</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>Coattail effects: a popular federal leader helps state candidates down the ballot</li>
              <li className="text-sm leading-relaxed"><span className="text-green-600 font-bold mr-2">+</span>Lower turnout in concurrent elections generally favors incumbent parties</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold mb-3">Counter-Arguments &amp; Risks</h3>
            <ul className="space-y-3">
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>Anwar gives up ~6 months of his term by dissolving early</li>
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>If the economy weakens, synchronized losses could cascade across both federal and state levels</li>
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>BN-PH already competing in recent state elections &mdash; alliance may not hold for synchronized polls</li>
            </ul>
            <h3 className="text-sm font-semibold mt-6 mb-3">Historical Precedent</h3>
            <ul className="space-y-2">
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>GE14 (2018): Held concurrently with 12 of 13 state elections &mdash; PH swept both levels</li>
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>2023 state elections: Held separately from federal &mdash; PH+BN lost significant ground to PN</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  )
}
