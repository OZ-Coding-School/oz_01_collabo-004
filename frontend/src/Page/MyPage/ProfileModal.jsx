import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/esm/Col";
import Row from "react-bootstrap/esm/Row";
import styles from "./ProfileModal.module.css";

function ProfileModal({
  show,
  handleClose,
  email,
  setEmail,
  phone,
  setPhone,
  password,
  setPassword,
  confirmPassword,
  setConfirmPassword,
  user,
  userUpdate,
}) {
  const [imageSrc, setImageSrc] = useState("../images/wonbin.png");

  const handleImageChange = (e) => {
    setImageSrc(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleConfirmPasswordChange = (e) => {
    setConfirmPassword(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePhoneChange = (e) => {
    const formattedPhoneNumber = e.target.value
      .replace(/[^0-9]/g, "")
      .replace(/(\d{3})(\d{3,4})(\d{4})/, "$1-$2-$3");
    setPhone(formattedPhoneNumber);
  };

  return (
    <div
      className={styles.profile_modal}
      style={{ display: show ? "block" : "none" }}
    >
      <h1 style={{ textAlign: "center", margin: "30px", marginBottom: "30px" }}>
        회원정보 변경
      </h1>

      <div className={styles.modal_box}>
        <div style={{ fontSize: "25px" }} className={styles.modal_body}>
          <Row style={{ padding: "0", margin: "0" }}>
            <Col style={{ padding: "0", margin: "0" }}>
              <img
                style={{
                  objectFit: "cover",
                  height: "100px",
                  width: "100px",
                  border: "3px solid rgb(90 120 250)",
                  borderRadius: "50%",
                  marginLeft: "20px",
                }}
                src={imageSrc}
              />
              <button
                onClick={handleImageChange}
                style={{
                  backgroundColor: "rgb(90 120 250 )",
                  color: "white",
                  fontSize: "15px",
                  textAlign: "center",
                  display: "flex",
                  justifyContent: "center",
                  margin: "20px",
                  marginLeft: "40px",
                  width: "60px",
                  height: "30px",
                }}
              >
                EDIT
              </button>
            </Col>
            <Col>
              <div>
                I D .
                <br />
                {user.user_id}
              </div>
              <br />
              <div style={{ marginTop: "-25px" }}>
                NAME .
                <br /> {user.name}
              </div>
            </Col>
          </Row>

          <div style={{ marginTop: "20px" }} className={styles.input_container}>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className={styles.input_container}>
            <input
              type="tel"
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
            />
          </div>
          <div className={styles.input_container}>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="변경 할 비밀번호"
            />
          </div>
          <div className={styles.input_container}>
            <input
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder="비밀번호 확인"
            />
          </div>
        </div>
        <div className={styles.modal_button}>
          <Button onClick={userUpdate}>Save</Button>
          <Button onClick={handleClose}>Close</Button>
        </div>
      </div>
    </div>
  );
}

export default ProfileModal;
