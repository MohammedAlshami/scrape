"use client"

export default function StateAlignmentSlide() {
  return (
    <section className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">State Election Alignment</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Peninsular vs East Malaysia — diverging voting patterns</p>
        </div>
        <div className="flex-1 min-h-0 overflow-y-auto">
          <p className="text-xs text-muted-foreground mb-2">Sources: <a href="https://en.wikipedia.org/wiki/2023_Malaysian_state_elections" target="_blank" className="underline">2023 state elections</a> &middot; <a href="https://en.wikipedia.org/wiki/Results_of_the_2023_Malaysian_state_elections_by_constituency" target="_blank" className="underline">Results by constituency</a></p>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-3 mb-3">
            <div className="p-3">
              <h3 className="text-xs font-semibold mb-2">West Coast</h3>
              <p className="text-xs text-muted-foreground">Penang, Selangor, Negeri Sembilan, Malacca, Johor, Perak, KL</p>
              <div className="mt-2 space-y-1 text-xs">
                <p><strong>2023 results:</strong> PH+BN held Penang, Selangor, NS</p>
                <p><strong>Trend:</strong> Urban, mixed seats favour PH. Rural Malay seats trending PN.</p>
                <p><strong>Johor 2022:</strong> BN won 40/56 seats. PH 12. PN 0 (before Green Wave).</p>
              </div>
            </div>
            <div className="p-3">
              <h3 className="text-xs font-semibold mb-2">East Coast / North</h3>
              <p className="text-xs text-muted-foreground">Kelantan, Terengganu, Kedah, Perlis, Pahang interior</p>
              <div className="mt-2 space-y-1 text-xs">
                <p><strong>2023 results:</strong> PN swept Kelantan (43/45), Terengganu (32/32), Kedah (33/36)</p>
                <p><strong>Trend:</strong> PAS heartland. PN dominance consolidated. No signs of reversal.</p>
                <p><strong>Nenggiri by-election (Aug 24):</strong> BN flipped 1 seat — rare exception.</p>
              </div>
            </div>
            <div className="p-3">
              <h3 className="text-xs font-semibold mb-2">East Malaysia</h3>
              <p className="text-xs text-muted-foreground">Sabah, Sarawak</p>
              <div className="mt-2 space-y-1 text-xs">
                <p><strong>2021 Sarawak:</strong> GPS won 76/82 seats. Dominant.</p>
                <p><strong>2020 Sabah:</strong> GRS-led govt formed after election.</p>
                <p><strong>2025 Sabah:</strong> GRS won 29, WARISAN 25. Hung assembly.</p>
                <p><strong>Trend:</strong> East Malaysia votes differently — regional issues dominate. Kingmaker role in GE16.</p>
              </div>
            </div>
          </div>

          <div className="p-3">
            <h3 className="text-xs font-semibold mb-2">Peninsular Divergence Map</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
              <div>
                <p className="font-medium mb-1">PH+BN leaning states:</p>
                <ul className="space-y-0.5 text-muted-foreground">
                  <li>Selangor (22 fed seats) — PH stronghold</li>
                  <li>Penang (13) — PH stronghold</li>
                  <li>Johor (26) — BN leaning, PH competitive</li>
                  <li>Perak (24) — Mixed, PH+BN vs PN</li>
                  <li>Negeri Sembilan (8) — PH led govt</li>
                  <li>Malacca (6) — BN led govt</li>
                  <li>KL, Putrajaya, Labuan (13) — Urban, PH leaning</li>
                </ul>
              </div>
              <div>
                <p className="font-medium mb-1">PN leaning states:</p>
                <ul className="space-y-0.5 text-muted-foreground">
                  <li>Kelantan (14 fed seats) — PAS fortress</li>
                  <li>Terengganu (8) — PAS fortress</li>
                  <li>Kedah (15) — PN dominant</li>
                  <li>Perlis (3) — PN held</li>
                  <li>Pahang (14) — Split, BN+PAS (PH weak)</li>
                </ul>
                <p className="font-medium mt-2">Kingmaker blocs:</p>
                <ul className="space-y-0.5 text-muted-foreground">
                  <li>Sarawak (31) — GPS (pro-govt)</li>
                  <li>Sabah (25) — GRS/WARISAN split (pro-govt)</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
