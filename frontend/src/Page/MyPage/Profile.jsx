import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../../api/axios";
import Coupon from "./Coupon";
import ProfileModal from "./ProfileModal";

import "./MyPage.css";

function Profile({ setUserId }) {
  const user = {
    user_id: "",
    name: "",
    nickname: "",
    email: "",
    phone: "",
  };

  const [showModal, setShowModal] = useState(false);
  const [userImages, setUserImages] = useState(null);
  const [nickName, setNickName] = useState("");
  const [email, setEmail] = useState(user.email);
  const [phone, setPhone] = useState(user.phone);
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [coupons, setCoupons] = useState([]);
  const [userData, setUserData] = useState({});
  const handleShowModal = () => setShowModal(true);
  const handleCloseModal = () => setShowModal(false);
  const [isChange, setIsChange] = useState(false);

  const handleUserInfo = async () => {
    try {
      const response = await axios.get("/api/v1/user/info/", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });
      setUserId(response.data.user_id);
      setUserData(response.data);
      setNickName(response.data.nickname);
      setEmail(response.data.email);
      setPhone(response.data.phone);

      handleCloseModal();
    } catch (error) {}
  };
  const navigate = useNavigate();

  useEffect(() => {
    if (!localStorage.getItem("token")) {
      navigate("/login");
    }
  }, []);
  const userUpdate = async () => {
    if (password !== confirmPassword) return alert("암호가 일치하지 않습니다.");
    try {
      const formData = new FormData();
      formData.append("nickname", nickName);
      formData.append("email", email);
      formData.append("password", password);
      formData.append("phone", phone);
      if (userImages) {
        formData.append("profile_image", userImages);
      }

      const response = await axios.put("/api/v1/user/info/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });

      if (response.status === 200) {
        alert("회원정보 수정이 완료 되었습니다.");
        setIsChange(true);
        setPassword("");
        setConfirmPassword("");
        setShowModal(false);
      }
    } catch (error) {}
  };

  const handleReceiveCoupon = async () => {
    try {
      const response = await axios.get("/api/v1/coupon/");
      setUserData(response.data);
    } catch (error) {}
  };
  useEffect(() => {
    handleUserInfo();
  }, [isChange]);
  return (
    <div className="my-page-container">
      <div className="profile-section">
        <h2>My DogGo</h2>
        <hr />
        <div className="profile-info">
          <div>
            <img
              style={{
                objectFit: "cover",
                height: "100px",
                width: "100px",
                border: "3px solid rgb(90 120 250)",
                borderRadius: "50%",
                marginLeft: "20px",
              }}
              src={userData.profile_image}
            />
          </div>
          <p>
            <strong>이름 :</strong> {userData.name}
          </p>
          <p>
            <strong>아이디 :</strong> {userData.user_id}
          </p>
          <p>
            <strong>닉네임 :</strong> {userData.nickname}
          </p>

          <p>
            <strong>Email:</strong> {userData.email}{" "}
          </p>
          <p>
            <strong>Phone:</strong> {userData.phone}{" "}
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
        userImages={userImages}
        setUserImages={setUserImages}
        phone={phone}
        setPhone={setPhone}
        password={password}
        setPassword={setPassword}
        confirmPassword={confirmPassword}
        setConfirmPassword={setConfirmPassword}
        user={userData}
        setNickName={setNickName}
        nickname={nickName}
        userUpdate={userUpdate}
      />
    </div>
  );
}

export default Profile;
