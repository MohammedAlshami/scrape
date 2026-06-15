import { NextResponse } from "next/server";
import { execSync } from "child_process";
import path from "path";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const q = searchParams.get("q") || "malaysia politics";

  const script = path.resolve(process.cwd(), "..", "tools", "run.py");
  const result = execSync(`python "${script}" scrape "${q}"`, {
    encoding: "utf-8",
    timeout: 60000,
  });

  return NextResponse.json(JSON.parse(result.trim()));
}
