import KPIOverview from "../components/KPIOverview";
import DelayChart from "../components/DelayChart";

function DashboardPage({ kpis, chartData, trendData }) {
  return (
    <>
      <KPIOverview kpis={kpis} />

      <DelayChart
        chartData={chartData}
        trendData={trendData}
      />
    </>
  );
}

export default DashboardPage;