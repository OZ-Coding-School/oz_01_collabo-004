import React, { useState } from "react";
import Review from "./Review";
import "./Review.css";

function ReviewPage() {
  const [reviews, setReviews] = useState([]);

  return (
    <div className="review-page">
      <div className="review-list-container">
        <h2 className="review-list-title">리뷰 목록</h2>
        <div className="review-list">
          {reviews.map((review, index) => (
            <Review key={index} review={review} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default ReviewPage;
