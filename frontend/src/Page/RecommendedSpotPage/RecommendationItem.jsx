import React from "react";
import { Link } from "react-router-dom";

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
        <Link
          target="_blank"
          style={{ textDecoration: "none" }}
          href={spot.link}
        />
        🏠Click Me!
        <hr />
        <img
          style={{
            width: "600px",
            height: "350px",
          }}
          src={spot.image}
          alt="recommendimg"
        />
      </div>
    </div>
  );
};

export default RecommendationItem;
