import { NextResponse } from "next/server";
import { execSync } from "child_process";
import path from "path";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const url = searchParams.get("url");

  if (!url) {
    return NextResponse.json({ error: "missing url" }, { status: 400 });
  }

  const script = path.resolve(process.cwd(), "..", "tools", "run.py");
  const result = execSync(`python "${script}" article "${url}"`, {
    encoding: "utf-8",
    timeout: 30000,
  });

  const data = JSON.parse(result.trim());
  if (data.error) {
    return NextResponse.json(data, { status: 404 });
  }
  return NextResponse.json(data);
}
