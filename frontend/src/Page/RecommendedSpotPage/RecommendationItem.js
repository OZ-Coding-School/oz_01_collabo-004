import React from "react";

const RecommendationItem = ({ spot }) => {
  return (
    <div
      style={{
        margin: "10px",
        textAlign: "center",
      }}
      className="recommendation-item"
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
          }}
          src={spot.image}
        />
      </div>
    </div>
  );
};

export default RecommendationItem;
