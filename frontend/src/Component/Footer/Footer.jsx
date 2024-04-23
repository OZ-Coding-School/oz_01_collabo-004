import React from "react";
import { Link } from "react-router-dom";
import "./Footer.css";

function Footer() {
  return (
    <footer className="footer">
      <div className="container">
        <div className="column">
          <h3 className="column-title">공지사항</h3>
          <p>사이트제작 팀명 | 오서옵서게</p>
          <p>
            작업자명단 | BD:김기철,유용준/ BE:임대용,김형철/ FE:민덕기,김태율
          </p>
          <p>팀장:임대용 부팀장:민덕기</p>
          <p>주소 | Oz코딩스쿨</p>
          <ul>
            <Link>
              <li>이용약관</li>
            </Link>
            <Link>
              <li>개인정보처리방침</li>
            </Link>
            <Link>
              <li>위치기반서비스</li>
            </Link>
            <Link>
              <li>청소년보호정책</li>
            </Link>
            <Link>
              <li>고객센터</li>
            </Link>
          </ul>
        </div>
        <div className="column">
          <h3 className="column-title">문의하기</h3>
          <p>이메일: alsejrrl9723@naver.com</p>
          <p>전화번호: 010-8948-9709</p>
        </div>
      </div>
      <div className="copyRight">
        &copy; 2024 Example Company. All rights reserved.
      </div>
    </footer>
  );
}

export default Footer;
