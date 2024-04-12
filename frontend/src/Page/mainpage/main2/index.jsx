import { faChevronLeft, faChevronRight } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import React, { useEffect } from 'react';
import './index.css';

function Main2() {
  useEffect(() => {
    const handleNextClick = () => {
      const items = document.querySelectorAll('.item');
      document.querySelector('.slide').appendChild(items[0]);
    };

    const handlePrevClick = () => {
      const items = document.querySelectorAll('.item');
      document.querySelector('.slide').prepend(items[items.length - 1]);
    };

    const nextButton = document.querySelector('.next');
    const prevButton = document.querySelector('.prev');


    if (nextButton && prevButton) {
      nextButton.addEventListener('click', handleNextClick);
      prevButton.addEventListener('click', handlePrevClick);
    }


    return () => {
      if (nextButton && prevButton) {
        nextButton.removeEventListener('click', handleNextClick);
        prevButton.removeEventListener('click', handlePrevClick);
      }
    };
  }, []);
  return (
    <div className='main2-contanier'>
    <div className='main2slideshow-container'>

      <div className='slide'>

        <div className='item' style={{ backgroundImage: "url(./images/반려2.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>제주 펫 플라워 가든 투어</div>
            <div className='des'>
              <h3>"제주 반려동물과 꽃길만 걷자"</h3>
              <p>상품 설명:</p>
              <p>"제주 반려동물과 꽃길만 걷자"는
              반려동물과의 여행을 더욱 특별하게 만들어 줄 경험입니다. 제주 도내 여러 꽃 정원을 탐방하며,
              제철에 피어나는 다양한 꽃들 사이로 특별한 산책을 즐길 수 있습니다.
              꽃향기 가득한 제주의 봄을 반려동물과 함께 만끽하는 시간입니다</p>
            </div>
            <button>See More</button>
          </div>
        </div>

        <div className='item' style={{ backgroundImage: "url(./images/산책1.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>제주 펫 비치워크</div>
            <div className='des'>
            <h3>"제주 해변에서의 펫과의 산책"</h3>
              <p>상품 설명:</p>
              <p>"제주 해변에서의 펫과의 산책"은 제주도의 아름다운 해변을 반려동물과 함께 거닐며,
              파도 소리와 함께 여유로운 시간을 보낼 수 있는 상품입니다. 
              협재, 금능 등 반려동물과 함께 방문할 수 있는 해변에서의 산책을 통해, 
              반려동물과의 특별한 추억을 만들 수 있습니다. 해변에서의 놀이와 휴식은 
              반려동물과 여러분에게 잊지 못할 추억을 선사할 것입니다.</p>
            </div>
            <button>See More</button>
          </div>
        </div>

        <div className='item' style={{ backgroundImage: "url(./images/산책2.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>3번째 가상상품 컨텐츠</div>
            <div className='des'>
              콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명
            </div>
            <button>See More</button>
          </div>
        </div>

        <div className='item' style={{ backgroundImage: "url(./images/산책3.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>4번째 가상상품 컨텐츠</div>
            <div className='des'>
              콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명
            </div>
            <button>See More</button>
          </div>
        </div>

        <div className='item' style={{ backgroundImage: "url(./images/캠핑.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>5번째 가상상품 컨텐츠</div>
            <div className='des'>
              콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명
            </div>
            <button>See More</button>
          </div>
        </div>

        <div className='item' style={{ backgroundImage: "url(./images/캠핑5.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>6번째 가상상품 컨텐츠</div>
            <div className='des'>
              콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명
            </div>
            <button>See More</button>
          </div>
        </div>

      </div>

    <div className='main2slideshow-btn'>
    <button className='prev'><FontAwesomeIcon icon={faChevronLeft} /></button>
      <button className='next'><FontAwesomeIcon icon={faChevronRight} /></button>
    </div>

    </div>
    </div>
  )
}

export default Main2;
