import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../../api/axios";
import SignupForm from "../SignUpPage/SignUpPage";
import "./LoginPage.css";

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
  const navigate = useNavigate();
  const code = new URL(window.location.href).searchParams.get("code");

  useEffect(() => {
    if (localStorage.getItem("token")) {
      navigate("/");
    }
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log("Submitting", { user_id, password });

    try {
      const response = await axios.post("/api/v1/user/login/", {
        user_id: user_id,
        password: password,
      });
      localStorage.setItem("token", response.data.access);
      console.log("로그인 성공:", response);
      handleLoginFailure("로그인에 성공했습니다.");
      alert("반갑습니다. DogGo와 행복한 여행 되세요!");
      navigate("/");
    } catch (e) {
      console.log(e);
      handleLoginFailure("로그인에 실패했습니다.");
    }
  };

  function handleLoginFailure(message) {
    setAlertMessage(message);
    setShowAlert(true);
  }

  const kakaoLogin = async () => {
    try {
      const REST_API_KEY = "dbf3d260e4ea71ea45acb4f0c53bd224";
      const REDIRECT_URI = "http://localhost:3000/login";
      const url = `https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=${REST_API_KEY}&redirect_uri=${REDIRECT_URI}&prompt=login`;
      window.location.href = url;

      console.log(code);
    } catch (error) {
      console.log(error);
    }
  };

  const kakaoLogin1 = async () => {
    console.log("인가코드", code);
    try {
      const response = await axios.post(
        "http://dog-go.store/api/v1/user/auth/kakao_login/",
        {
          code: code,
        },
        {
          withCredentials: true,
        }
      );
      console.log(response);
      if (response.status === 200) {
        localStorage.setItem("token", response.data.access);
        navigate("/");
      }
    } catch (error) {
      console.log(error);
      navigate("/login");
    }
  };
  useEffect(() => {
    if (code) {
      kakaoLogin1();
    }
  }, [code]);

  return (
    <>
      <div className="login-container">
        {signUp ? <SignupForm setSignUp={setSignUp} /> : null}
        <div className="doggo">
          <h1>D o g</h1>
          <h1 className="go">G o</h1>
        </div>
        <form className="login-form" onSubmit={handleSubmit}>
          <div>
            <input
              style={{
                border: "none",
                borderBottom: "1px solid #aaaaaa",
                borderRadius: "0",
              }}
              type="text"
              id="user_id"
              value={user_id}
              onChange={(e) => setUser_id(e.target.value)}
              required
            />
            <label htmlFor="user_id">아이디</label>
            <span></span>
          </div>
          <div>
            <input
              style={{
                border: "none",
                borderBottom: "1px solid #aaaaaa",
                borderRadius: "0",
              }}
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <label htmlFor="password">비밀번호</label>
            <span></span>
          </div>
          <button style={{ marginTop: "20px" }} type="submit">
            로그인
          </button>
          <button type="button" onClick={() => setSignUp(true)}>
            회원가입
          </button>
        </form>
        <div id="error-message" className="error-message"></div>{" "}
        <div className="social-button">
          <a
            onClick={kakaoLogin}
            className="kakao-button"
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
