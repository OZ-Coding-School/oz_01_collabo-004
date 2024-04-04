import axios from "axios";
import React, { useEffect, useState } from "react";
import "./index.css";

function MyPage() {
  // 이전 내용 시작
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
  // 이전 내용 끝

  // 위시 리스트 시작
  const [wishList, setWishList] = useState([]);
  const [wishItem, setWishItem] = useState("");

  const handleAddWishItem = () => {
    if (wishItem.trim() !== "") {
      setWishList([...wishList, wishItem]);
      setWishItem("");
    }
  };

  const handleRemoveWishItem = (index) => {
    const updatedWishList = [...wishList];
    updatedWishList.splice(index, 1);
    setWishList(updatedWishList);
  };
  // 위시 리스트 끝

  // 내 정보 불러오기 시작
  useEffect(() => {
    // 이 부분에서 내 정보를 불러오는 API를 호출하고, 그 결과를 이용하여 상태를 업데이트합니다.
    const fetchUserInfo = async () => {
      try {
        const response = await axios.get("https://example.com/api/user-info");
        const { email, phone } = response.data; // 예시: response.data에는 email과 phone 정보가 있다고 가정합니다.
        setEmail(email);
        setPhone(phone);
      } catch (error) {
        console.error("Error fetching user info:", error);
      }
    };

    fetchUserInfo();
  }, []);
  // 내 정보 불러오기 끝

  return (
    <div className="my-page-container">
      {/* 프로필 정보 */}
      <div className="profile-section">
        <h2>프로필 정보</h2>
        <div className="profile-info">
          <p>
            <strong>이메일:</strong> {email}
          </p>
          <p>
            <strong>전화번호:</strong>{" "}
            <input type="text" value={phone} onChange={handlePhoneChange} />{" "}
            <button onClick={handlePhoneSubmit}>수정</button>
          </p>
        </div>
      </div>

      {/* 위시 리스트 */}
      <div className="wish-list-section">
        <h2>위시 리스트</h2>
        <div>
          <input
            type="text"
            value={wishItem}
            onChange={(e) => setWishItem(e.target.value)}
          />
          <button onClick={handleAddWishItem}>추가</button>
        </div>
        <ul>
          {wishList.map((item, index) => (
            <li key={index}>
              {item}
              <button onClick={() => handleRemoveWishItem(index)}>삭제</button>
            </li>
          ))}
        </ul>
      </div>

      {/* 비밀번호 수정 */}
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
