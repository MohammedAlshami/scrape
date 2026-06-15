"use client"

const FLOODS = [
  { year: "1971", deaths: 32, displaced: "180,000", cost: "-", states: "Kuala Lumpur", months: "Jan" },
  { year: "2006-07", deaths: 15, displaced: "70,000", cost: "$395M", states: "Johor, Melaka, Pahang", months: "Dec-Jan" },
  { year: "2010", deaths: 4, displaced: "50,000", cost: "-", states: "Kedah, Perlis, Kelantan", months: "Oct-Nov" },
  { year: "2014-15", deaths: 21, displaced: "200,000+", cost: "$560M", states: "11 states (worst widespread)", months: "Dec-Jan" },
  { year: "2017", deaths: 7, displaced: "7,294+", cost: "$76.3M", states: "Kedah, Penang, Perak", months: "Nov" },
  { year: "2020-21", deaths: 9, displaced: "Tens of thousands", cost: "-", states: "Pahang, Johor, Terengganu, Kelantan", months: "Nov-Jan" },
  { year: "2021-22", deaths: 54, displaced: "125,490+", cost: "$1.27-1.55B", states: "Selangor, KL, Pahang, Perak, N.Sembilan", months: "Dec-Jan" },
]

export default function FloodsSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Flood Risk & Election Timing</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Major flood events & implications for GE16 scheduling</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <p className="text-xs text-muted-foreground mb-2">Source: <a href="https://en.wikipedia.org/wiki/Floods_in_Malaysia" target="_blank" className="underline">Wikipedia (Floods in Malaysia)</a></p>
          <div className="border border-foreground/10 rounded-lg overflow-hidden mb-3">
            <table className="w-full text-xs">
              <thead><tr className="border-b bg-muted/30">
                <th className="py-1.5 px-2 text-left">Year</th><th className="py-1.5 px-2 text-left">Deaths</th><th className="py-1.5 px-2 text-left">Displaced</th>
                <th className="py-1.5 px-2 text-left">Cost</th><th className="py-1.5 px-2 text-left">Months</th>
              </tr></thead>
              <tbody>{FLOODS.map((f, i) => (
                <tr key={i} className="border-b last:border-0 hover:bg-muted/20">
                  <td className="py-1.5 px-2">{f.year}</td><td className="py-1.5 px-2">{f.deaths}</td>
                  <td className="py-1.5 px-2">{f.displaced}</td><td className="py-1.5 px-2">{f.cost}</td>
                  <td className="py-1.5 px-2 font-medium">{f.months}</td>
                </tr>
              ))}</tbody>
            </table>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
            <div className="p-3 border border-red-200 bg-red-50/30 rounded-lg">
              <p className="font-medium text-red-700">Highest risk months: Dec-Jan</p>
              <p className="text-red-600 mt-1">54 deaths in 2021-22 floods. GE15 (Nov 2022) had polling suspended in Baram due to flooding.</p>
            </div>
            <div className="p-3 border border-green-200 bg-green-50/30 rounded-lg">
              <p className="font-medium text-green-700">Safest window: May-Sep</p>
              <p className="text-green-600 mt-1">Southwest monsoon = low rainfall. Best period for campaigning and polling logistics.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
