import React from "react";
import Recommendationslide from "../../Component/slideshow/Recommendationslide";
import Bestcontentsslide from "../../Component/slideshow/bestcontentsslide";
import Hitscontentslide from "../../Component/slideshow/hitscontentslide";
import "./index.css";

function Banner() {
  return (
    <div className="banner-container">
      <video autoPlay muted loop>
        <source src="/images/A.mp4" type="video/mp4" />
      </video>
      <div className="content-overlay">
        <div className="banner-description">
          <div className="banner-description_img">
            <img
              src={"/images/휴양10.jpg"}
              alt="배너이미지"
              className="bannerimg"
            />
          </div>
          <div className="banner-description_p">
            <h2>
              반려견과 제주를 여행할땐, <span>Dog</span>Go
            </h2>
            <div className="banner-description_p_box">
              <p>사랑하는 반려견과 함께 제주도를 여행할때</p>
              <p>
                반려견과 함께할수 있는 "맛집, 여행지, 숙소"를 추천해주는
                여행플랫폼입니다.
              </p>
              <p>내용추가</p>
              <p>내용추가</p>
              <p>내용추가</p>
              <p>내용추가</p>
            </div>
          </div>
        </div>
      </div>
      <Hitscontentslide />
      <Bestcontentsslide />
      <Recommendationslide />
    </div>
  );
}

export default Banner;