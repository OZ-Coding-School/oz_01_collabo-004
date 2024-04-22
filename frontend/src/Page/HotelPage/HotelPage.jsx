import React from "react";
import HotelItem from "./HotelItem";
import "./HotelPage.css";

const HotelPage = () => {
  const hotelSpots = [
    {
      id: "1",
      name: "귤빛 캠핑장",
      description: "조천읍 함와로 428",
      link: "http://www.jeju-camping.com/",
      image: "/images/hotelImages/gyullight.png",
    },
    {
      id: "2",
      name: "금능 이큐 스테이 호텔",
      description: "함림읍 금능리 1258",
      link: "https://blog.naver.com/jt_home",
      image: "/images/hotelImages/geumneng.png",
    },

    {
      id: "3",
      name: "더칠린",
      description: "애월읍 애월리 2115-5",
      link: "https://www.instagram.com/the._.chillin",
      image: "/images/hotelImages/thechilin.png",
    },
    {
      id: "4",
      name: "디어 마이 프렌즈",
      description: "한경면 청수리 1466-2",
      link: "https://pf.kakao.com/_IxoVxes",
      image: "/images/hotelImages/dear.png",
    },
    {
      id: "5",
      name: "멍멍 플레이스",
      description: "애월읍 소길리 952-2",
      link: "https://www.instagram.com/jeju__mmplays",
      image: "/images/hotelImages/mungmung.png",
    },
    {
      id: "6",
      name: "소노벨 제주",
      description: "조천읍 함덕리 274",
      link: "https://www.sonohotelsresorts.com/hd/",
      image: "/images/hotelImages/sonobel.png",
    },
    {
      id: "7",
      name: "에퀴녹스 드 협재",
      description: "한림읍 협재로 210-55",
      link: "https://blog.naver.com/jt_home",
      image: "/images/hotelImages/aquenos.png",
    },
    {
      id: "8",
      name: "엔젤 하우스",
      description: "애월읍 고내리 11-1",
      link: "https://angelhouse.kr/m/index.php",
      image: "/images/hotelImages/angel.png",
    },
    {
      id: "9",
      name: "엠버 퓨어 힐 호텔 & 리조트",
      description: "노형동 산 13",
      link: "https://amberpurehill.com",
      image: "/images/hotelImages/purehill.png",
    },
    {
      id: "10",
      name: "오롯 바이 에퀴녹스",
      description: "한림읍 금능리 1417",
      link: "https://blog.naver.com/jt_home",
      image: "/images/hotelImages/orotby.png",
    },
    {
      id: "11",
      name: "옵데 가바이 에퀴녹스",
      description: "한림읍 협재10길 4",
      link: "https://blog.naver.com/jt_home",
      image: "/images/hotelImages/opde.png",
    },
    {
      id: "12",
      name: "유수암 캠핑장",
      description: "애월읍 유수암리 2994",
      link: "https://m.place.naver.com/accommodation/1315382283/home?entry=plt&businessCategory=camping",
      image: "/images/hotelImages/usooam.png",
    },
    {
      id: "13",
      name: "제주 애 물들다",
      description: "한경면 고조로 492-8",
      link: "https://jejulovestay.modoo.at",
      image: "/images/hotelImages/mooldel.png",
    },
    {
      id: "14",
      name: "제주 애 빛나다",
      description: "한경면 고조로 492-6",
      link: "https://jejulovestay.modoo.at",
      image: "/images/hotelImages/jejulight.png",
    },
    {
      id: "15",
      name: "제주 애 설레다",
      description: "한경면 조수리 492-4",
      link: "https://jejulovestay.modoo.at",
      image: "/images/hotelImages/jejue.png",
    },
    {
      id: "16",
      name: "크리스마스 리조트",
      description: "구좌읍 종달리 1422",
      link: "http://christmasresort.kr/",
      image: "/images/hotelImages/crithmas.png",
    },
    {
      id: "17",
      name: "하늘오름 펜션",
      description: "구좌읍 덕천리 1325",
      link: "http://skyoreum.com",
      image: "/images/hotelImages/skyorem.png",
    },
    {
      id: "18",
      name: "하이제주 호텔",
      description: "한립읍 협재리 1165",
      link: "http://hijejuhotel.co.kr",
      image: "/images/hotelImages/hijeju.png",
    },
    {
      id: "19",
      name: "한화리조트 제주",
      description: "회천동 3-16",
      link: "http://www.hanwharesort.co.kr/",
      image: "/images/hotelImages/hanhwa.png",
    },
    {
      id: "20",
      name: "고성2119펜션 위플레이독",
      description: "https://blog.naver.com/mjjinu",
      link: "https://www.gosung2119.com/",
      image: "/images/hotelImages/weplay.png",
    },
    {
      id: "21",
      name: "그림그리는 펜션",
      description: "성산읍 수산리 3342-6",
      link: "http://artpension.fortour.kr/",
      image: "/images/hotelImages/grimgrin.png",
    },
    {
      id: "22",
      name: "라임 오렌지빌",
      description: "토평동 416",
      link: "https://limevil.co.kr/",
      image: "/images/hotelImages/lime.png",
    },
  ];

  return (
    <div className="hotel-page">
      <h2 style={{ textAlign: "center", margin: "30px" }}>
        반려 동물과 함께 할 추천 호텔
      </h2>
      <div className="hotel-box">
        {hotelSpots.map((spot) => (
          <HotelItem key={spot.id} spot={spot} />
        ))}
      </div>
    </div>
  );
};

export default HotelPage;
