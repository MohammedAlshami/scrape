import { NextResponse } from "next/server";
import { query } from "@/lib/neo4j";

const PAGE_SIZE = 12;

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const q = searchParams.get("q") || "";
  const page = parseInt(searchParams.get("page") || "1");
  const skip = (page - 1) * PAGE_SIZE;

  let total: number;
  let results: Record<string, unknown>[];

  if (q) {
    const countResult = await query(
      "MATCH (n:Article) WHERE toLower(n.title) CONTAINS toLower($q) "
        + "OR toLower(n.summary) CONTAINS toLower($q) "
        + "OR toLower(n.categories) CONTAINS toLower($q) "
        + "RETURN count(n) AS total",
      { q },
    );
    total = countResult[0]["total"] as number;
    results = await query(
      "MATCH (n:Article) WHERE toLower(n.title) CONTAINS toLower($q) "
        + "OR toLower(n.summary) CONTAINS toLower($q) "
        + "OR toLower(n.categories) CONTAINS toLower($q) "
        + "RETURN n.title AS title, n.url AS url, n.image_url AS image_url, "
        + "n.summary AS summary, n.published_at AS published_at, n.author AS author, "
        + "n.categories AS categories "
        + "ORDER BY n.published_at DESC SKIP $skip LIMIT $limit",
      { q, skip, limit: PAGE_SIZE },
    );
  } else {
    const countResult = await query(
      "MATCH (n:Article) RETURN count(n) AS total",
    );
    total = countResult[0]["total"] as number;
    results = await query(
      "MATCH (n:Article) "
        + "RETURN n.title AS title, n.url AS url, n.image_url AS image_url, "
        + "n.summary AS summary, n.published_at AS published_at, n.author AS author, "
        + "n.categories AS categories "
        + "ORDER BY n.published_at DESC SKIP $skip LIMIT $limit",
      { skip, limit: PAGE_SIZE },
    );
  }

  const articles = results.map((r) => ({
    title: r.title,
    url: r.url,
    image_url: r.image_url,
    summary: r.summary,
    published_at: r.published_at,
    author: r.author,
    categories: typeof r.categories === "string"
      ? (r.categories as string).split(",").filter(Boolean)
      : [],
  }));

  return NextResponse.json({
    articles,
    total,
    page,
    pageSize: PAGE_SIZE,
    totalPages: Math.max(1, Math.ceil(total / PAGE_SIZE)),
  });
}
