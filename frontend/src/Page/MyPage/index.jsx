import axios from "axios";
import React, { useState } from "react";
import "./index.css";

function MyPage() {
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePhoneChange = (e) => {
    setPhone(e.target.value); // 함수 이름 수정
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleConfirmPasswordChange = (e) => {
    setConfirmPassword(e.target.value); // 함수 추가
  };

  const handlePhoneSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "https://124f-27-117-139-6.ngrok-free.app/api/v1/user/info/",
        {
          email: email,
          password: password,
          phone: phone,
        }
      );
      console.log("Updated Phone Number:", phone);
    } catch (error) {
      console.error("Error updating phone number:", error);
    }
  };

  const handlePasswordSubmit = async (e) => {
    e.preventDefault();
    try {
      if (password !== confirmPassword) {
        alert("비밀번호와 비밀번호 확인이 일치하지 않습니다.");
        return;
      }
      const response = await axios.post(
        "https://example.com/api/update-password",
        {
          password: password,
        }
      );
      console.log("Updated Password:", password);
    } catch (error) {
      console.error("Error updating password:", error);
    }
  };

  return (
    <div className="my-page-container">
      <div className="profile-section">
        <h2>프로필 정보</h2>
        <div className="profile-info">
          <p>
            <strong>아이디:</strong> user123
          </p>
          <p>
            <strong>이름:</strong> 홍길동
          </p>
          <p>
            <strong>이메일:</strong> user@example.com
          </p>
          <p>
            <strong>전화번호:</strong>{" "}
            <input type="text" value={phone} onChange={handlePhoneChange} />{" "}
            <button onClick={handlePhoneSubmit}>수정</button>
          </p>
        </div>
      </div>
      <div className="edit-section">
        <h2>비밀번호 수정</h2>
        <form onSubmit={handlePasswordSubmit}>
          <div className="input-field">
            <label htmlFor="password">새 비밀번호</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={handlePasswordChange}
              required
            />
          </div>
          <div className="input-field">
            <label htmlFor="confirmPassword">비밀번호 확인</label>
            <input
              type="password"
              id="confirmPassword"
              value={confirmPassword}
              onChange={handleConfirmPasswordChange}
              required
            />
          </div>
          <button className="input-field" type="submit">
            비밀번호 수정
          </button>
        </form>
      </div>
    </div>
  );
}

export default MyPage;
