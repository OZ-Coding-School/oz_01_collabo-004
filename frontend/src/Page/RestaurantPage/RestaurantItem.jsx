import React from "react";
import RestaurantPage from "./RestaurantPage";
import "./RestaurantPage.css";

const RestaurantItem = () => {
  const restaurantSpots = [
    {
      id: "1",
      name: "513 텐동",
      description: "테우해안로 46 2층",
      link: "https://m.place.naver.com/restaurant/1466059040/home?entry=pll",
      image: "/images/restaurantImages/513tendong.png",
    },
    {
      id: "2",
      name: "그초록",
      description: "구좌읍 행원리 1485",
      link: "https://m.place.naver.com/restaurant/38411991/home?entry=plt",
      image: "/images/restaurantImages/green.png",
    },
    {
      id: "3",
      name: "금능제면소",
      description: "한림읍 금능리 1361",
      link: "https://m.place.naver.com/restaurant/1245704097/home?entry=pll",
      image: "/images/restaurantImages/jemyunso.png",
    },
    {
      id: "4",
      name: "금요일의 아침 조금",
      description: "가령골 1길 12",
      link: "https://www.instagram.com/friday_morning_",
      image: "/images/restaurantImages/friday.png",
    },
    {
      id: "5",
      name: "김만덕 객주",
      description: "임항로 68",
      link: "https://www.diningcode.com/profile.php?rid=MThJ1zlDJAql",
      image: "/images/restaurantImages/mandeuk.png",
    },
    {
      id: "6",
      name: "깅코",
      description: "도령로 100",
      link: "https://www.instagram.com/cafe_ginkgo",
      image: "/images/restaurantImages/gingko.png",
    },
    {
      id: "7",
      name: "너는 파라다이스 길리",
      description: "구좌읍 월정1길 65",
      link: "http://www.instagram.com/paradise_gili_in_jeju",
      image: "/images/restaurantImages/gilli.png",
    },
    {
      id: "8",
      name: "니모메빈티지라운지",
      description: "외도이동 341-2",
      link: "http://www.instagram.com/nimome_jeju",
      image: "/images/restaurantImages/nimo.png",
    },
    {
      id: "9",
      name: "다니쉬",
      description: "조천읍 함덕리 1250",
      link: "http://www.instagram.com/danish_jeju/",
      image: "/images/restaurantImages/danish.png",
    },
    {
      id: "10",
      name: "달이뜨는식탁",
      description: "구좌읍 월정리 885",
      link: "https://dalsiktakjeju.modoo.at",
      image: "/images/restaurantImages/moon.png",
    },
    {
      id: "11",
      name: "더 펫츠",
      description: "1100로 3124 2층",
      link: "http://www.jejupet.com/",
      image: "/images/restaurantImages/pets.png",
    },
    {
      id: "12",
      name: "도을",
      description: "조천읍 와흘리 125",
      link: "http://instagram.com/_do_eul_",
      image: "/images/restaurantImages/doel.png",
    },
    {
      id: "13",
      name: "돈파스타 정원",
      description: "애월읍 애월해안로 364",
      link: "http://0647993336.tshome.co.kr/",
      image: "/images/restaurantImages/donpasta.png",
    },
    {
      id: "14",
      name: "돌담넘는고양이",
      description: "구좌읍 종달리 722",
      link: "https://www.instagram.com/jeju.sol/",
      image: "/images/restaurantImages/cats.png",
    },
    {
      id: "15",
      name: "동명정류장",
      description: "한림읍 동명7길 26",
      link: "http://instagram.com/jeju_dm",
      image: "/images/restaurantImages/dongmyung.png",
    },
    {
      id: "16",
      name: "돼지 굽는 정원",
      description: "한림읍 협재리 2528",
      link: "http://www.instagram.com/pig9840",
      image: "/images/restaurantImages/pigpark.png",
    },
    {
      id: "17",
      name: "라트반",
      description: "구좌읍 하도리 3078-4",
      link: "https://m.place.naver.com/restaurant/1721326180/home?entry=plt",
      image: "/images/restaurantImages/ratbun.png",
    },
    {
      id: "18",
      name: "러블리 독스",
      description: "이도이동 122-1",
      link: "https://m.place.naver.com/place/1487550510/home?entry=pll",
      image: "/images/restaurantImages/dogs.png",
    },
    {
      id: "19",
      name: "레이지 펌프",
      description: "애월읍 애월북서길 32",
      link: "http://instagram.com/lazy_pump",
      image: "/images/restaurantImages/raze.png",
    },
    {
      id: "20",
      name: "르카페 하도",
      description: "구좌읍 종달리 1422",
      link: "https://m.place.naver.com/restaurant/1454969983/home?entry=plt",
      image: "/images/restaurantImages/recafe.png",
    },
    {
      id: "21",
      name: "리치망고 애월본점",
      description: "애월읍 애월해안로 272",
      link: "http://www.instagram.com/jejurichmango",
      image: "/images/restaurantImages/rich.png",
    },
    {
      id: "22",
      name: "마음에온",
      description: "일도일동 1301-4",
      link: "http://www.instagram.com/oncafe0707",
      image: "/images/restaurantImages/maeume.png",
    },
  ];

  return (
    <div className="restaurant-page">
      <h2> Restaurant With Pet </h2>
      <div className="restaurant-box">
        {restaurantSpots.map((spot) => (
          <RestaurantPage key={spot.id} spot={spot} />
        ))}
      </div>
    </div>
  );
};

export default RestaurantItem;
