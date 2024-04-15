import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../navbar";
import "./index.css";

function Search() {
  const [scrolled, setScrolled] = useState(false);
  const navigate = useNavigate();
  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 0) {
        setScrolled(true);
      } else {
        setScrolled(false);
      }
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  const handleUser = async () => {
    try {
      const response = await axios.post(
        "http://dog-go.store/api/v1/user/logout/",
        {},
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );
      localStorage.removeItem("token");
      window.location.reload();
      navigate("/");
      console.log("로그아웃:", response);
    } catch (error) {
      console.log("로그아웃 에러:", error);
    }
  };
  return (
    <div className={`header-content ${scrolled ? "scrolled" : ""}`}>
      <div className="header-logo">
        <Link to="/">
          <img src="/images/doggologo.png" alt="로고" className="logo" />
        </Link>
      </div>
      <Navbar />
      <div className="header-login">
        <ul>
          {localStorage.getItem("token") ? ( // 토큰이 있으면 로그아웃, 없으면 로그인 링크 표시
            <Link>
              <li onClick={handleUser}>로그아웃</li>
            </Link>
          ) : (
            <Link to="/login">
              <li>로그인</li>
            </Link>
          )}

          <Link to="/mypage">
            <li>마이도꼬</li>
          </Link>
        </ul>
      </div>
    </div>
  );
}

export default Search;
