import { NextResponse } from "next/server";
import db from "@/lib/sqlite";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const limit = parseInt(searchParams.get("limit") || "200");
  const offset = parseInt(searchParams.get("offset") || "0");
  const eventType = searchParams.get("type");
  const since = searchParams.get("since");
  const until = searchParams.get("until");

  let sql = "SELECT * FROM events WHERE 1=1";
  const params: unknown[] = [];

  if (eventType) {
    sql += " AND event_type = ?";
    params.push(eventType);
  }
  if (since) {
    sql += " AND date >= ?";
    params.push(since);
  }
  if (until) {
    sql += " AND date <= ?";
    params.push(until);
  }
  sql += " ORDER BY date LIMIT ? OFFSET ?";
  params.push(limit, offset);

  const eventsRaw = db.prepare(sql).all(...params) as Record<string, unknown>[];

  const stats = {
    total_events: (
      db.prepare("SELECT COUNT(*) AS c FROM events").get() as Record<string, unknown>
    ).c as number,
    by_type: Object.fromEntries(
      (
        db
          .prepare(
            "SELECT event_type, COUNT(*) as c FROM events GROUP BY event_type ORDER BY c DESC",
          )
          .all() as { event_type: string; c: number }[]
      ).map((r) => [r.event_type, r.c]),
    ),
    date_range: (
      db.prepare("SELECT MIN(date) as first, MAX(date) as last FROM events").get() as {
        first: string;
        last: string;
      }
    ),
  };

  const events = eventsRaw.map((e) => ({
    id: e.id,
    date: e.date,
    date_precision: e.date_precision,
    event_type: e.event_type,
    title: e.title,
    description: e.description,
    severity: e.severity,
    entities: typeof e.entities === "string" ? JSON.parse(e.entities) : e.entities,
    source_page: e.source_page,
    source_url: e.source_url,
  }));

  return NextResponse.json({ events, stats });
}
