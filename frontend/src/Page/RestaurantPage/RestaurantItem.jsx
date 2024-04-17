import React from "react";
import RestaurantItem from "./index";
import "./index.css";

const RestaurantPage = () => {
  const restaurantSpots = [
    {
      id: "1",
      name: "도치돌 알파카 목장",
      description: "제주시 애월읍 납읍리 98-1",
      link: "https://www.alpacajeju.com/",
      image: "/images/recommendedImages/도치돌목장.png",
    },
    // 나머지 레스토랑 정보들...
  ];

  return (
    <div className="restaurant-page">
      <h2> 반려 동물과 함께 할 레스토랑 </h2>
      <div className="restaurant-container">
        {restaurantSpots.map((spot) => (
          <RestaurantItem key={spot.id} spot={spot} />
        ))}
      </div>
    </div>
  );
};

export default RestaurantItem;
