import { NextResponse } from "next/server";
import { execSync } from "child_process";
import path from "path";

export async function POST(request: Request) {
  const body = await request.json();
  const messages = body.messages || [];

  const script = path.resolve(process.cwd(), "..", "tools", "run.py");
  const result = execSync(`python "${script}" chat`, {
    input: JSON.stringify(messages),
    encoding: "utf-8",
    timeout: 120000,
  });

  return NextResponse.json(JSON.parse(result.trim()));
}
