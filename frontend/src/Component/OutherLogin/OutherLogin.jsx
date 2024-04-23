import React from "react";
import "./OutherLogin.css";

function OtherLogin() {
  return (
    <div className="paymentpage-other-login">
      <button className="naver-login">
        <img src="./images/Logo/NaverLogo.png" alt="네이버로고" />
        <p>네이버로그인</p>
      </button>

      <button className="KaKao-login">
        <img src="./images/Logo/KaKaoLogo.png" alt="네이버로고" />
        <p>카카오로그인</p>
      </button>

      <button className="google-login">
        <img src="./images/Logo/GoogleLogo.png" alt="네이버로고" />
        <p>구글로그인</p>
      </button>

      <button className="facebook-login">
        <img src="./images/Logo/FacebookLogo.png" alt="네이버로고" />
        <p>페이스북로그인</p>
      </button>
    </div>
  );
}

export default OtherLogin;
