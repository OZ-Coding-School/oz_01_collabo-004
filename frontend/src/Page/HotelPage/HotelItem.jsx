import React from "react";

const HotelItem = ({ spot }) => {
  return (
    <div
      style={{
        margin: "10px",
        textAlign: "center",
      }}
      className="hotel-item"
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
            width: "600px",
            height: "350px",
            alt: "images",
          }}
          src={spot.image}
          alt="img"
        />
      </div>
    </div>
  );
};

export default HotelItem;
