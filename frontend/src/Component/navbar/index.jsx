import React from "react";
import { Link } from "react-router-dom";
import "./index.css";

function Navbar() {
  return (
    <div className="navbar">
      <div className="navbar-links">
        <ul>
            <Link to="/"><li>Main</li></Link>
            <Link to="/petshop"><li>Travel Package</li></Link>
            <Link to="/pethouse"><li>Hotel</li></Link>
            <Link to="/petrestaurant"><li>Restaurant</li></Link>
            <Link to="/travel"><li>Recommended Spot</li></Link>
        </ul>
      </div>
    </div>
  );
}

export default Navbar;
