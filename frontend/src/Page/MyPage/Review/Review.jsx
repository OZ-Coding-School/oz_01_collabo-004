import React from "react";

function Review({ review }) {
  return (
    <div className="review">
      <h3 className="review-title">{review.title}</h3>
      <p className="review-content">{review.content}</p>
      {review.image_url && (
        <img src={review.image_url} alt="Review" className="review-image" />
      )}
      <p className="review-created-at">Created At: {review.created_at}</p>
      <p className="review-view-count">View Count: {review.view_count}</p>
    </div>
  );
}

export default Review;
