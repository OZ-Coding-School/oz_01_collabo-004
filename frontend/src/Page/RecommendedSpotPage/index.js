import React, { useEffect, useState } from "react";
import Spinner from "react-bootstrap/Spinner";
import "./index.css";

const TravelPage = () => {
  const [items, setItems] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    loadMoreItems();
  }, []);

  const loadMoreItems = () => {
    if (!isLoading) {
      setIsLoading(true);
      setTimeout(() => {
        const newItems = Array.from(
          { length: 10 },
          (_, index) => `Item ${items.length + index + 1}`
        );
        setItems((prevItems) => [...prevItems, ...newItems]);
        setIsLoading(false);
      }, 1000);
    }
  };

  const handleScroll = (e) => {
    const bottom =
      Math.ceil(e.target.scrollTop + e.target.clientHeight) >=
      e.target.scrollHeight;
    if (bottom && !isLoading) {
      loadMoreItems();
    }
  };

  return (
    <div className="travel-page-container" onScroll={handleScroll}>
      <h2>추천 여행지</h2>
      {items.map((item, index) => (
        <div key={index} className="travel-item">
          {item}
        </div>
      ))}
      {isLoading && (
        <div className="loading">
          {" "}
          <Spinner animation="border" variant="primary" />
        </div>
      )}
    </div>
  );
};

export default TravelPage;
