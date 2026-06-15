"use client"

const SCENARIOS = [
  {
    id: "A", title: "Full Term (Recommended)", prob: "55%", window: "Oct-Nov 2027",
    color: "border-l-green-500",
    for: [
      "Anwar wants full term — said 'tunggu 2 tahun lagi' in Jul 2025",
      "Approval recovering (50%→55%) — waiting lets it rise further",
      "State elections first (Malacca Feb 27, Sarawak Apr 27, Johor Jun 27)",
      "Redelineation needs to complete (eligible after Mar 2026)",
      "PN in disarray (PAS-BERSATU split) — no need to rush",
    ],
    against: [
      "PH-BN pact may not survive to 2027 (N9, Johor already fraying)",
      "Oil price crash after peace deal reduces fiscal space",
    ],
    evidence: ["Prior pattern: PMs run close to term when stable (GE11, GE13)", "Parliament sessions scheduled through Dec 2026", "Budget 2027 in Oct-Dec 2027 would be final opportunity"],
  },
  {
    id: "B", title: "Snap 2026", prob: "20%", window: "Oct-Dec 2026",
    color: "border-l-amber-500",
    for: [
      "Oil revenue at $120+ — call before peace deal crashes prices",
      "RON95 subsidy removal pending — call BEFORE voters feel pain",
      "Opposition maximally fragmented (PAS-BERSATU split, WAWASAN new)",
      "Oust Anwar rally showed vulnerability — seek fresh mandate while govt can still win",
    ],
    against: [
      "Redelineation not done — new boundaries could help PH",
      "PH-BN already competing in Johor/NS state polls — risky to generalize",
      "Anwar has stated preference for full term",
    ],
    evidence: ["GE15 called 10 months early due to political crisis", "GE10 called early amid Reformasi crisis", "GE14 called slightly early after redelineation"],
  },
  {
    id: "C", title: "Synchronized with States", prob: "15%", window: "Jul-Aug 2027",
    color: "border-l-blue-500",
    for: [
      "Hold GE16 concurrently with 6 state elections due mid-2027",
      "Cost savings, coattail effects favor incumbents",
      "Lower turnout helps government (rural voters more reliable)",
    ],
    against: [
      "Anwar gives up ~6 months of term",
      "If economy weakens, synchronized losses could collapse govt",
    ],
    evidence: ["GE14 (2018) was held concurrently with state elections in 12 states", "2023 state elections were held separately from federal — mixed results"],
  },
  {
    id: "D", title: "Crisis Snap", prob: "5%", window: "Before Nov 2026",
    color: "border-l-red-500",
    for: [
      "BN pulls out of unity government at federal level",
      "No-confidence motion against Anwar succeeds",
      "Major economic shock (oil crash, ringgit crisis)",
    ],
    against: [
      "Govt majority is comfortable (~151 seats)",
      "No trigger event visible in current data",
    ],
    evidence: ["Sheraton Move (2020) collapsed PH govt", "Muhyiddin lost majority after UMNO withdrew support (Jul 2021)", "No similar dynamic currently — BN still in govt"],
  },
  {
    id: "E", title: "Late Deadline", prob: "5%", window: "Jan-Feb 2028",
    color: "border-l-purple-500",
    for: [
      "Maximum time in power — economy fully recovers",
      "Redelineation fully implemented",
    ],
    against: [
      "Monsoon flooding (NE monsoon peak Dec-Jan)",
      "Chinese New Year (Jan-Feb) disrupts campaigning",
      "Perceived as 'clinging to power'",
    ],
    evidence: ["No Malaysian GE has ever been held at the absolute deadline", "Latest was GE11 (Mar 2004), 8 days campaign — shortest ever"],
  },
]

export function ScenarioOverviewSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">GE16 Scenarios Overview</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">5 possible outcomes with evidence-weighted probabilities</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <div className="space-y-2">
            {SCENARIOS.map((s, i) => (
              <div key={i} className={`border border-foreground/10 border-l-4 ${s.color} rounded-lg p-3`}>
                <div className="flex items-center justify-between mb-1">
                  <h3 className="text-sm font-semibold">{s.title}</h3>
                  <div className="flex items-center gap-3">
                    <span className="text-xs text-muted-foreground">{s.window}</span>
                    <span className="text-lg font-bold">{s.prob}</span>
                  </div>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
                  <div>
                    <p className="text-green-600 font-medium mb-0.5">Supporting:</p>
                    <ul className="space-y-0.5 text-muted-foreground">{s.for.map((f, j) => <li key={j} className="flex gap-1"><span className="text-green-500">+</span>{f}</li>)}</ul>
                  </div>
                  <div>
                    <p className="text-red-600 font-medium mb-0.5">Against:</p>
                    <ul className="space-y-0.5 text-muted-foreground">{s.against.map((a, j) => <li key={j} className="flex gap-1"><span className="text-red-500">-</span>{a}</li>)}</ul>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}

export function ScenarioDetailSlide({ scenario }: { scenario: typeof SCENARIOS[0] }) {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Scenario {scenario.id}: {scenario.title}</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">{scenario.window} — Probability: {scenario.prob}</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 h-full">
            <div className="border border-green-200 bg-green-50/30 rounded-lg p-4">
              <h3 className="text-sm font-semibold text-green-700 mb-3">Evidence FOR</h3>
              <ul className="space-y-2">
                {scenario.for.map((f, i) => (
                  <li key={i} className="text-xs flex gap-2"><span className="text-green-600 font-bold shrink-0">+</span>{f}</li>
                ))}
              </ul>
            </div>
            <div className="border border-red-200 bg-red-50/30 rounded-lg p-4">
              <h3 className="text-sm font-semibold text-red-700 mb-3">Evidence AGAINST</h3>
              <ul className="space-y-2">
                {scenario.against.map((a, i) => (
                  <li key={i} className="text-xs flex gap-2"><span className="text-red-600 font-bold shrink-0">-</span>{a}</li>
                ))}
              </ul>
              <h3 className="text-sm font-semibold mt-4 mb-2">Historical Precedent</h3>
              <ul className="space-y-1">
                {scenario.evidence.map((e, i) => (
                  <li key={i} className="text-xs text-muted-foreground flex gap-2"><span className="text-muted-foreground">&bull;</span>{e}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
