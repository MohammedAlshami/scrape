"use client"

const RELIEF = [
  { date: "Jul 2025", measure: "RON95 cut to RM1.99/L", cost: "~RM2bn/yr foregone", trigger: "Oust Anwar rally" },
  { date: "Jul 2025", measure: "RM100 cash to every adult", cost: "RM2.2bn one-off", trigger: "Oust Anwar rally" },
  { date: "Jul 2025", measure: "Toll price freeze", cost: "~RM500m/yr", trigger: "Oust Anwar rally" },
  { date: "Sep 2025", measure: "Budi95 fuel subsidy (capped)", cost: "RM4.2bn/yr saved", trigger: "Fiscal consolidation" },
  { date: "Oct 2025", measure: "RM15bn cash handouts package", cost: "RM15bn", trigger: "Budget 2026 pre-election" },
  { date: "Mar 2026", measure: "Diesel price freeze in Sabah/Sarawak", cost: "RM1.4bn/yr", trigger: "Hormuz crisis protection" },
  { date: "May 2026", measure: "Post-maternity allowance", cost: "~RM200m/yr", trigger: "Policy initiative" },
]

export default function CostReliefSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Cost Relief Measures</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Timing of subsidies, cash aid packages &amp; pre-election relief</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <p className="text-xs text-muted-foreground mb-2">Sources: <a href="https://en.wikipedia.org/wiki/2025_Oust_Anwar_rally" target="_blank" className="underline">Oust Anwar rally</a> &middot; <a href="https://en.wikipedia.org/wiki/Anwar_Ibrahim" target="_blank" className="underline">Anwar page</a> &middot; News reports</p>

          <div className="border border-foreground/10 rounded-lg overflow-hidden">
            <table className="w-full text-xs">
              <thead>
                <tr className="border-b bg-muted/30">
                  <th className="py-2 px-3 text-left font-medium">Date</th>
                  <th className="py-2 px-3 text-left font-medium">Measure</th>
                  <th className="py-2 px-3 text-left font-medium">Cost</th>
                  <th className="py-2 px-3 text-left font-medium">Trigger</th>
                </tr>
              </thead>
              <tbody>
                {RELIEF.map((r, i) => (
                  <tr key={i} className="border-b last:border-0 hover:bg-muted/20">
                    <td className="py-2 px-3 whitespace-nowrap">{r.date}</td>
                    <td className="py-2 px-3">{r.measure}</td>
                    <td className="py-2 px-3 whitespace-nowrap text-muted-foreground">{r.cost}</td>
                    <td className="py-2 px-3 text-muted-foreground">{r.trigger}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="mt-3 grid grid-cols-1 md:grid-cols-3 gap-2">
            <div className="border border-green-200 bg-green-50/30 rounded-lg p-3">
              <p className="text-xs font-medium text-green-700">Pre-election pattern</p>
              <p className="text-xs text-green-600 mt-1">Cash handouts, toll freezes, and fuel price cuts cluster around politically sensitive periods. The Oust Anwar rally (Jul 2025) triggered RM2.2bn in immediate relief.</p>
            </div>
            <div className="border border-amber-200 bg-amber-50/30 rounded-lg p-3">
              <p className="text-xs font-medium text-amber-700">Unsustainable costs</p>
              <p className="text-xs text-amber-600 mt-1">Total relief measures since Jul 2025: ~RM20bn+. With debt at 70%, this is not sustainable long-term. Relief is timed for maximum political impact.</p>
            </div>
            <div className="border border-blue-200 bg-blue-50/30 rounded-lg p-3">
              <p className="text-xs font-medium text-blue-700">GE16 timing signal</p>
              <p className="text-xs text-blue-600 mt-1">More relief measures expected in the 6 months before GE16. Historically, Malaysian govts increase handouts before elections. Watch for Budget 2027.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
