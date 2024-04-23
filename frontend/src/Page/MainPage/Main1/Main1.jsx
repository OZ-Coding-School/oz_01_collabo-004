import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./Main1.css";

function Main1() {
  const [loadedH1, setLoadedH1] = useState(false);
  const [loadedH2, setLoadedH2] = useState(false);
  const [loadedH3, setLoadedH3] = useState(false);
  const [loadedH4, setLoadedH4] = useState(false);
  const [loadedP1, setLoadedP1] = useState(false);

  useEffect(() => {
    setTimeout(() => {
      setLoadedH1(true);
    }, 200);
    setTimeout(() => {
      setLoadedH2(true);
    }, 300);
    setTimeout(() => {
      setLoadedH3(true);
    }, 400);
    setTimeout(() => {
      setLoadedH4(true);
    }, 500);

    setTimeout(() => {
      setLoadedP1(true);
    }, 700);
  }, []);

  return (
    <div className={`main-container ${loadedH1 ? "loadedH1" : ""}`}>
      <div className={`main-content ${loadedP1 ? "loadedP" : ""}`}>
        <div className="mainvideo-container">
          <video autoPlay muted loop className="main-video">
            <source src="/images/mainvideo.mp4" type="video/mp4" />
          </video>
        </div>
        <div className="main-content-introduction">
          <h1 className={loadedH1 ? "show" : ""}>Welcome.</h1>
          <h1 className={loadedH2 ? "show" : ""}>DogGo</h1>
          <h1 className={loadedH3 ? "show" : ""}>When you travel to</h1>
          <h1 className={loadedH4 ? "show" : ""}>Jeju with your pet</h1>
          <p className={loadedP1 ? "show" : ""}>
            함께하는 친구와의 추억은 언제나 특별합니다.
          </p>
          <p className={loadedP1 ? "show" : ""}>
            제주도의 아름다움이 당신을 기다리고 있습니다.{" "}
          </p>
          <p className={loadedP1 ? "show" : ""}>여행의 마법에 빠져보세요!</p>
          <p className={loadedP1 ? "show" : ""}>
            <Link>
              <strong>
                D<span>o</span>gG<span>o</span>
              </strong>
            </Link>{" "}
            에서 도움을 드리겠습니다
          </p>
        </div>
      </div>
    </div>
  );
}

export default Main1;
