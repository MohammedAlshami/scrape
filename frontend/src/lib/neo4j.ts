import neo4j from "neo4j-driver";

const driver = neo4j.driver(
  process.env.NEO4J_URI || "bolt://localhost:7687",
  neo4j.auth.basic(
    process.env.NEO4J_USER || "neo4j",
    process.env.NEO4J_PASSWORD || "password",
  ),
);

export function query(cypher: string, params: Record<string, unknown> = {}) {
  const session = driver.session({ database: process.env.NEO4J_DATABASE || "neo4j" });
  return session.run(cypher, params).then((result) => {
    session.close();
    return result.records.map((r) => r.toObject());
  });
}
