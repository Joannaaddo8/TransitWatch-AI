import "../styles/dashboard.css";

function KPIOverview({ kpis }) {
  return (
    <div className="kpi-grid">
      <div className="kpi-card">
        <h3>Total Trips</h3>
        <p>{kpis.total_trips}</p>
      </div>

      <div className="kpi-card">
        <h3>Delay Frequency</h3>
        <p>{kpis.delay_frequency_percent}%</p>
      </div>

      <div className="kpi-card">
        <h3>Reliability Score</h3>
        <p>{kpis.reliability_score}%</p>
      </div>
    </div>
  );
}

export default KPIOverview;