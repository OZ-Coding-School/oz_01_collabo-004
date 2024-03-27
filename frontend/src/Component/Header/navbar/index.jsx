import React from 'react';
import { Link } from 'react-router-dom';
import './index.css';

function Navbar() {
  return (
    <div className='navbar'>
      <div className='navbar-links'>
        <ul>
          <li><Link to="/">홈</Link></li>
          <li><Link to="/petshop">반려 여행 상품</Link></li>
          <li><Link to="/pethouse">반려 동반 숙소</Link></li>
          <li><Link to="/petrestaurant">반려 동반 식당</Link></li>
          <li><Link to="/travel">반려 추천 여행지</Link></li>
        </ul>
      </div>
    </div>
  );
}

export default Navbar;