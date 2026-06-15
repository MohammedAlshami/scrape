import { NextResponse } from "next/server";
import { query } from "@/lib/neo4j";

export async function GET() {
  const results = await query(
    "MATCH (n:Person) RETURN n.name AS name, elementId(n) AS id, n.role AS role, n.image_url AS image_url ORDER BY n.name",
  );
  const out = [];
  for (const r of results) {
    const rels = await query(
      "MATCH (n:Person)-[r]->(m) WHERE elementId(n) = $id RETURN type(r) AS rel, coalesce(m.name, m.title, m.abbreviation) AS target, labels(m)[0] AS target_type",
      { id: r["id"] },
    );
    out.push({
      name: r["name"],
      role: r["role"] || "",
      image_url: r["image_url"] || "",
      relationships: rels.map((rel: Record<string, unknown>) => ({
        rel: rel["rel"],
        target: rel["target"],
        type: rel["target_type"],
      })),
    });
  }
  return NextResponse.json(out);
}
