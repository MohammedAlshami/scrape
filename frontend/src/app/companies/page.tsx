import EntityPage from "@/app/entity-page";

export default function CompaniesPage() {
  return (
    <EntityPage
      title="Companies"
      apiPath="/api/companies"
      subtitle="Malaysian publicly-listed companies in the knowledge graph"
      extraFields={[
        { key: "industry", label: "Industry" },
        { key: "ticker", label: "Ticker" },
      ]}
    />
  );
}
