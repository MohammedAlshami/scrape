"use client"

export default function ScenarioDSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-4">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Scenario D: Crisis Snap Election</h2>
          <p className="text-base md:text-lg text-muted-foreground mt-1">Before November 2026 &mdash; Probability: 5%</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto grid grid-cols-1 md:grid-cols-2 gap-6 auto-rows-min">
          <div>
            <h3 className="text-sm font-semibold mb-3">Trigger Events That Would Cause This</h3>
            <ul className="space-y-3">
              <li className="text-sm leading-relaxed"><span className="text-amber-600 font-bold mr-2">!</span>BN pulls out of unity government at federal level &mdash; government loses its majority</li>
              <li className="text-sm leading-relaxed"><span className="text-amber-600 font-bold mr-2">!</span>A no-confidence motion against Anwar succeeds in Parliament</li>
              <li className="text-sm leading-relaxed"><span className="text-amber-600 font-bold mr-2">!</span>Major economic shock: oil crash below $50 or ringgit crisis to 5.50+</li>
            </ul>
          </div>
          <div>
            <h3 className="text-sm font-semibold mb-3">Why It Is Unlikely</h3>
            <ul className="space-y-3">
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>Government majority is comfortable at ~151 seats &mdash; no imminent collapse risk</li>
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>No trigger event is visible in current data (June 2026)</li>
              <li className="text-sm leading-relaxed"><span className="text-red-600 font-bold mr-2">&minus;</span>BN benefits from being inside the government &mdash; no incentive to bring it down</li>
            </ul>
            <h3 className="text-sm font-semibold mt-6 mb-3">Historical Parallels</h3>
            <ul className="space-y-2">
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>Sheraton Move (Feb 2020): 11 PKR MPs defected, collapsed PH government in 48 hours</li>
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>Muhyiddin lost majority after UMNO withdrew support (Jul 2021) &mdash; resigned Aug 2021</li>
              <li className="text-sm leading-relaxed"><span className="mr-2">&bull;</span>Current situation: No mass defection dynamic is visible. The government is stable.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  )
}
