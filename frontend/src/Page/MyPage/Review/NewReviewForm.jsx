import React, { useRef, useState } from "react";
import useOnclickOutside from "../../../hooks/modalClose";
import "./NewReviewForm.css";

function NewReviewForm({ review, setShowModal }) {
  const [title, setTitle] = useState(review.title);
  const [content, setContent] = useState(review.content);
  const ref = useRef(null);
  const handleSubmit = (e) => {
    e.preventDefault();
    const newReview = {
      title,
      content,
    };

    setTitle("");
    setContent("");
  };
  useOnclickOutside(ref, () => {
    setShowModal(false);
  });
  return (
    <div ref={ref} className="review-form-container">
      <h2 className="form-title">도꼬 리뷰에 참여해주세요.</h2>
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
