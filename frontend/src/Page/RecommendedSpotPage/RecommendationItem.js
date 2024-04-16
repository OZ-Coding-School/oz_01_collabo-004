import React from "react";

const RecommendationItem = ({ spot }) => {
  return (
    <div
      style={{
        backgroundImage: `url('/images/noname.png')`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        minHeight: "100vh",
        margin: "10px",
        textAlign: "center",
      }}
      className="recommendation-item"
    >
      <div style={{ margin: "10px" }}>
        <h3>{spot.name}</h3>
        <p>{spot.description}</p>
        <a style={{ textDecoration: "none" }} href={spot.link}>
          🏠Click Me!
        </a>
        <hr />
        <img
          style={{
            width: "1000px",
          }}
          src={spot.image}
        />
      </div>
    </div>
  );
};

export default RecommendationItem;
