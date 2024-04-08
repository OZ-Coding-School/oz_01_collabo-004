import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./index.css";

function LoginMyPage({ onLogout }) {
  return (
    <div>
      <h2>My Page</h2>
      <p>Welcome to My Page!</p>
      <button onClick={onLogout}>Logout</button>
      <Link to="/login">Back to Login</Link>
    </div>
  );
}

function Profile() {
  const user = { user_id: "userid", name: "홍길동", email: "start@gmail.com" };
  const [email, setEmail] = useState(user.email);
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
          user_id: user.user_id,
          name: user.name,
          email: user.email,
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

  useEffect(() => {
    const fetchUserInfo = async () => {
      try {
        const response = await axios.get("https://example.com/api/user-info");
        const { email, phone } = response.data;
        setEmail(email);
        setPhone(phone);
      } catch (error) {
        console.error("Error fetching user info:", error);
      }
    };

    fetchUserInfo();
  }, []);

  return (
    <div className="my-page-container">
      <div className="profile-section">
        <h2>My DogGo</h2>
        <hr />
        <div className="profile-info">
          <p>
            <strong>아이디 :</strong> {user.user_id}
          </p>
          <p>
            <strong>이름 :</strong> {user.name}
          </p>
          <p>
            <strong>이메일 :</strong> {email}
          </p>
          <p>
            <strong>전화번호:</strong>{" "}
            <button onClick={handlePhoneSubmit}>수정</button>
          </p>
        </div>
      </div>

      <div className="edit-section">
        <form onSubmit={handlePasswordSubmit}>
          <div className="input-field">
            <label htmlFor="password"></label>
            <input
              placeholder="새 비밀번호"
              type="password"
              id="password"
              value={password}
              onChange={handlePasswordChange}
              required
            />
          </div>
          <div className="input-field">
            <label htmlFor="confirmPassword"></label>
            <input
              placeholder="비밀번호 확인"
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

export default Profile;
