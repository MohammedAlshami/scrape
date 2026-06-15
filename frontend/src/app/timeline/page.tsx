"use client";

import { useState, useEffect } from "react";
import Timeline from "@mui/lab/Timeline";
import TimelineItem from "@mui/lab/TimelineItem";
import TimelineSeparator from "@mui/lab/TimelineSeparator";
import TimelineConnector from "@mui/lab/TimelineConnector";
import TimelineContent from "@mui/lab/TimelineContent";
import TimelineOppositeContent from "@mui/lab/TimelineOppositeContent";
import TimelineDot from "@mui/lab/TimelineDot";
import HowToVoteIcon from "@mui/icons-material/HowToVote";
import GroupIcon from "@mui/icons-material/Group";
import HandshakeIcon from "@mui/icons-material/Handshake";
import WarningIcon from "@mui/icons-material/Warning";
import PolicyIcon from "@mui/icons-material/Policy";
import AccountBalanceIcon from "@mui/icons-material/AccountBalance";
import GavelIcon from "@mui/icons-material/Gavel";
import NewReleasesIcon from "@mui/icons-material/NewReleases";
import PublicIcon from "@mui/icons-material/Public";
import BusinessIcon from "@mui/icons-material/Business";
import BiotechIcon from "@mui/icons-material/Biotech";
import EventIcon from "@mui/icons-material/Event";
import Typography from "@mui/material/Typography";

const API = "";

const EVENT_ICONS: Record<string, { icon: typeof HowToVoteIcon; color: string }> = {
  election: { icon: HowToVoteIcon, color: "#e74c3c" },
  leadership: { icon: GroupIcon, color: "#3498db" },
  coalition: { icon: HandshakeIcon, color: "#9b59b6" },
  crisis: { icon: WarningIcon, color: "#e67e22" },
  policy: { icon: PolicyIcon, color: "#1abc9c" },
  economic: { icon: AccountBalanceIcon, color: "#27ae60" },
  legal: { icon: GavelIcon, color: "#2c3e50" },
  scandal: { icon: NewReleasesIcon, color: "#c0392b" },
  international: { icon: PublicIcon, color: "#2980b9" },
  business: { icon: BusinessIcon, color: "#f39c12" },
  covid: { icon: BiotechIcon, color: "#e91e63" },
  cabinet: { icon: GroupIcon, color: "#8e44ad" },
  political: { icon: HowToVoteIcon, color: "#d35400" },
  other: { icon: EventIcon, color: "#7f8c8d" },
};

function formatDate(dateStr: string) {
  const d = new Date(dateStr);
  return d.toLocaleDateString("en-GB", {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}

interface Event {
  id: number;
  date: string;
  date_precision: string;
  event_type: string;
  title: string;
  description: string;
  severity: number;
  entities: string[];
  source_page: string;
  source_url: string;
}

export default function TimelinePage() {
  const [events, setEvents] = useState<Event[]>([]);
  const [stats, setStats] = useState<{
    total_events: number;
    date_range: { first: string; last: string };
    by_type: Record<string, number>;
  } | null>(null);

  useEffect(() => {
    fetch(`${API}/api/events?limit=500`)
      .then((r) => r.json())
      .then((data) => {
        setEvents(data.events);
        setStats(data.stats);
      });
  }, []);

  return (
    <div className="max-w-5xl mx-auto px-4 pt-10 pb-20">
      <div className="text-center mb-12">
        <h1 className="heading-lg mb-3">Events Timeline</h1>
        {stats && (
          <p className="text-muted-foreground text-lg">
            {stats.total_events} events from{" "}
            {formatDate(stats.date_range.first)} to{" "}
            {formatDate(stats.date_range.last)}
          </p>
        )}
      </div>

      <div className="flex flex-wrap justify-center gap-2 mb-10">
        {stats &&
          Object.entries(stats.by_type).map(([type, count]) => {
            const config = EVENT_ICONS[type] || EVENT_ICONS.other;
            return (
              <span
                key={type}
                className="text-xs px-3 py-1.5 rounded-full flex items-center gap-1.5 capitalize"
                style={{
                  backgroundColor: config.color + "18",
                  color: config.color,
                  border: `1px solid ${config.color}30`,
                }}
              >
                {count} {type}
              </span>
            );
          })}
      </div>

      <Timeline position="alternate">
        {events.map((event, idx) => {
          const config = EVENT_ICONS[event.event_type] || EVENT_ICONS.other;
          const Icon = config.icon;

          return (
            <TimelineItem key={event.id}>
              <TimelineOppositeContent
                sx={{ m: "auto 0" }}
                align="right"
                variant="body2"
                className="text-muted-foreground"
              >
                {formatDate(event.date)}
              </TimelineOppositeContent>
              <TimelineSeparator>
                {idx < events.length - 1 && (
                  <TimelineConnector
                    sx={{ bgcolor: config.color + "40" }}
                  />
                )}
                <TimelineDot sx={{ bgcolor: config.color }}>
                  <Icon sx={{ fontSize: 16, color: "#fff" }} />
                </TimelineDot>
                {idx < events.length - 1 && (
                  <TimelineConnector
                    sx={{ bgcolor: config.color + "40" }}
                  />
                )}
              </TimelineSeparator>
              <TimelineContent sx={{ py: "12px", px: 2 }}>
                <Typography variant="subtitle2" sx={{ fontWeight: 600 }}>
                  {event.title}
                </Typography>
                {event.description && (
                  <Typography
                    variant="body2"
                    color="text.secondary"
                    sx={{ mt: 0.5 }}
                  >
                    {event.description}
                  </Typography>
                )}
                {event.entities.length > 0 && (
                  <div className="flex flex-wrap gap-1 mt-2">
                    {event.entities.map((entity: string, i: number) => (
                      <span
                        key={i}
                        className="text-[10px] px-2 py-0.5 rounded-full bg-secondary text-secondary-foreground"
                      >
                        {entity}
                      </span>
                    ))}
                  </div>
                )}
              </TimelineContent>
            </TimelineItem>
          );
        })}
      </Timeline>
    </div>
  );
}
