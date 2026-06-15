import EntityPage from "@/app/entity-page";

export default function ElectionsPage() {
  return (
    <EntityPage
      title="Elections"
      apiPath="/api/elections"
      subtitle="Malaysian general elections in the knowledge graph"
      extraFields={[
        { key: "year", label: "Year" },
        { key: "country", label: "Country" },
      ]}
    />
  );
}
