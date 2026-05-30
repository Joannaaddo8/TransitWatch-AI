import { NavLink } from "react-router-dom";
import "../styles/navbar.css";

function Navbar() {
  return (
    <div className="navbar">
      <NavLink to="/" className="nav-link">
        Dashboard
      </NavLink>

      <NavLink to="/insights" className="nav-link">
        AI Insights
      </NavLink>

      <NavLink to="/routes" className="nav-link">
        Routes
      </NavLink>

      <NavLink to="/map" className="nav-link">
        Transit Map
      </NavLink>
    </div>
  );
}

export default Navbar;