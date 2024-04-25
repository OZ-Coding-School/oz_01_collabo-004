import React, { useRef, useState } from "react";
import axios from "../../../api/axios";
import useOnclickOutside from "../../../hooks/modalClose";
import "./ReviewEdit.css";

function ReviewEdit({ review, setShowModal }) {
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
        <button type="submit">Img</button>
        <button type="submit">EDIT</button>
      </form>
    </div>
  );
}

export default ReviewEdit;
