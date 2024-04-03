/* eslint-disable jsx-a11y/alt-text */
import React from "react";
import { Link } from "react-router-dom";
import Navbar from "../navbar";
import "./index.css";

function Search() {


  return (
    <header className="header">
    <div className="header-container">
      <div className="header-title">
      <Link to="/">
      <img className="logo" src="/images/doggologo.png" />
      </Link>
      </div>

      <Navbar />

      <div className="header-login">
        <ul>
          {/* <span>웰컴</span> */}
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
    </header>
  );
}

export default Search;
