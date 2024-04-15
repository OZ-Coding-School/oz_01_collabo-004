import React, { useRef, useState } from "react";
import useOnclickOutside from "../../hooks/modalClose";
import "./index.css";

function SignupForm({ setSignUp }) {
  const [formData, setFormData] = useState({
    user_id: "",
    name: "",
    email: "",
    phone: "",
    password: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch(
        "https://124f-27-117-139-6.ngrok-free.app/api/v1/user/signup/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        }
      ).then(console.log(JSON.stringify(formData)));

      if (!response.ok) {
        throw new Error("회원가입에 실패했습니다.");
      }
    } catch (error) {
      console.error("회원가입 실패:", error.message);
    }
  };

  const ref = useRef(null);
  useOnclickOutside(ref, () => {
    setSignUp(false);
  });
  return (
    <div ref={ref} className="modal">
      <form className="signup-form" onSubmit={handleSubmit}>
        <div className="sign-tittle" style={{ margin: "20px" }}>
          <h2>Dog</h2>
          <h2 style={{ color: "rgb(90, 120, 250)", marginRight: "10px" }}>
            Go
          </h2>
          <h2>회원가입</h2>
        </div>
        <div className="input-group">
          <label htmlFor="name">사용자 이름</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-group">
          <label htmlFor="user_id">아이디</label>
          <input
            type="text"
            id="user_id"
            name="user_id"
            value={formData.user_id}
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
            type="text"
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
    </div>
  );
}

export default SignupForm;
