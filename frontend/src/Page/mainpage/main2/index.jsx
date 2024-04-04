import React from 'react';
import { Link } from 'react-router-dom';
import './index.css';

function Main2() {
  return (
    <div className='main-content2'>
      <div className='main-content2-btn'>
      <div className='main-content-btn_title'>
      <h1>DogGo에서 보여드립니다.</h1>
      <p>제주도에서 반려동물과 함께할 수 있는</p>
      <p>패키지, 숙소, 식당, 장소를 추천받고</p>
      <p>DogGo에서 추천받고 행복한 여행 되세요</p>
      </div>
        <ul>
          <Link to='/petshop'><li>여행패키지</li></Link>
          <Link to='/pethouse'><li>숙소</li></Link>
          <Link to='/petrestaurant'><li>식당</li></Link>
          <Link to='/travel'><li>추천장소</li></Link>
        </ul>
      </div>
      </div>
  )
}

export default Main2