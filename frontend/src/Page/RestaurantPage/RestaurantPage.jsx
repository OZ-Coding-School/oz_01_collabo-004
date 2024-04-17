import React from "react";

const RestaurantPage = ({ spot }) => {
  return (
    <div
      style={{
        margin: "10px",
        textAlign: "center",
      }}
      className="restaurant-item"
    >
      <div style={{ margin: "10px" }}>
        <h3>{spot.name}</h3>
        <p>{spot.description}</p>
        <a target="_blank" style={{ textDecoration: "none" }} href={spot.link}>
          🏠Click Me!
        </a>
        <hr />
        <img
          style={{
            width: "700px",
            height: "350px",
          }}
          src={spot.image}
          alt={spot.name}
        />
      </div>
    </div>
  );
};

export default RestaurantPage;
