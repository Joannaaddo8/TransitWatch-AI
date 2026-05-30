import { Bar, Line } from "react-chartjs-2";
import "../styles/dashboard.css";

function DelayChart({ chartData, trendData }) {
  return (
    <>
      <div style={{ width: "500px", marginBottom: "40px" }}>
        <Bar data={chartData} />
      </div>

      <h2>📈 Delay Trends</h2>

      <div style={{ width: "700px" }}>
        <Line data={trendData} />
      </div>
    </>
  );
}

export default DelayChart;