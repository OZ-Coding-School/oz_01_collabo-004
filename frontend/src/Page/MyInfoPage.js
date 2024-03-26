import React, { useState } from "react";
import "./MyInfoPage.css";

const MyInfoPage = () => {
  // 사용자 정보를 상태로 관리
  const [userInfo, setUserInfo] = useState({
    name: "홍길동",
    email: "hong@example.com",
  });

  // 이메일 업데이트 핸들러
  const handleEmailChange = (e) => {
    setUserInfo({
      ...userInfo,
      email: e.target.value,
    });
  };

  return (
    <div>
      <h1>마이페이지</h1>
      <div>
        <h2>기본 정보</h2>
        <p>이름: {userInfo.name}</p>
        <p>이메일: {userInfo.email}</p>
      </div>
      <div>
        <h2>정보 수정</h2>
        <form>
          <label>
            새 이메일:
            <input
              type="email"
              value={userInfo.email}
              onChange={handleEmailChange}
            />
          </label>
          <button type="button" onClick={() => alert("업데이트 되었습니다.")}>
            업데이트
          </button>
        </form>
      </div>
    </div>
  );
};

export default MyInfoPage;
