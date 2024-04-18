import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../../api/axios";
import Coupon from "./Coupon";
import ProfileModal from "./ProfileModal";
import "./index.css";

function Profile() {
  const user = {
    user_id: "",
    name: "",
    email: "",
    phone: "",
  };

  const [showModal, setShowModal] = useState(false);
  const [userImages, setUserImages] = useState(user.userImages);
  const [email, setEmail] = useState(user.email);
  const [phone, setPhone] = useState(user.phone);
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [coupons, setCoupons] = useState([]);
  const [userData, setUserData] = useState({});
  const handleShowModal = () => setShowModal(true);
  const handleCloseModal = () => setShowModal(false);

  const handleSaveChanges = async () => {
    try {
      const response = await axios.get("/api/v1/user/info/", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });
      setUserData(response.data);

      handleCloseModal();
    } catch (error) {
      console.error("Error saving changes:", error);
    }
  };
  const navigate = useNavigate();

  useEffect(() => {
    if (!localStorage.getItem("token")) {
      navigate("/login");
    }
  }, []);

  const handleReceiveCoupon = async () => {
    try {
      const response = await axios.get("http://dog-go.store/api/v1/coupon/");
      setUserData(response.data);
      console.log("User Coupon:", response.data);
    } catch (error) {
      console.error("Error receiving coupon:", error);
    }
  };
  useEffect(() => {
    handleSaveChanges();
  }, []);
  return (
    <div className="my-page-container">
      <div className="profile-section">
        <h2>My DogGo</h2>
        <hr />
        <div className="profile-info">
          <p>
            <strong>아이디 :</strong> {userData.user_id}
          </p>
          <p>
            <strong>이름 :</strong> {userData.name}
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
        phone={phone}
        setPhone={setPhone}
        password={password}
        setPassword={setPassword}
        confirmPassword={confirmPassword}
        setConfirmPassword={setConfirmPassword}
        handleSave={handleSaveChanges}
        user={userData}
      />
    </div>
  );
}

export default Profile;
