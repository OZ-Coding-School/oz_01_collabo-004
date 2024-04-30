import React, { useEffect, useState } from "react";
import axios from "../../../api/axios";
import ReviewEdit from "./ReviewEdit";
import "./ReviewPage.css";

const ReviewPage = (count) => {
  const [reviews, setReviews] = useState([]);
  const [editReviewId, setEditReviewId] = useState(null);

  useEffect(() => {
    const fetchReviews = async () => {
      try {
        const response = await axios.get("/api/v1/review/", {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        });
        setReviews(response.data.results);
      } catch (error) {}
    };

    fetchReviews();
  }, [count]);

  const handleShowModal = (reviewId) => {
    setEditReviewId(reviewId);
  };

  const handleCloseModal = () => {
    setEditReviewId(null);
  };

  const formatDate = (dateString) => {
    const createdAt = new Date(dateString);
    return `${createdAt.getFullYear()}-${(createdAt.getMonth() + 1)
      .toString()
      .padStart(2, "0")}-${createdAt
      .getDate()
      .toString()
      .padStart(2, "0")} ${createdAt
      .getHours()
      .toString()
      .padStart(2, "0")}:${createdAt
      .getMinutes()
      .toString()
      .padStart(2, "0")}:${createdAt.getSeconds().toString().padStart(2, "0")}`;
  };

  return (
    <div className="review-page">
      <div className="review-list">
        {reviews.map((review) => (
          <div key={review?.id} className="review-container">
            <div className="review">
              <h3 className="review-title">{review.title}</h3>
              <div className="review-count">
                <p className="review-view-count">조회수: {review.view_count}</p>
                <p>작성일: {formatDate(review.created_at)}</p>
              </div>
              <div className="review-line"></div>
              <p className="review-content">{review.content}</p>
              <div className="review-line"></div>
              {review.image_url && (
                <img
                  style={{ width: "200px" }}
                  src={review.image_url}
                  alt="Review"
                  className="review-image"
                />
              )}
              <button
                className="review-bt"
                onClick={() => handleShowModal(review.id)}
              >
                EDIT
              </button>
              {editReviewId === review.id && (
                <ReviewEdit review={review} setShowModal={handleCloseModal} />
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ReviewPage;
