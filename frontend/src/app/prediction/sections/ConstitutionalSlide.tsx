"use client"

import Timeline from "@mui/lab/Timeline"
import TimelineItem from "@mui/lab/TimelineItem"
import TimelineSeparator from "@mui/lab/TimelineSeparator"
import TimelineConnector from "@mui/lab/TimelineConnector"
import TimelineContent from "@mui/lab/TimelineContent"
import TimelineOppositeContent from "@mui/lab/TimelineOppositeContent"
import TimelineDot from "@mui/lab/TimelineDot"
import HowToVoteIcon from "@mui/icons-material/HowToVote"
import GroupIcon from "@mui/icons-material/Group"
import WarningIcon from "@mui/icons-material/Warning"
import AccountBalanceIcon from "@mui/icons-material/AccountBalance"
import EventIcon from "@mui/icons-material/Event"
import Typography from "@mui/material/Typography"
import { TIMELINE_EVENTS, EVENT_ICONS } from "./shared"

export default function ConstitutionalSlide() {
  return (
    <section id="constitutional" className="h-screen w-full flex flex-col snap-start overflow-hidden">
      <div className="flex flex-col h-full max-w-7xl mx-auto w-full px-6 md:px-8 py-6 md:py-10">
        <div className="shrink-0 mb-6 md:mb-8">
          <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">Constitutional Constraints</h2>
          <p className="text-sm md:text-base text-muted-foreground mt-1">Maximum parliamentary term, dissolution rules &amp; PM discretion</p>
        </div>

        <div className="flex-1 min-h-0 overflow-y-auto grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6 auto-rows-min">
          {/* Card 1 */}
          <div>
            <h3 className="text-sm md:text-base font-semibold mb-2">Maximum Parliamentary Term</h3>
            <p className="text-lg md:text-2xl font-bold text-blue-600 mb-1">5 Years</p>
            <p className="text-sm md:text-base text-muted-foreground leading-relaxed">
              Article 55(3) of the Federal Constitution: Parliament continues for <strong>5 years</strong> from its first meeting and shall then stand dissolved.
            </p>
            <div className="mt-3 text-sm md:text-base text-muted-foreground leading-relaxed space-y-1">
              <div className="flex justify-between"><span>First sitting:</span><span className="font-medium text-foreground">19 Dec 2022</span></div>
              <div className="flex justify-between"><span>Auto dissolution:</span><span className="font-medium text-foreground">19 Dec 2027</span></div>
              <div className="flex justify-between"><span>Latest election:</span><span className="font-medium text-foreground">17 Feb 2028</span></div>
            </div>
            <a href="https://en.wikipedia.org/wiki/Constitution_of_Malaysia" target="_blank" className="text-xs md:text-sm text-blue-600 underline mt-2 inline-block">Source: Constitution Art 55</a>
          </div>

          {/* Card 2 */}
          <div>
            <h3 className="text-sm md:text-base font-semibold mb-2">Dissolution Rules</h3>
            <ul className="space-y-2 text-sm md:text-base">
              <li className="leading-relaxed"><strong>Art 40(2)(b):</strong> YDPA dissolves Parliament on the PM&rsquo;s advice. The YDPA <span className="italic">may</span> withhold consent — but this has never been exercised in Malaysian history.</li>
              <li className="leading-relaxed"><strong>Art 55(4):</strong> An election must be held within <strong>60 days</strong> of dissolution.</li>
              <li className="leading-relaxed"><strong>Art 55(5):</strong> Parliament must reconvene within <strong>120 days</strong> of dissolution.</li>
              <li className="leading-relaxed">The PM can advise dissolution at <strong>any time</strong> — no parliamentary vote or no-confidence motion is required.</li>
            </ul>
            <a href="https://en.wikipedia.org/wiki/Constitution_of_Malaysia" target="_blank" className="text-xs md:text-sm text-blue-600 underline mt-2 inline-block">Source: Constitution of Malaysia</a>
          </div>

          {/* Card 3 */}
          <div>
            <h3 className="text-sm md:text-base font-semibold mb-2">PM Discretion &amp; Precedent</h3>
            <ul className="space-y-2 text-sm md:text-base">
              <li className="leading-relaxed">The PM has <strong>absolute discretion</strong> to advise the YDPA on dissolution timing.</li>
              <li className="leading-relaxed"><strong>4 of the last 6</strong> general elections were called early. Only GE11 and GE13 ran near the full term.</li>
              <li className="leading-relaxed">Average dissolution-to-polling period: <strong>28 days</strong>. The trend is going longer (19 days in 1999 to 40 days in 2022).</li>
              <li className="leading-relaxed">Anwar (Jul 2025): &ldquo;tunggu pilihan raya dua tahun lagi&rdquo; — he is signalling he wants a full term.</li>
            </ul>
            <a href="https://en.wikipedia.org/wiki/Next_Malaysian_general_election" target="_blank" className="text-xs md:text-sm text-blue-600 underline mt-2 inline-block">Source: Next Malaysian GE page</a>
          </div>

          {/* Timeline */}
          <div className="md:col-span-3 mt-2">
            <p className="text-xs md:text-sm text-muted-foreground mb-3">Sources: <a href="https://en.wikipedia.org/wiki/Next_Malaysian_general_election" target="_blank" className="underline">Next GE page</a> &middot; <a href="https://en.wikipedia.org/wiki/Constitution_of_Malaysia" target="_blank" className="underline">Constitution Art 55</a> &middot; <a href="/data/insights/elections/ge_turnout.csv" className="underline">Download CSV</a></p>
            <Timeline sx={{ flexDirection: "row", alignItems: "flex-start", py: 0 }}>
              {TIMELINE_EVENTS.slice(0, 4).map((ev, i) => {
                const cfg = EVENT_ICONS[ev.type] || EVENT_ICONS.other
                const Icon = cfg.icon
                return (
                  <TimelineItem key={i} sx={{ flex: 1, minWidth: 0, "&::before": { flex: 0 } }}>
                    <TimelineOppositeContent sx={{ display: "none" }} />
                    <TimelineSeparator sx={{ flexDirection: "column", alignItems: "center" }}>
                      <TimelineDot sx={{ bgcolor: cfg.color, my: 0.5 }}><Icon sx={{ fontSize: 14, color: "#fff" }} /></TimelineDot>
                      {i < 3 && <TimelineConnector sx={{ bgcolor: cfg.color + "40", minHeight: 24, width: 2 }} />}
                    </TimelineSeparator>
                    <TimelineContent sx={{ py: "4px", px: 1 }}>
                      <Typography variant="caption" color="text.secondary" sx={{ display: "block", fontSize: "0.7rem" }}>{ev.date}</Typography>
                      <Typography variant="body2" sx={{ fontWeight: 600, lineHeight: 1.3, fontSize: "0.75rem" }}>{ev.event}</Typography>
                    </TimelineContent>
                  </TimelineItem>
                )
              })}
            </Timeline>
          </div>
        </div>
      </div>
    </section>
  )
}
