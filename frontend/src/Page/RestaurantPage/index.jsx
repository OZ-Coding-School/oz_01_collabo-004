import React from "react";

const RestaurantItem = ({ spot }) => {
  if (!spot) return null; // spot이 정의되지 않았을 경우 컴포넌트를 null로 반환합니다.

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
          alt={spot.name} // 이미지에 대한 대체 텍스트를 제공합니다.
        />
      </div>
    </div>
  );
};

export default RestaurantItem;
