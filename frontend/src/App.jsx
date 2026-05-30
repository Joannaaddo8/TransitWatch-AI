import { useEffect, useState } from "react";
import API from "./services/api";
import { Routes, Route } from "react-router-dom";

import {
  Chart as ChartJS,
  BarElement,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

import "leaflet/dist/leaflet.css";

import Navbar from "./components/Navbar";
import DashboardPage from "./pages/DashboardPage";
import InsightsPage from "./pages/InsightsPage";
import RoutesPage from "./pages/RoutesPage";
import MapPage from "./pages/MapPage";

ChartJS.register(
  BarElement,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale
);

function App() {
  const [kpis, setKpis] = useState(null);
  const [insights, setInsights] = useState([]);
  const [worstRoutes, setWorstRoutes] = useState([]);
  const [routePaths, setRoutePaths] = useState({});
  const [liveVehicles, setLiveVehicles] = useState([]);

  useEffect(() => {
    API.get("/dashboard")
      .then((res) => setKpis(res.data.data))
      .catch((err) => console.error(err));

    API.get("/insights")
      .then((res) => setInsights(res.data.insights))
      .catch((err) => console.error(err));

    API.get("/routes/worst")
      .then((res) => setWorstRoutes(res.data.data))
      .catch((err) => console.error(err));

    API.get("/routes/shapes")
      .then((res) => setRoutePaths(res.data.data))
      .catch((err) => console.error(err));

    const fetchLiveVehicles = () => {
      API.get("/vehicles/live")
        .then((res) => {
          setLiveVehicles(res.data.data);
        })
        .catch((err) => console.error(err));
    };

    fetchLiveVehicles();

    const interval = setInterval(fetchLiveVehicles, 30000);

    return () => clearInterval(interval);
  }, []);

  if (!kpis) {
    return (
      <div className="app-container">
        <h2>🚍 Loading TransitWatch AI...</h2>
      </div>
    );
  }

  const chartData = {
    labels: ["On-Time Trips", "Delayed Trips"],
    datasets: [
      {
        label: "Trips",
        data: [kpis.on_time_trips, kpis.delayed_trips],
        backgroundColor: ["green", "red"],
      },
    ],
  };

  const trendData = {
    labels: Object.keys(kpis.delay_by_hour || {}),
    datasets: [
      {
        label: "Delay Minutes by Hour",
        data: Object.values(kpis.delay_by_hour || {}),
        borderColor: "orange",
        backgroundColor: "orange",
        tension: 0.3,
      },
    ],
  };

  return (
    <div className="app-container">
      <h1 className="app-title">🚍 TransitWatch AI Dashboard</h1>

      <Navbar />

      <Routes>
        <Route
          path="/"
          element={
            <DashboardPage
              kpis={kpis}
              chartData={chartData}
              trendData={trendData}
            />
          }
        />

        <Route
          path="/insights"
          element={<InsightsPage insights={insights} />}
        />

        <Route
          path="/routes"
          element={<RoutesPage worstRoutes={worstRoutes} />}
        />

        <Route
          path="/map"
          element={
            <MapPage
              routePaths={routePaths}
              liveVehicles={liveVehicles}
            />
          }
        />
      </Routes>
    </div>
  );
}

export default App;