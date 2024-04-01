import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./index.css";

let aut_acc = "";
const kakaoParams = {
  client_id: "dbf3d260e4ea71ea45acb4f0c53bd224",
  redirect_uri: "http://127.0.0.1:3000/user/social/kakao/login",
  response_type: "code",
};
const kParams = new URLSearchParams(kakaoParams).toString();

function LoginPage() {
  const [user_id, setUser_id] = useState("");
  const [password, setPassword] = useState("");
  // const history = useHistory();

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log("Submitting", { user_id, password });

    try {
      const response = await fetch(
        "https://124f-27-117-139-6.ngrok-free.app/api/v1/user/login/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          credentials: "include",
          body: JSON.stringify({ user_id: user_id, password: password }),
        }
      )
        .then((response) => response.json())
        .then((jsonData) => {
          console.log(jsonData);
          aut_acc = jsonData.access;
          // history.push("/");
        })
        .then(console.log(aut_acc));

      // if (!response.status === 200) {
      //   throw new Error("로그인에 실패했습니다.");
      // }
    } catch (e) {
      console.log(e);
    }
  };

  return (
    <>
      <div className="login-container">
        <div className="doggo">
          <h1>D o g</h1>
          <h1 className="go">G o</h1>
        </div>
        <form onSubmit={handleSubmit}>
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
          <Link to="/signup">
            <button type="button">회원가입</button>
          </Link>
        </form>
        <a
          href={`https://kauuth.kakao.com/oauth/authorize?${kParams}`}
          style={{
            backgroundColor: "#fff",
          }}
        >
          {" "}
          <img
            className="kakao"
            src="/images/kakao_login_medium_narrow.png"
            alt="뻐큐
              "
          />{" "}
        </a>
        <div className="kakaogoogle">
          <button
            style={{
              backgroundColor: "#fff",
              height: "10px",
            }}
          >
            {" "}
            <img
              style={{
                width: "180px",
              }}
              className="google"
              src="/images/ios_light_sq_SI@3x.png"
              alt="뻐큐
              "
            />{" "}
          </button>
        </div>
      </div>
    </>
  );
}
export default LoginPage;
