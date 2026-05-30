import TransitMap from "../components/TransitMap";

function MapPage({ routePaths, liveVehicles }) {
  return (
    <>
      <h2>🗺️ Transit Operations Map</h2>

      <p>
        Real TTC route geometry and live TTC vehicle positions powered by GTFS Static and GTFS-Realtime data. Vehicle locations refresh automatically every 30 seconds.
      </p>

      <TransitMap
        routePaths={routePaths}
        liveVehicles={liveVehicles}
      />
    </>
  );
}

export default MapPage;