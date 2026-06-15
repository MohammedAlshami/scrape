import { NextResponse } from "next/server";
import { query } from "@/lib/neo4j";

export async function GET() {
  const results = await query(
    "MATCH (n:PoliticalParty) RETURN n.name AS name, elementId(n) AS id, n.abbreviation AS abbreviation, n.logo_url AS logo_url ORDER BY n.name",
  );
  const out = [];
  for (const r of results) {
    const rels = await query(
      "MATCH (n:PoliticalParty)-[r]->(m) WHERE elementId(n) = $id RETURN type(r) AS rel, coalesce(m.name, m.title, m.abbreviation) AS target, labels(m)[0] AS target_type",
      { id: r["id"] },
    );
    out.push({
      name: r["name"],
      abbreviation: r["abbreviation"] || "",
      logo_url: r["logo_url"] || "",
      relationships: rels.map((rel: Record<string, unknown>) => ({
        rel: rel["rel"],
        target: rel["target"],
        type: rel["target_type"],
      })),
    });
  }
  return NextResponse.json(out);
}
