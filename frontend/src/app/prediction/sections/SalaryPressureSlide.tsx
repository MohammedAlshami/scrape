"use client"

import { useCsv } from "./useData"

type MinWageRow = { year: string; min_wage_rm: string }

export default function SalaryPressureSlide() {
  const data = useCsv<MinWageRow>("/data/insights/economy/minimum_wage.csv")

  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Public Sector Salary Pressure</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Civil service wage expectations vs fiscal reality</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://tradingeconomics.com/malaysia/minimum-wages" target="_blank" className="underline">Trading Economics</a> &middot; <a href="https://en.wikipedia.org/wiki/Economy_of_Malaysia" target="_blank" className="underline">Economy of Malaysia</a> &middot; <a href="/data/insights/economy/minimum_wage.csv" className="underline">Download CSV</a></p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3 h-3/5">
            <div className="p-3 flex flex-col">
              <h3 className="text-xs font-semibold mb-2 shrink-0">Minimum Wage History (RM/month)</h3>
              <div className="flex-1 min-h-0 overflow-y-auto">
                {data.length > 0 ? (
                  <div className="space-y-0.5 text-xs">
                    {data.slice().reverse().map((r, i) => (
                      <div key={i} className="flex justify-between items-center py-1 border-b border-foreground/5 last:border-0">
                        <span className="text-muted-foreground">{r.year}</span>
                        <span className="font-medium">RM{r.min_wage_rm}</span>
                      </div>
                    ))}
                  </div>
                ) : (
                  <div className="text-xs text-muted-foreground">Loading...</div>
                )}
              </div>
              <p className="text-xs text-muted-foreground mt-2">Min wage rose from RM900 (2013) to RM1,700 (2025). An 89% increase over 12 years.</p>
            </div>

            <div className="p-3 flex flex-col">
              <h3 className="text-xs font-semibold mb-2 shrink-0">Civil Service Context</h3>
              <div className="flex-1 space-y-2 text-xs">
                <div className="p-2 bg-muted/30 rounded">
                  <p className="font-medium">1.6 million</p>
                  <p className="text-muted-foreground">public sector employees</p>
                </div>
                <div className="p-2 bg-muted/30 rounded">
                  <p className="font-medium">~30%</p>
                  <p className="text-muted-foreground">of operating budget goes to emoluments</p>
                </div>
                <div className="p-2 bg-muted/30 rounded">
                  <p className="font-medium">Forecast: RM1,900</p>
                  <p className="text-muted-foreground">expected min wage by end of 2026 (Trading Economics)</p>
                </div>
                <p className="text-muted-foreground leading-relaxed">Civil servants are a key voting bloc (~15% of registered voters are govt employees or dependents). Anwar announced a salary review in 2025 but has not implemented it fully yet.</p>
              </div>
            </div>
          </div>

          <div className="mt-3 text-xs text-muted-foreground">
            <p><strong>Election implication:</strong> Civil service salary increases are popular but costly. Every RM100 increase in minimum wage costs the govt ~RM500m. With debt at 70% of GDP, fiscal space is limited. The govt may announce pre-election bonuses as a vote-winning move.</p>
          </div>
        </div>
      </div>
    </section>
  )
}
