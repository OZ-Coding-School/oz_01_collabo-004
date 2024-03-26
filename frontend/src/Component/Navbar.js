import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  return (
    <div>
      <div className="navbar">
        <Link to="/">Home</Link>
        <Link to="/petshop">PetShop</Link>
        <Link to="/pethouse">PetHouse</Link>
        <Link to="/petrestaurant">PetRestaurant</Link>
        <Link to="/travel">Travel</Link>
        <Link to="/myinfo">MyInfo</Link>
        <Link to="/service">Service</Link>
      </div>
    </div>
  );
}

export default Navbar;
