import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../navbar";
import "./index.css";

function Search() {
  const [scrolled, setScrolled] = useState(false);

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

  return (
    <div className={`header-content ${scrolled ? "scrolled" : ""}`}>
      <div className="header-logo">
        <Link to="/">
        <img 
        src='/images/doggologo.png' alt='로고'
        className='logo'
        />
        </Link>
      </div>
      <Navbar />
      <div className="header-login">
        <ul>
          <Link to="/login">
            <li>로그인</li>
          </Link>
          <Link to="/mypage">
            <li>마이도꼬</li>
          </Link>
        </ul>
      </div>
    </div>
  );
}

export default Search;
