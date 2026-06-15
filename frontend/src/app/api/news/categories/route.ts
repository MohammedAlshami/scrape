import { NextResponse } from "next/server";
import { query } from "@/lib/neo4j";

export async function GET() {
  const results = await query(
    "MATCH (n:Article) WHERE n.categories <> '' "
      + "RETURN n.categories AS cat, count(n) AS c ORDER BY c DESC",
  );
  const cats = new Set<string>();
  for (const r of results) {
    for (const c of (r.cat as string).split(",")) {
      const trimmed = c.trim();
      if (trimmed) cats.add(trimmed);
    }
  }
  return NextResponse.json([...cats].sort());
}
