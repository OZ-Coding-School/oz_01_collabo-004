// ProfileModal.jsx

import React from "react";
import Button from "react-bootstrap/Button";
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
  handleSave,
  user,
}) {
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
    setPhone(e.target.value);
  };

  const handleSaveChanges = () => {
    handleSave();
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
          <div>
            아이디
            <br />
            {user.user_id}
          </div>
          <br />
          <div>
            이름
            <br /> {user.name}
          </div>
          <br />
          <div className={styles.input_container}>
            <input type="email" value={email} onChange={handleEmailChange} />
          </div>
          <div className={styles.input_container}>
            <input type="tel" value={phone} onChange={handlePhoneChange} />
          </div>
          <div className={styles.input_container}>
            <input
              type="password"
              value={password}
              onChange={handlePasswordChange}
              placeholder="변경 할 비밀번호"
            />
          </div>
          <div className={styles.input_container}>
            <input
              type="password"
              value={confirmPassword}
              onChange={handleConfirmPasswordChange}
              placeholder="비밀번호 확인"
            />
          </div>
        </div>
        <div className={styles.modal_button}>
          <Button onClick={handleSaveChanges}>Save</Button>
          <Button onClick={handleClose}>Close</Button>
        </div>
      </div>
    </div>
  );
}

export default ProfileModal;
