import React, { useEffect, useState } from 'react';
import './index.css';

function Mainpage() {
  const [loadedH1, setLoadedH1] = useState(false);
  const [loadedP, setLoadedP] = useState(false);

  useEffect(() => {
    setTimeout(() => {
      setLoadedH1(true); 
      setTimeout(() => {
        setLoadedP(true);
      }, 250);
    }, 250);
  }, []);

  return (
    <div className={`main-container ${loadedH1 ? 'loadedH1' : ''}`}>
      <div className={`main-content ${loadedP ? 'loadedP' : ''}`}>
        <div className='mainvideo-container'>
          <video autoPlay muted loop className='main-video'>
            <source src="/images/mainvideo.mp4" type="video/mp4" />
          </video>
        </div>
        <div className='main-content-introduction'>
          <h1>Welcome.</h1>
          <h1>DoGGo</h1>
          <p className={loadedP ? 'show' : ''}>함께하는 친구와의 추억은 언제나 특별합니다.</p>
          <p className={loadedP ? 'show' : ''}>제주도의 아름다움이 당신을 기다리고 있습니다. </p>
          <p className={loadedP ? 'show' : ''}>여행의 마법에 빠져보세요!</p>
        </div>
      </div>
    </div>
  );
}

export default Mainpage;


