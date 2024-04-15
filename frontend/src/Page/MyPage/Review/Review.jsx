import React from "react";
import "./Review.css";

function Review({ review }) {
  return (
    <div className="review">
      <h3 className="review-title">{review.title}</h3>
      <p className="review-author">작성자: {review.author}</p>
      <p className="review-rating">평점: {review.rating}</p>
      <p className="review-content">{review.content}</p>
    </div>
  );
}

export default Review;
