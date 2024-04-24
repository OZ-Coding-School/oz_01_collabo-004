import axios from "axios"; // axios import 추가
import React, { useRef, useState } from "react";
import useOnclickOutside from "../../../hooks/modalClose";
import "./NewReviewForm.css";

function NewReviewForm({ review, setShowModal }) {
  const [title, setTitle] = useState(review.title);
  const [content, setContent] = useState(review.content);
  const ref = useRef(null);
  const handleSubmit = async (e) => {
    e.preventDefault();
    const updatedReview = {
      title,
      content,
    };

    try {
      const response = await axios.put(
        `/api/v1/review/${review.id}/`,
        updatedReview,
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );
      console.log("Updated review:", response.data);
      setShowModal(false);
    } catch (error) {
      console.error("Error updating review:", error);
    }
  };
  useOnclickOutside(ref, () => {
    setShowModal(false);
  });
  return (
    <div ref={ref} className="review-form-container">
      <h2 className="form-title">{title}</h2>
      <form onSubmit={handleSubmit} className="review-form">
        <div className="form-group">
          <label>제목:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>내용:</label>
          <textarea
            value={content}
            onChange={(e) => setContent(e.target.value)}
          />
        </div>
        <button type="submit">작성하기</button>
      </form>
    </div>
  );
}

export default NewReviewForm;
