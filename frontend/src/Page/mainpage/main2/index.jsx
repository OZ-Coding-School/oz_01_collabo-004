import { faChevronLeft, faChevronRight, } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React, { useEffect } from "react";
import "./index.css";

function Main2() {
  useEffect(() => {
    const handleNextClick = () => {
      const items = document.querySelectorAll(".item");
      document.querySelector(".slide").appendChild(items[0]);
    };

    const handlePrevClick = () => {
      const items = document.querySelectorAll(".item");
      document.querySelector(".slide").prepend(items[items.length - 1]);
    };

    const nextButton = document.querySelector(".next");
    const prevButton = document.querySelector(".prev");

    if (nextButton && prevButton) {
      nextButton.addEventListener("click", handleNextClick);
      prevButton.addEventListener("click", handlePrevClick);
    }

    return () => {
      if (nextButton && prevButton) {
        nextButton.removeEventListener("click", handleNextClick);
        prevButton.removeEventListener("click", handlePrevClick);
      }
    };
  }, []);
  return (
    <div className="main2-contanier">
      <div className="main2slideshow-container">

        <div className="slide">
          <div
            className="item"
            style={{ backgroundImage: "url(./images/펫플라워가든투어.png)" }}
          >
            <div className="main2slideshow-content">
              <div className="main2slideshow-content-title">
                <h2>제주 펫 플라워 가든 투어</h2>
                <h5>제주 반려동물과 꽃길만 걷자</h5>
              </div>
              <button>SEE MORE</button>
            </div>
          </div>

          <div
            className="item"
            style={{ backgroundImage: "url(./images/pet_beach_walk.jpeg)" }}>
            <div className="main2slideshow-content">
              <div className="main2slideshow-content-title">
                <h2>제주 펫 비치워크</h2>
                <h5>제주 해변에서의 펫과의 산책</h5>
              </div>
              <button>SEE MORE</button>
            </div>
          </div>

          <div
            className="item"
            style={{ backgroundImage: "url(./images/제주숲속펫테라피워크.png)" }}>
            <div className="main2slideshow-content">
              <div className="main2slideshow-content-title">
                <h2>제주 숲속 펫테라피 워크</h2>
                <h5>숲속의 속삭임, 펫과 함께하는 치유 여행</h5>
              </div>
              <button>SEE MORE</button>
            </div>
          </div>

          <div
            className="item"
            style={{ backgroundImage: "url(./images/pethighking.jpeg)" }}
          >
            <div className="main2slideshow-content">
              <div className="main2slideshow-content-title">
                <h2>제주 오름 펫테라피 하이킹</h2>
                <h5>"오름 정상에서 만나는 펫테라피</h5>
              </div>
              <button>SEE MORE</button>
            </div>
          </div>

          <div
            className="item"
            style={{ backgroundImage: "url(./images/제주펫캠핑리트리트.png)" }}
          >
            <div className="main2slideshow-content">
              <div className="main2slideshow-content-title">
                <h2>제주 펫 캠핑 리트리트</h2>
                <h5>제주에서의 반려동물과 힐링 캠프</h5>
              </div>
              <button>SEE MORE</button>
            </div>
          </div>

          <div
            className="item"
            style={{ backgroundImage: "url(./images/제주펫포레스트캠핑.png)" }}
          >
            <div className="main2slideshow-content">
              <div className="main2slideshow-content-title">
                <h2>제주 펫 포레스트 캠핑</h2>
                <h5>숲속의 반려동물과 휴식 시간</h5>
              </div>
              <button>SEE MORE</button>
            </div>
          </div>
        </div>

        <div className="main2slideshow-btn">
          <button className="prev">
            <FontAwesomeIcon icon={faChevronLeft} />
          </button>
          <button className="next">
            <FontAwesomeIcon icon={faChevronRight} />
          </button>
        </div>
      </div>
    </div>
  );
}

export default Main2;
