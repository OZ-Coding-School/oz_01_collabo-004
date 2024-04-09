import { faArrowLeft, faArrowRight } from '@fortawesome/free-solid-svg-icons';
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

    document.querySelector('.next').addEventListener('click', handleNextClick);
    document.querySelector('.prev').addEventListener('click', handlePrevClick);

    return () => {
      document.querySelector('.next').removeEventListener('click', handleNextClick);
      document.querySelector('.prev').removeEventListener('click', handlePrevClick);
    };
  }, []);
  return (
    <div className='main2-contanier'>
    <div className='main2slideshow-container'>

      <div className='slide'>

        <div className='item' style={{ backgroundImage: "url(./images/반려2.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>1번째이미지</div>
            <div className='des'>
              콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명
            </div>
            <button>See More</button>
          </div>
        </div>
        <div className='item' style={{ backgroundImage: "url(./images/산책1.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>2번째이미지</div>
            <div className='des'>
              콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명
            </div>
            <button>See More</button>
          </div>
        </div>
        <div className='item' style={{ backgroundImage: "url(./images/산책2.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>3번째이미지</div>
            <div className='des'>
              콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명
            </div>
            <button>See More</button>
          </div>
        </div>
        <div className='item' style={{ backgroundImage: "url(./images/산책3.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>4번째이미지</div>
            <div className='des'>
              콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명
            </div>
            <button>See More</button>
          </div>
        </div>
        <div className='item' style={{ backgroundImage: "url(./images/캠핑.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>5번째이미지</div>
            <div className='des'>
              콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명
            </div>
            <button>See More</button>
          </div>
        </div>
        <div className='item' style={{ backgroundImage: "url(./images/캠핑5.jpg)" }}>
          <div className='main2slideshow-content'>
            <div className='name'>6번째이미지</div>
            <div className='des'>
              콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명콘텐츠설명설명
            </div>
            <button>See More</button>
          </div>
        </div>
    </div>

    <div className='main2slideshow-btn'>
    <button className='prev'><FontAwesomeIcon icon={faArrowLeft} /></button>
            <button className='next'><FontAwesomeIcon icon={faArrowRight} /></button>
    </div>

    </div>
    </div>
  )
}

export default Main2;
