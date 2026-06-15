import { NextResponse } from "next/server";
import { query } from "@/lib/neo4j";

export async function GET() {
  const nodesRaw = await query(
    "MATCH (n) RETURN elementId(n) AS id, labels(n) AS labels, n",
  );
  const edgesRaw = await query(
    "MATCH (a)-[r]->(b) RETURN elementId(a) AS source, elementId(b) AS target, type(r) AS label, elementId(r) AS id",
  );

  const nodes = nodesRaw.map((n: Record<string, unknown>) => {
    const props = n["n"] as Record<string, unknown>;
    const label =
      (props["name"] as string) ||
      (props["title"] as string) ||
      (n["labels"] as string[])[0];
    return {
      id: n["id"],
      label,
      group: (n["labels"] as string[])[0],
      size: 5,
    };
  });

  const edges = edgesRaw.map((e: Record<string, unknown>) => ({
    id: e["id"],
    source: e["source"],
    target: e["target"],
    label: e["label"],
  }));

  return NextResponse.json({ nodes, edges });
}
