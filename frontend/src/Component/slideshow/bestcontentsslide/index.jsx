import React from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick-theme.css';
import 'slick-carousel/slick/slick.css';
import './index.css';

const NextArrow = (props) => {
  const { className, style, onClick } = props;
  return (
    <div
      className={className}
      style={{ ...style, 
      display: "block", 
      background: "#289aff" }}
      onClick={onClick}
    />
  );
}

const PrevArrow = (props) => {
  const { className, style, onClick } = props;
  return (
    <div
      className={className}
      style={{ ...style, 
        display: "block",
        color:"black",
        background: "#289aff",
    }}
      onClick={onClick}
    />
  );
}

const images = [
    "/images/산책3.jpg",
    "/images/반려3.jpg",
    "/images/반려6.jpg",
    "/images/산책2.jpg",
    "/images/반려동물 캠프2.jpg",
    "/images/캠핑7.jpg"
  ];
  
  function Bestcontentsslide() {
    const settings = {
      dots: true,
      speed: 1500,
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 3,
      autoplay: true,
      autoplaySpeed: 3000,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ],
      nextArrow: <NextArrow />,
      prevArrow: <PrevArrow /> 
    };
  
    return (
      <div className='slide-container'>
        <h2>구매율 높은 컨텐츠</h2>
        <div className="slide-container-items">
        <Slider {...settings}>
          {images.map((image, index) => (
            <div key={index} className="slide-item">
              <img src={image} alt={`Slide${index + 1}`} />
            </div>
          ))}
        </Slider>
      </div>
      </div>
    );
  }

export default Bestcontentsslide;
