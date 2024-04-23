import axios from "axios";
import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Auth = () => {
  const code = new URL(window.location.href).searchParams.get("code");
  console.log("kakao 토큰 : ", code);
  const navigate = useNavigate();
  const kakaoLogin = async () => {
    try {
      const response = await axios.post(
        "/api/v1/user/auth/kakao_login/",
        {
          access_token: code,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true,
        }
      );
      console.log(response);
      if (response.status === 200) {
        localStorage.setItem("token", response.data.token);
        navigate("/");
      }
    } catch (error) {
      console.log(error);
    }
  };
  useEffect(() => {
    if (code) {
      kakaoLogin();
    }
  }, [code]);

  return <div></div>;
};

export default Auth;
