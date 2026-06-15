"use client"

const slides = [
  { n: 2, title: "Elections Over Time", desc: "GE10-GE15 table with major events" },
  { n: 3, title: "Election Timing Trend", desc: "Dissolution-to-polling & turnout" },
  { n: 4, title: "Parliament Composition", desc: "Current seat breakdown" },
  { n: 5, title: "Constitutional Constraints", desc: "Max term, dissolution, PM discretion" },
  { n: 6, title: "PM Approval Trend", desc: "Anwar's approval trajectory" },
  { n: 7, title: "GDP Growth Trend", desc: "Recent vs historical average" },
  { n: 8, title: "Inflation Trends", desc: "CPI headline over time" },
  { n: 9, title: "Cost of Living", desc: "CPI, food, housing composite" },
  { n: 10, title: "Fuel Prices & Subsidy", desc: "RON95/97/diesel & reform impact" },
  { n: 11, title: "Govt Debt & Deficit", desc: "Debt ceiling & consolidation" },
  { n: 12, title: "Fuel Subsidy Burden", desc: "Annual costs & reform progress" },
  { n: 13, title: "Major Policy Announcements", desc: "Subsidy, tax & wage changes" },
  { n: 14, title: "Policy Shock Events", desc: "Unpopular reforms & reversals" },
  { n: 15, title: "Public Sector Salary", desc: "Civil service wage pressure" },
  { n: 16, title: "Cost Relief Measures", desc: "Subsidies, aid & pre-election relief" },
  { n: 17, title: "Coalition Stability", desc: "Govt internal fractures" },
  { n: 18, title: "Leadership Challenge", desc: "Party internal dynamics" },
  { n: 19, title: "Cabinet Reshuffles", desc: "Frequency as instability signal" },
  { n: 20, title: "By-Election Trend", desc: "Recent constituency swings" },
  { n: 21, title: "State Election Alignment", desc: "Peninsular vs East Malaysia" },
  { n: 22, title: "Poll Aggregation", desc: "Combined polling averages" },
  { n: 23, title: "Flood Risk & Elections", desc: "Historical flood data & timing" },
  { n: 24, title: "Parliament Sessions", desc: "Dissolution windows" },
  { n: 25, title: "Unemployment Rate", desc: "Labour market & voter sentiment" },
  { n: 26, title: "OPR & Monetary Policy", desc: "BNM interest rate cycle" },
  { n: 27, title: "KLCI Stock Market", desc: "Index trend & election correlation" },
  { n: 28, title: "Ringgit Exchange Rate", desc: "MYR/USD & import cost impact" },
  { n: 29, title: "Brent Crude Oil", desc: "Price cycle & fiscal exposure" },
  { n: 30, title: "Scenario A: Full Term", desc: "Oct-Nov 2027 (55%) — Recommended" },
  { n: 31, title: "Scenario B: Snap 2026", desc: "Oct-Dec 2026 (20%)" },
  { n: 32, title: "Scenario C: Synchronized", desc: "Jul-Aug 2027 (15%)" },
  { n: 33, title: "Scenario D: Crisis Snap", desc: "Before Nov 2026 (5%)" },
  { n: 34, title: "Scenario E: Late Deadline", desc: "Jan-Feb 2028 (5%)" },
]

export default function TocSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Table of Contents</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">All 34 sections — scroll to navigate or click to jump</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2 md:gap-3">
            {slides.map((s, i) => (
              <a
                key={i}
                href={`#slide-${s.n}`}
                className="flex items-center gap-3 p-2.5 rounded-lg hover:bg-muted/50 transition-colors no-underline text-foreground"
              >
                <span className="flex items-center justify-center w-7 h-7 rounded-full bg-foreground/10 text-xs font-mono font-medium shrink-0">{s.n}</span>
                <div className="min-w-0">
                  <span className="text-sm font-medium block truncate">{s.title}</span>
                  <span className="text-xs text-muted-foreground block truncate">{s.desc}</span>
                </div>
              </a>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
