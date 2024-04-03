import React from "react";
import { Link } from "react-router-dom";
import "./index.css";

function Search() {


  return (
    <div className="header-container">
        <div className="header-title">
        <Link to="/">
          <img className="logo" src="/images/doggologo.png" />
        </Link>
      </div>
      <div className="header-login">
        <ul>
          <span>웰컴</span>
          <Link to="/login">
            <li>로그인</li>
          </Link>
          <Link to="/mypage">
            <li>마이도꼬</li>
          </Link>
          <Link to="/service">
            <li>고객센터</li>
          </Link>
        </ul>
      </div>
    </div>
  );
}

export default Search;
