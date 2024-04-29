import React, { useState } from "react";
import axios from "../../../api/axios";
import "./ReviewModal.css";

const ReviewModal = ({ onClose, productId, setCount }) => {
  const [title, setTitle] = useState("");
  const [image_file, setImage] = useState("");
  const [content, setContent] = useState("");
  console.log(title, image_file, content, productId);
  const handleSubmit = async () => {
    try {
      const formData = new FormData();
      formData.append("title", title);
      formData.append("image_file", image_file);
      formData.append("content", content);
      formData.append("product", productId);

      const response = await axios.post("/api/v1/review/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });

      console.log(" 보내기", response);
      setCount((prev) => prev + 1);
      onClose();
    } catch (error) {
      console.error("Error submitting review:", error);
    }
  };

  return (
    <div className="review-modal">
      <h3 className="review-modal-title">리뷰 작성</h3>
      <input
        type="text"
        className="review-modal-input"
        placeholder="제목"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <input
        type="file"
        className="review-modal-input"
        accept="image/*"
        onChange={(e) => setImage(e.target.files[0])}
      />
      <textarea
        className="review-modal-textarea"
        placeholder="내용"
        value={content}
        onChange={(e) => setContent(e.target.value)}
      ></textarea>
      <button className="review-modal-button" onClick={handleSubmit}>
        리뷰 제출
      </button>
      <button className="review-modal-button" onClick={onClose}>
        닫기
      </button>
    </div>
  );
};

export default ReviewModal;
