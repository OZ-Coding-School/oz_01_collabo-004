import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../navbar";
import "./index.css";

function Search() {
  const [scrolled, setScrolled] = useState(false);
  const navigate = useNavigate();
  const [profileImage, setProfileImage] = useState(
    localStorage.getItem("profileImage")
  );

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
      console.log("로그아웃:", response);
      localStorage.removeItem("profileImage");
      navigate("/");
      alert("로그아웃 되었습니다.");
    } catch (error) {
      console.log("로그아웃 에러:", error);
    }
  };

  const handleScroll = () => {
    if (window.scrollY > 0) {
      setScrolled(true);
    } else {
      setScrolled(false);
    }
  };

  window.addEventListener("scroll", handleScroll);

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
          {localStorage.getItem("token") ? (
            <>
              {profileImage && (
                <img
                  src={profileImage}
                  alt="프로필 이미지"
                  style={{ width: "30px", height: "30px", borderRadius: "50%" }}
                />
              )}
              <Link>
                <li onClick={handleUser}>로그아웃</li>
              </Link>
            </>
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
