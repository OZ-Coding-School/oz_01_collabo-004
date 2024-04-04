import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../navbar';
import './index.css';

function Search() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 0) {
        setScrolled(true); // 스크롤이 발생하면 scrolled를 true로 설정
      } else {
        setScrolled(false); // 스크롤이 상단으로 올라가면 scrolled를 false로 설정
      }
    };

    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div className={`header-content ${scrolled ? 'scrolled' : ''}`}>
      <div className="header-logo">
        <Link to="/">
          <img className="logo" src="/images/doggologo.png" />
        </Link>
      </div>
      <Navbar />
      <div className="header-login">
        <ul>
          <Link to="/login"><li>로그인</li></Link>
          <Link to="/mypage"><li>마이도꼬</li></Link>
        </ul>
      </div>
    </div>
  );
}

export default Search;


