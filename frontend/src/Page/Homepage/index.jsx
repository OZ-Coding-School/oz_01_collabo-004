import React from 'react';
import './index.css';

function Banner() {
  return (
    <div className='banner-container'>
        <div className='banner'>
            <h2>베너 및 광고</h2>
        </div>
        <div className='banner-description'>
        <div className='banner-description_img'>
        <img src={'/images/휴양10.jpg'}
        alt='배너이미지' 
        className='bannerimg'
        />
        </div>
        <div className='banner-description_p'>
        <h2>반려견과 제주를 여행할땐, <span>Dog</span>Go</h2>
        <div className='banner-description_p_box'>
        <p>사랑하는 반려견과 함께 제주도를 여행할때</p>
        <p>반려견과 함께할수 있는 "맛집, 여행지, 숙소"를 추천해주는 여행플랫폼입니다.</p>
        </div>
        </div>
        </div>
    </div>
  )
}

export default Banner