import { MapContainer, TileLayer, Polyline, Marker, Popup } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

import markerIcon2x from "leaflet/dist/images/marker-icon-2x.png";
import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: markerIcon2x,
  iconUrl: markerIcon,
  shadowUrl: markerShadow,
});

function TransitMap({ routePaths = {}, liveVehicles = [] }) {
  const vehicles = liveVehicles || [];
  return (
    <div style={{ height: "600px", width: "100%" }}>
      <MapContainer
        center={[43.72, -79.42]}
        zoom={11}
        style={{ height: "100%", width: "100%" }}
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

        {Object.entries(routePaths || {}).map(([route, coords]) => (
          <Polyline
            key={route}
            positions={coords}
            color="blue"
            weight={3}
            opacity={0.6}
          />
        ))}

        {vehicles.map((vehicle) => (
          <Marker
            key={vehicle.vehicle_id}
            position={[vehicle.latitude, vehicle.longitude]}
          >
            <Popup>
  <h4>🚍 TTC Vehicle</h4>

  <b>Vehicle ID:</b> {vehicle.vehicle_id}
  <br />

  <b>Route:</b> {vehicle.route_id}
  <br />

  <b>Trip:</b> {vehicle.trip_id}
  <br />

  <b>Status:</b> Live Position Feed
</Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}

export default TransitMap;