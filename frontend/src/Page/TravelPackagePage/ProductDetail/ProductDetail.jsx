import React, { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import axios from "../../../api/axios";
import "./ProductDetail.css";

function ProductDetail(props) {
  const location = useLocation();

  const [departureDate, setDepartureDate] = useState("");
  const [numberOfPeople, setNumberOfPeople] = useState(1);
  const [smallPetsCount, setSmallPetsCount] = useState(0);
  const [mediumPetsCount, setMediumPetsCount] = useState(0);
  const [largePetsCount, setLargePetsCount] = useState(0);
  const [showPetSizeInfo, setShowPetSizeInfo] = useState(false);
  const [reviewData, setReviewData] = useState([]);
  const [travelData, setTravelData] = useState({});
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();

  const handleBack = () => {
    navigate(-1); //뒤로가기
  };

  const [posttravelData, setPosttravelData] = useState({
    departureDate: "",
    numberOfPeople: 0,
    smallPetsCount: 0,
    mediumPetsCount: 0,
    largePetsCount: 0,
  });

  const basePrice = travelData.price;
  const PersonToTalPrice = numberOfPeople * 15000;
  const smallPetsTotalPrice = smallPetsCount * 6000;
  const mediumPetsTotalPrice = mediumPetsCount * 10000;
  const largePetsTotalPrice = largePetsCount * 15000;

  let totalPrice = basePrice

  const getTravelDetailData = async () => {
    try {
      const response = await axios.get(`/api/v1/product/${location.state.id}`);
      setTravelData(response.data);
      console.log("상품상세페이지", response);
      setIsLoading(false);
    } catch (error) {
      console.log(error);
    }
  };

  const getReview = async () => {
    try {
      const response = await axios.get(
        `/api/v1/review/product/${location?.state?.id}`
      );
      setReviewData(response.data);
      console.log("리뷰페이지", response);
      console.log("리뷰페이지", response.data.results);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getTravelDetailData();
    getReview();
  }, []);

  const togglePetSizeInfo = () => {
    setShowPetSizeInfo((prevState) => !prevState);
  };

  const [imageUrl, setImageUrl] = useState("");

  useEffect(() => {
    if (travelData && travelData.product_img) {
      setImageUrl(travelData.product_img);
    }
  }, [travelData]);

  const handleDateChange = (e) => {
    setDepartureDate(e.target.value);
    setPosttravelData({
      ...posttravelData,
      departureDate: e.target.value,
    });
  };

const handlePeopleChange = (amount) => {
  const updatedNumberOfPeople = Math.max(0, numberOfPeople + amount);
  setNumberOfPeople(updatedNumberOfPeople);

  const updatedPosttravelData = {
    ...posttravelData,
    numberOfPeople: updatedNumberOfPeople,
  };
  setPosttravelData(updatedPosttravelData);
};

const handlePetsChange = (size, amount) => {
  let updatedPetsCount;
  switch (size) {
    case "small":
      updatedPetsCount = Math.max(0, smallPetsCount + amount);
      setSmallPetsCount(updatedPetsCount);
      break;
    case "medium":
      updatedPetsCount = Math.max(0, mediumPetsCount + amount);
      setMediumPetsCount(updatedPetsCount);
      break;
    case "large":
      updatedPetsCount = Math.max(0, largePetsCount + amount);
      setLargePetsCount(updatedPetsCount);
      break;
    default:
      break;
  }
  const updatedPosttravelData = {
    ...posttravelData,
    [`${size}PetsCount`]: updatedPetsCount,
  };
  setPosttravelData(updatedPosttravelData);
};


  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("출발일:", departureDate);
    console.log("인원수:", numberOfPeople);
    console.log("소 반려동물 수:", smallPetsCount);
    console.log("중 반려동물 수:", mediumPetsCount);
    console.log("대 반려동물 수:", largePetsCount);
  };
  const prouductId = location.state.id;
  const paybutton = () => {
    if (!posttravelData.departureDate) {
      alert("출발일을 선택해주세요!!");
      return;
    } else {
      navigate("/paymentpage", {
        state: {
          travelData,
          posttravelData,
          totalPrice,
          imageUrl,
          prouductId
        },
      });
    }
  };

  console.log("test", posttravelData);
  if (isLoading) return <div>로딩중...</div>;
  console.log(typeof testtotalPrice);
  return (
    <div className="productdetail-page">
      <div className="productdetail-page_contnet">
        <div className="productdetail-page-title">
          <h2>
            <span
              className="material-symbols-outlined"
              onClick={handleBack}
            >
              undo
            </span>
            {travelData.name}
          </h2>
          <img
            src={travelData.product_img}
            alt="상품이미지"
            className="productdetail-page_product-img"
          />
        </div>
        <div className="productdetail-page_contnet_review-content">
          <h3>해당상품 리뷰</h3>
          <div className="productdetail-page_contnet_review">
            <ul>
              {reviewData.map((review, index) => (
                <li key={index}>
                  <p>{review.content}</p>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>

      <div className="productdetail-page2">

        <div className="productdetail-page_contnet_detail">
          <h4>
            {travelData.description_text}
          </h4>
          <hr />
          <img
            src={travelData.description_img}
            alt="상세설명이미지"
            className="description-img"
          />
        </div>

        <div className="reservation-form">
          <h3>패키지 요금 : {Number(travelData.price).toLocaleString()} 원</h3>
          <form onSubmit={handleSubmit}>
            <table>
              <tbody>
                <tr>
                  <td>출발일 : </td>
                  <td>
                    <input
                      type="date"
                      value={departureDate}
                      onChange={handleDateChange}
                      required
                      className="reservation-form-input"
                    />
                  </td>
                </tr>
                <tr>
                  <td>인원 수 : </td>
                  <td>
                    <button
                      onClick={() => handlePeopleChange(-1)}
                      className="counter-button"
                    >
                      -
                    </button>
                    <span>{numberOfPeople}</span>
                    <button
                      onClick={() => handlePeopleChange(1)}
                      className="counter-button"
                    >
                      +
                    </button>
                  </td>
                  
                </tr>
                <tr>
                  <td>반려동물 (소): </td>
                  <td>

                    <button
                      onClick={() => handlePetsChange("small", -1)}
                      className="counter-button"
                    >
                      -
                    </button>

                    <span>{smallPetsCount}</span>
                    <button
                      onClick={() => handlePetsChange("small", 1)}
                      className="counter-button"
                    >
                      +
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>반려동물 (중): </td>
                  <td>
                    <button
                      onClick={() => handlePetsChange("medium", -1)}
                      className="counter-button"
                    >
                      -
                    </button>
                    <span>{mediumPetsCount}</span>
                    <button
                      onClick={() => handlePetsChange("medium", 1)}
                      className="counter-button"
                    >
                      +
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>반려동물 (대): </td>
                  <td>
                    <button
                      onClick={() => handlePetsChange("large", -1)}
                      className="counter-button"
                    >
                      -
                    </button>
                    <span>{largePetsCount}</span>
                    <button
                      onClick={() => handlePetsChange("large", 1)}
                      className="counter-button"
                    >
                      +
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>

            <div className="petcount_add">
              총 : 인원 {numberOfPeople}명 / 반려동물{" "}
              {smallPetsCount + mediumPetsCount + largePetsCount} 마리
            </div>
            <div className="petsize-info">
              <p>
                # 반려동물 요금 및 상세정보{""}
                <span>
                  <button onClick={togglePetSizeInfo}>
                    {showPetSizeInfo ? "간략히" : "자세히"}
                  </button>
                </span>
              </p>

              {showPetSizeInfo && (
                <div>
                  <p>소 : (6000원) 5kg 미만 </p>
                  <p>중 : (10000원) 5kg 이상 ~ 25kg 미만 </p>
                  <p>대 : (15000원) 25kg 이상 </p>
                </div>
              )}
            </div>

            <button
              type="submit"
              className="reservation-btn"
              onClick={paybutton}
            >
              예약하기
            </button>
          </form>
          <div className="reservation-form-info">
          <p>예약 확정 전에는 요금이 청구되지 않습니다.</p>
          <p>모든 상품은 인원수,반려동물의수의 따라 변결될수있습니다.</p>
          </div>
          <hr />
          <p>총 예약 가격 : {
            basePrice+
            PersonToTalPrice +
            smallPetsTotalPrice +
            mediumPetsTotalPrice +
            largePetsTotalPrice} 원</p>
        </div>

      </div>
    </div>
  );
}

export default ProductDetail;
