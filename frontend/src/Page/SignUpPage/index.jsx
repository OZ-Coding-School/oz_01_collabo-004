import { React, useState } from "react";
import "./index.css";

function SignupForm() {
  const [formData, setFormData] = useState({
    id: "",
    username: "",
    email: "",
    phone: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // 비밀번호 일치 확인
    if (formData.password !== formData.confirmPassword) {
      alert("비밀번호가 맞지 않습니다.");
      return;
    }
    // 회원가입 로직 처리
    console.log("Form Submitted", formData);
  };

  return (
    <form className="signup-form" onSubmit={handleSubmit}>
      <h2>회원가입</h2>
      <div className="input-group">
        <label htmlFor="username">사용자 이름</label>
        <input
          type="text"
          id="username"
          name="username"
          value={formData.username}
          onChange={handleChange}
          required
        />
      </div>
      <div className="input-group">
        <label htmlFor="id">아이디</label>
        <input
          type="id"
          id="id"
          name="id"
          value={formData.id}
          onChange={handleChange}
          required
        />
      </div>
      <div className="input-group">
        <label htmlFor="email">이메일 주소</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
        />
      </div>
      <div className="input-group">
        <label htmlFor="phone">전화번호</label>
        <input
          type="phoneNumber"
          id="phone"
          name="phone"
          value={formData.phone}
          onChange={handleChange}
          required
        />
      </div>
      <div className="input-group">
        <label htmlFor="password">비밀번호</label>
        <input
          type="password"
          id="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          required
        />
      </div>
      <div className="input-group">
        <label htmlFor="confirmPassword">비밀번호 확인</label>
        <input
          type="password"
          id="confirmPassword"
          name="confirmPassword"
          value={formData.confirmPassword}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit">가입하기</button>
    </form>
  );
}

export default SignupForm;
