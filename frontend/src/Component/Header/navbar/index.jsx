import React from 'react';
import { Link } from 'react-router-dom';
import './index.css';

function Navbar() {
  return (
    <div className='navbar'>
      <div className='navbar-links'>
        <ul>
          <Link><li>홈</li></Link>
          <Link><li>반려 여행 상품</li></Link>
          <Link><li>반려 동반 숙소</li></Link>
          <Link><li>반려 동반 식당</li></Link>
          <Link><li>반려 추천 여행지</li></Link>
        </ul>
      </div>
    </div>
  );
}

export default Navbar;