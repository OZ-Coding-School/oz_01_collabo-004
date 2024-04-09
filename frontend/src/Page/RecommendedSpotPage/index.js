import React from "react";
import RecommendationItem from "./RecommendationItem";
import "./index.css";

const RecommendedSpotPage = () => {
  const recommendedSpots = [
    {
      name: "도치돌 알파카 목장",
      description: "제주시 애월읍 납읍리 98-1",
      link: "https://www.alpacajeju.com/",
      image: "/images/recommendedImages/도치돌목장.png",
    },
    {
      name: "돌하르방 미술관",
      description: "조천읍 북촌서 1길 70",
      link: "https://www.visitjeju.net/kr/detail/view?contentsid=CONT_000000000500150",
      image: "/images/recommendedImages/돌하르방미술관.png",
    },

    {
      name: "메이즈랜드",
      description: "구좌읍 평대리 3322",
      link: "https://mazeland.co.kr/kor/",
      image: "/images/recommendedImages/메이즈랜드.png",
    },
    {
      name: "방림원",
      description: "한경면 용금로 864",
      link: "http://banglimwon.com/",
      image: "/images/recommendedImages/방림원.png",
    },
    {
      name: "비체올린",
      description: "한경면 판포리 725-1",
      link: "http://www.vicheollin.com/index.php",
      image: "/images/recommendedImages/비체올린.png",
    },
    {
      name: "생각하는 정원",
      description: "한경면 저지리 1534",
      link: "https://spiritedgarden.com",
      image: "/images/recommendedImages/생각하는 정원.png",
    },
    {
      name: "서프라이즈 테마파크",
      description: "조천읍 와흘리 2988",
      link: "https://surprisethemepark.lscompany2014.com/",
      image: "/images/recommendedImages/서프라이즈.png",
    },
    {
      name: "성이시 돌목장",
      description: "한림읍 금악리 116",
      link: "https://www.visitjeju.net/kr/detail/view?contentsid=CNTS_200000000008053",
      image: "/images/recommendedImages/성이시돌목장.jpeg",
    },
    {
      name: "스누피 가든",
      description: "구좌읍 금백조로 930",
      link: "https://www.snoopygarden.com/",
      image: "/images/recommendedImages/스누피가든.png",
    },
    {
      name: "아침미소 목장",
      description: "첨단동길 160-20",
      link: "https://morningsmile.modoo.at/",
      image: "/images/recommendedImages/아침미소목장.png",
    },
    {
      name: "월령선인장 군락지",
      description: "한림읍 월령리 359-4",
      link: "https://www.visitjeju.net/kr/detail/view?contentsid=CONT_000000000500494",
      image: "/images/recommendedImages/월령선인장.jpeg",
    },
    {
      name: "제주고산리 유적",
      description: "한경면 노을해안로 1100",
      link: "https://gosanriyujeok.co.kr/",
      image: "/images/recommendedImages/제주고산리.png",
    },
    {
      name: "제주 레일 바이크",
      description: "구좌읍 용눈이오름로 641",
      link: "https://www.visitjeju.net/kr/detail/view?contentsid=CNTS_000000000020139",
      image: "/images/recommendedImages/레일바이크.jpeg",
    },
    {
      name: "제주 레포츠 랜드",
      description: "조천읍 와흘리 870",
      link: "http://www.leportsland.kr/main/main.php",
      image: "/images/recommendedImages/레포츠랜드.jpeg",
    },
    {
      name: "제주 불빛정원",
      description: "애월읍 평화로 2346",
      link: "https://www.visitjeju.net/kr/detail/view?contentsid=CNTS_000000000022082",
      image: "/images/recommendedImages/불빛정원.jpeg",
    },
    {
      name: "차귀도 유람선",
      description: "한경면 노을해안로 1160",
      link: "https://chagwido.modoo.at/",
      image: "/images/recommendedImages/차귀도유람선.png",
    },
    {
      name: "한림공원",
      description: "한림읍 한림로 300",
      link: "https://hallimpark.com/",
      image: "/images/recommendedImages/한림공원.jpeg",
    },
    {
      name: "노리매 공원",
      description: "대정읍 구억리 654-1",
      link: "https://www.visitjeju.net/kr/detail/view?contentsid=CNTS_000000000018415",
      image: "/images/recommendedImages/노리매.jpeg",
    },
    {
      name: "드르쿰다 in 성산",
      description: "성산읍 고성리 372-1",
      link: "https://delekoomdainsungsan.modoo.at/",
      image: "/images/recommendedImages/드르쿰다.jpeg",
    },
    {
      name: "목장 카페 드르쿰다",
      description: "표선면 성읍리 2873",
      link: "https://delekoomda.modoo.at/",
      image: "/images/recommendedImages/목장카페.jpeg",
    },
    {
      name: "보롬왓",
      description: "표선면 성읍리 3229-4",
      link: "https://www.visitjeju.net/kr/detail/view?contentsid=CNTS_000000000020050",
      image: "/images/recommendedImages/보롬왓.jpeg",
    },
    {
      name: "목장 카페 드르쿰다",
      description: "표선면 성읍리 2873",
      link: "https://delekoomda.modoo.at/",
      image: "/images/recommendedImages/목장카페.jpeg",
    },
    {
      name: "목장 카페 드르쿰다",
      description: "표선면 성읍리 2873",
      link: "https://delekoomda.modoo.at/",
      image: "/images/recommendedImages/목장카페.jpeg",
    },
    {
      name: "목장 카페 드르쿰다",
      description: "표선면 성읍리 2873",
      link: "https://delekoomda.modoo.at/",
      image: "/images/recommendedImages/목장카페.jpeg",
    },
    {
      name: "목장 카페 드르쿰다",
      description: "표선면 성읍리 2873",
      link: "https://delekoomda.modoo.at/",
      image: "/images/recommendedImages/목장카페.jpeg",
    },
    {
      name: "목장 카페 드르쿰다",
      description: "표선면 성읍리 2873",
      link: "https://delekoomda.modoo.at/",
      image: "/images/recommendedImages/목장카페.jpeg",
    },
  ];

  return (
    <div className="recommended-spot-page">
      <h2>반려 동반 추천 여행지</h2>
      {recommendedSpots.map((spot, index) => (
        <RecommendationItem key={index} spot={spot} />
      ))}
    </div>
  );
};

export default RecommendedSpotPage;
