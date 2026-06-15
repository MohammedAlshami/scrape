import EntityPage from "@/app/entity-page";

export default function PartiesPage() {
  return (
    <EntityPage
      title="Political Parties"
      apiPath="/api/parties"
      subtitle="Political parties in the Malaysian knowledge graph"
      extraFields={[
        { key: "abbreviation", label: "Abbreviation" },
      ]}
    />
  );
}
