import React, { useState } from "react";
import axios from "../../api/axios";
import SignupForm from "../SignUpPage";
import "./index.css";

function AlertModal({ message, onClose }) {
  return (
    <div className="modal-overlay">
      <div className="alert-modal">
        <p>{message}</p>
        <button onClick={onClose}>닫기</button>
      </div>
    </div>
  );
}

function LoginPage() {
  const [user_id, setUser_id] = useState("");
  const [password, setPassword] = useState("");
  const [showAlert, setShowAlert] = useState(false);
  const [alertMessage, setAlertMessage] = useState("");
  const [signUp, setSignUp] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log("Submitting", { user_id, password });

    try {
      const response = await axios.post("/login", {
        id: user_id,
        pw: password,
      });
      axios.defaults.headers.common[
        "Authorization"
      ] = `Bearer ${response.date.token}`;
      console.log(response.data.token);

      handleLoginFailure("로그인에 성공했습니다.");
    } catch (e) {
      console.log(e);
      handleLoginFailure("로그인에 실패했습니다.");
    }
  };

  function handleLoginFailure(message) {
    setAlertMessage(message);
    setShowAlert(true);
  }

  const kakaoParams = {
    client_id: "dbf3d260e4ea71ea45acb4f0c53bd224",
    redirect_uri: "http://127.0.0.1:3000/user/social/kakao/login",
    response_type: "code",
  };
  const kParams = new URLSearchParams(kakaoParams).toString();
  console.log(signUp);

  return (
    <>
      <div className="login-container">
        {/* <div className="signUpModal"> */}
        {signUp ? <SignupForm setSignUp={setSignUp} /> : null}
        {/* </div> */}
        <div className="doggo">
          <h1>D o g</h1>
          <h1 className="go">G o</h1>
        </div>
        <form className="login-form" onSubmit={handleSubmit}>
          <div>
            <label htmlFor="user_id">아이디</label>
            <input
              type="text"
              id="user_id"
              value={user_id}
              onChange={(e) => setUser_id(e.target.value)}
              required
            />
          </div>
          <div>
            <label htmlFor="password">비밀번호</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit">로그인</button>
          {/* <Link to="/signup"> */}
          <button type="button" onClick={() => setSignUp(true)}>
            회원가입
          </button>
          {/* </Link> */}
        </form>
        <div id="error-message" className="error-message"></div>{" "}
        <div className="social-button">
          <a
            className="kakao-button"
            href={`https://kauuth.kakao.com/oauth/authorize?${kParams}`}
            style={{
              backgroundColor: "#fff",
            }}
          >
            <img
              style={{
                width: "170px",
                margin: "0",
              }}
              className="kakao"
              src="/images/kakao_login_medium_narrow.png"
              alt="카카오 로그인"
            />
          </a>
          <div>
            <a>
              <img
                style={{
                  width: "180px",
                }}
                className="google"
                src="/images/ios_light_sq_SI@3x.png"
                alt="구글 로그인"
              />
            </a>
          </div>
        </div>
      </div>
      {showAlert && (
        <AlertModal
          message={alertMessage}
          onClose={() => setShowAlert(false)}
        />
      )}
    </>
  );
}

export default LoginPage;
