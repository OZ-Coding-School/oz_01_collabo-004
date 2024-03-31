import React, { useState } from "react";
import "./index.css";

function MyPage() {
  const [phoneNumber, setPhoneNumber] = useState("010-1234-5678");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handlePhoneNumberChange = (e) => {
    setPhoneNumber(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleConfirmPasswordChange = (e) => {
    setConfirmPassword(e.target.value);
  };

  const handlePhoneSubmit = (e) => {
    e.preventDefault();
    // 여기서 서버로 수정된 전화번호를 전송하는 API 호출을 할 수 있습니다.
    console.log("Updated Phone Number:", phoneNumber);
    // 전화번호 수정 완료 후 필요한 작업을 수행할 수 있습니다.
  };

  const handlePasswordSubmit = (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      alert("비밀번호와 비밀번호 확인이 일치하지 않습니다.");
      return;
    }
    // 여기서 서버로 수정된 비밀번호를 전송하는 API 호출을 할 수 있습니다.
    console.log("Updated Password:", password);
    // 비밀번호 수정 완료 후 필요한 작업을 수행할 수 있습니다.
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
            <strong>전화번호:</strong> {phoneNumber}{" "}
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
