import WorstRoutesTable from "../components/WorstRoutesTable";

function RoutesPage({ worstRoutes }) {
  return (
    <>
      <h2>🚨 Top Worst Routes</h2>

      <WorstRoutesTable worstRoutes={worstRoutes} />
    </>
  );
}

export default RoutesPage;