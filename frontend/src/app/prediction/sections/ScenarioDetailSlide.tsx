"use client"

const scenarios = [
  {
    id: "A", title: "Full Term (Recommended)", prob: "55%", window: "October-November 2027",
    color: "border-l-green-500 bg-green-50/10",
    supporting: [
      "Anwar publicly stated 'tunggu pilihan raya dua tahun lagi' in Jul 2025 — consistent with full term",
      "Approval recovering from 50% (Nov 2023) to 55% (Jun 2025) — waiting lets it rise further",
      "SW monsoon (May-Sep) is best campaigning weather. No major festivals in Jul-Sep",
      "6 state elections due mid-2027 (Penang, Selangor, NS, Kedah, Kelantan, Terengganu) — GE16 can be synchronized or held after",
      "Redelineation only possible after Mar 2026 — process takes 12-18 months, pushing to 2027",
      "PN in disarray (PAS-BERSATU split Jun 2026) — no electoral imperative to rush",
    ],
    against: [
      "PH-BN pact fraying at state level (N9 MB crisis Apr 2026, Johor BN going solo) — may not survive to 2027",
      "Oil price crash after Iran peace deal reduces Petronas dividends and fiscal space",
      "Rafizi's BERSAMA party could consolidate by 2027 and split PH vote",
    ],
    precedent: [
      "GE11 (2004): New PM sought mandate early, won landslide",
      "GE13 (2013): Najib ran near full term, lost popular vote but won seats",
      "Pattern: Stable PMs with comfortable majorities tend to run close to term",
    ],
  },
  {
    id: "B", title: "Snap 2026 Election", prob: "20%", window: "October-December 2026",
    color: "border-l-amber-500 bg-amber-50/10",
    supporting: [
      "Oil at $120+ due to Iran war — call election before peace deal crashes prices to $60-70",
      "RON95 full subsidy removal still pending — call BEFORE voters feel the pain",
      "Opposition maximally fragmented (PAS-BERSATU split, WAWASAN new, BERSAMA just formed)",
      "Oust Anwar rally (Jul 2025) showed govt vulnerable — seek fresh mandate while still winnable",
    ],
    against: [
      "Redelineation not done — new boundaries could help PH gain seats",
      "PH-BN already competing in Johor (Jul 11) and NS (Aug 1) state polls — risky to generalize to federal",
      "Constitutional term still has ~2 years left — early election looks opportunistic",
    ],
    precedent: [
      "GE10 (1999): Called early amid Reformasi crisis — Mahathir won reduced majority",
      "GE15 (2022): Called ~10 months early due to political crisis — first hung parliament",
      "GE14 (2018): Called slightly early after redelineation — first regime change",
    ],
  },
  {
    id: "C", title: "Synchronized with State Elections", prob: "15%", window: "July-August 2027",
    color: "border-l-blue-500 bg-blue-50/10",
    supporting: [
      "6 state assemblies expire mid-2027 — holding concurrent elections saves costs",
      "Coattail effects — popular federal leader helps state candidates",
      "Lower turnout in concurrent elections favors incumbents with more reliable voter base",
    ],
    against: [
      "Anwar gives up ~6 months of his term by dissolving early",
      "If economy weakens, synchronized losses could cascade across both levels",
      "BN-PH competition in recent state elections suggests fraying alliance",
    ],
    precedent: [
      "GE14 (2018): Held concurrently with state elections in 12 of 13 states — PH sweep",
      "2023 state elections: Held separately from federal — PH+BN lost significant ground to PN",
    ],
  },
  {
    id: "D", title: "Crisis Snap Election", prob: "5%", window: "Before November 2026",
    color: "border-l-red-500 bg-red-50/10",
    supporting: [
      "BN pulls out of unity government at federal level — government loses majority",
      "No-confidence motion against Anwar succeeds in parliament",
      "Major economic shock (oil crash below $50, ringgit crisis to 5.50+)",
    ],
    against: [
      "Govt majority is comfortable (~151 seats) — no imminent collapse risk",
      "No trigger event visible in current data (Jun 2026)",
      "BN benefits from being in government — no incentive to bring it down",
    ],
    precedent: [
      "Sheraton Move (Feb 2020): 11 PKR MPs defected, collapsed PH govt in 48 hours",
      "Muhyiddin lost majority after UMNO withdrew support (Jul 2021) — resigned Aug 2021",
    ],
  },
  {
    id: "E", title: "Late Deadline Scenario", prob: "5%", window: "January-February 2028",
    color: "border-l-purple-500 bg-purple-50/10",
    supporting: [
      "Maximum time in power — economy has longest recovery window",
      "Redelineation fully implemented — new boundaries benefit govt",
      "Opposition fully fragmented by then",
    ],
    against: [
      "NE monsoon peak (Dec-Jan) causes flooding — Baram polling was suspended during GE15",
      "Chinese New Year (Jan-Feb) disrupts campaigning in urban constituencies",
      "Perceived as 'clinging to power' — media narrative would be negative",
      "Feb 17, 2028 is absolute constitutional deadline — no flexibility if anything goes wrong",
    ],
    precedent: [
      "No Malaysian GE has ever been held at the absolute constitutional deadline",
      "GE11 (2004) had shortest campaign at 8 days — tightest timeline",
    ],
  },
]

export default function ScenarioDetailSlide({ params }: { params?: { id?: string } }) {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">GE16 Scenarios — Detailed Analysis</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">All 5 scenarios with supporting evidence, counter-arguments & historical precedent</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto space-y-3">
          {scenarios.map((s, i) => (
            <div key={i} className={`border border-foreground/10 border-l-4 ${s.color} rounded-lg p-3 md:p-4`}>
              <div className="flex items-center justify-between mb-2">
                <h3 className="text-sm font-bold">{s.title}</h3>
                <div className="flex items-center gap-2">
                  <span className="text-xs text-muted-foreground">{s.window}</span>
                  <span className="text-lg font-bold">{s.prob}</span>
                </div>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                <div>
                  <p className="text-green-600 font-semibold mb-1">Supporting Evidence</p>
                  <ul className="space-y-0.5">{s.supporting.map((f, j) => <li key={j} className="flex gap-1 text-muted-foreground"><span className="text-green-500 shrink-0">+</span>{f}</li>)}</ul>
                </div>
                <div>
                  <p className="text-red-600 font-semibold mb-1">Counter-Arguments</p>
                  <ul className="space-y-0.5">{s.against.map((a, j) => <li key={j} className="flex gap-1 text-muted-foreground"><span className="text-red-500 shrink-0">-</span>{a}</li>)}</ul>
                </div>
                <div>
                  <p className="text-blue-600 font-semibold mb-1">Historical Precedent</p>
                  <ul className="space-y-0.5">{s.precedent.map((p, j) => <li key={j} className="flex gap-1 text-muted-foreground"><span className="text-blue-500 shrink-0">&bull;</span>{p}</li>)}</ul>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
