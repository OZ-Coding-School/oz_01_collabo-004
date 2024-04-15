import React, { useState } from "react";
import Coupon from "./Coupon";
import ProfileModal from "./ProfileModal";
import "./index.css";

function Profile() {
  const user = {
    user_id: "user_id",
    name: "홍길동",
    email: "start@gmail.com",
    phone: "010-1234-1234",
  };

  const [showModal, setShowModal] = useState(false);
  const [email, setEmail] = useState(user.email);
  const [phone, setPhone] = useState(user.phone);
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [coupons, setCoupons] = useState([]);

  const handleShowModal = () => setShowModal(true);
  const handleCloseModal = () => setShowModal(false);

  const handleSaveChanges = async () => {
    try {
      // 저장하는 API 호출
      handleCloseModal();
    } catch (error) {
      console.error("Error saving changes:", error);
    }
  };

  const handleReceiveCoupon = async () => {
    try {
      // 쿠폰 받는 API 호출
    } catch (error) {
      console.error("Error receiving coupon:", error);
    }
  };

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
            <strong>Email:</strong> {email}{" "}
          </p>
          <p>
            <strong>Phone:</strong> {phone}{" "}
          </p>

          <button onClick={handleShowModal}>회원정보 수정</button>
        </div>
      </div>

      <div className="coupon-section">
        <h2>내 쿠폰</h2>
        <Coupon onReceiveCoupon={handleReceiveCoupon} />
        <ul>
          {coupons.map((coupon, index) => (
            <li key={index}>{coupon}</li>
          ))}
        </ul>
      </div>

      <ProfileModal
        show={showModal}
        handleClose={handleCloseModal}
        email={email}
        setEmail={setEmail}
        phone={phone}
        setPhone={setPhone}
        password={password}
        setPassword={setPassword}
        confirmPassword={confirmPassword}
        setConfirmPassword={setConfirmPassword}
        handleSave={handleSaveChanges}
        user={user}
      />
    </div>
  );
}

export default Profile;
