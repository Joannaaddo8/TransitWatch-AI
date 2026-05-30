import "../styles/dashboard.css";

function WorstRoutesTable({ worstRoutes }) {
  return (
    <div className="table-card">
      <table className="data-table">
        <thead>
          <tr>
            <th>Route</th>
            <th>Reliability</th>
            <th>Avg Delay</th>
            <th>Total Trips</th>
          </tr>
        </thead>

        <tbody>
          {worstRoutes.map((route) => (
            <tr key={route.route}>
              <td>{route.route}</td>
              <td>{route.reliability_score}%</td>
              <td>{route.average_delay_minutes} mins</td>
              <td>{route.total_trips}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default WorstRoutesTable;