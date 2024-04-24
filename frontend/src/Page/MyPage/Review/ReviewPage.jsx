import React, { useEffect, useState } from "react";
import axios from "../../../api/axios";
import Review from "../Review/Review";
import NewReviewForm from "./NewReviewForm";
import "./Review.css";

function ReviewPage() {
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
        console.log("리뷰", response.data.results);
      } catch (error) {
        console.error("Error fetching reviews:", error);
      }
    };

    fetchReviews();
  }, []);

  const handleShowModal = (reviewId) => {
    setEditReviewId(reviewId);
  };

  const handleCloseModal = () => {
    setEditReviewId(null);
  };

  return (
    <div className="review-page">
      <h2 className="review-page-title">Review List</h2>
      <div className="review-list">
        {reviews.map((review) => (
          <div key={review?.id}>
            <Review review={review} />
            <button onClick={() => handleShowModal(review.id)}> EDIT </button>
            {editReviewId === review.id && (
              <NewReviewForm review={review} setShowModal={handleCloseModal} />
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default ReviewPage;
