import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./index.css";

function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log("Submitting", { username, password });
  };

  return (
    <div className="login-container">
      <div className="doggo">
        <h1>D o g</h1>
        <h1 className="go">G o</h1>
      </div>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">아이디</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
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
    </div>
  );
}

export default LoginPage;
