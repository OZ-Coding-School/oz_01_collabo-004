import React, { useEffect, useState } from "react";
import axios from "../../../api/axios";
import Review from "../Review/Review";
import NewReviewForm from "./NewReviewForm";
import "./Review.css";

function ReviewPage() {
  const [showModal, setShowModal] = useState(false);
  const [reviews, setReviews] = useState([]);
  const [review, setReview] = useState({});

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

  const handleShowModal = (review) => {
    setShowModal(true);
    setReview(review);
  };

  const reviewForm = async (id) => {
    const response = await axios.put(`/api/v1/review/${id}/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  };

  return (
    <div className="review-page">
      <h2 className="review-page-title">Review List</h2>
      <div className="review-list">
        {reviews.map((review) => (
          <div key={review?.id}>
            <Review review={review} />
            <button onClick={() => handleShowModal(review)}> EDIT </button>
          </div>
        ))}
      </div>
      {showModal ? (
        <NewReviewForm review={review} setShowModal={setShowModal} />
      ) : null}
    </div>
  );
}

export default ReviewPage;
