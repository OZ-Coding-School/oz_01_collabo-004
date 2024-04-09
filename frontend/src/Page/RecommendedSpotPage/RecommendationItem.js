import React from "react";

const RecommendationItem = ({ spot }) => {
  return (
    <div style={{ margin: "10px" }} className="recommendation-item">
      <div style={{ margin: "10px" }}>
        <h3>{spot.name}</h3>
        <p>{spot.description}</p>
        <a style={{ textDecoration: "none" }} href={spot.link}>
          홈페이지 바로가기
        </a>
        <hr />
        <img style={{ width: "1200px" }} src={spot.image} />
      </div>
    </div>
  );
};

export default RecommendationItem;
