import React, { useState } from "react";
import "./NewReviewForm.css";

function NewReviewForm({ onAddReview }) {
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [rating, setRating] = useState("");
  const [content, setContent] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    const newReview = {
      title,
      author,
      rating,
      content,
    };
    onAddReview(newReview);
    setTitle("");
    setAuthor("");
    setRating("");
    setContent("");
  };

  return (
    <div className="review-form-container">
      <h2 className="form-title">도꼬 리뷰에 참여해주세요.</h2>
      <form onSubmit={handleSubmit} className="review-form">
        <div className="form-group">
          <label>작성자:</label>
          <input
            type="text"
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>평점:</label>
          <select value={rating} onChange={(e) => setRating(e.target.value)}>
            <option value="">평점 선택</option>
            <option value="1">1점</option>
            <option value="2">2점</option>
            <option value="3">3점</option>
            <option value="4">4점</option>
            <option value="5">5점</option>
          </select>
        </div>
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
