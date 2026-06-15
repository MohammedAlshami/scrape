import { NextResponse } from "next/server";
import { query } from "@/lib/neo4j";

export async function GET() {
  const results = await query(
    "MATCH (n:Election) RETURN n.title AS name, elementId(n) AS id, n.year AS year, n.country AS country ORDER BY n.title",
  );
  const out = [];
  for (const r of results) {
    const rels = await query(
      "MATCH (n:Election)-[r]->(m) WHERE elementId(n) = $id RETURN type(r) AS rel, coalesce(m.name, m.title, m.abbreviation) AS target, labels(m)[0] AS target_type",
      { id: r["id"] },
    );
    out.push({
      name: r["name"],
      year: r["year"] || "",
      country: r["country"] || "",
      relationships: rels.map((rel: Record<string, unknown>) => ({
        rel: rel["rel"],
        target: rel["target"],
        type: rel["target_type"],
      })),
    });
  }
  return NextResponse.json(out);
}
