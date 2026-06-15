import EntityPage from "@/app/entity-page";

export default function PeoplePage() {
  return (
    <EntityPage
      title="People"
      apiPath="/api/people"
      subtitle="Political figures in the Malaysian knowledge graph"
      extraFields={[
        { key: "role", label: "Role" },
      ]}
    />
  );
}
