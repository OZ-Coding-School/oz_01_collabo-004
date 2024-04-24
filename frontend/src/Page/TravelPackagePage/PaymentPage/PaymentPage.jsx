import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import CouponInfoComponent from "../../../Component/PaymentCoupon/PaymentCoupon";
import PaymentPageModal from "../../../Component/PaymentPageModal/PaymentPageModal";
import axios from "../../../api/axios";
import "./PaymentPage.css";

function PaymentPage() {
  const location = useLocation();
  const travelData = location?.state?.travelData;
  const posttravelData = location?.state?.posttravelData;
  const totalPricepay = location?.state?.totalPrice;

  const [departureDate, setDepartureDate] = useState(posttravelData?.departureDate);
  const [numberOfPeople, setNumberOfPeople] = useState(posttravelData?.numberOfPeople);
  const [smallPetsCount, setSmallPetsCount] = useState(posttravelData?.smallPetsCount);
  const [mediumPetsCount, setMediumPetsCount] = useState(posttravelData?.mediumPetsCount);
  const [largePetsCount, setLargePetsCount] = useState(posttravelData?.largePetsCount);
  const navigate = useNavigate();

  const handleBack = () => {
    navigate(-1); //뒤로가기
  };


const handlePayment = async (e) => {
    e.preventDefault();
    const paymentData = {
        departure_date:departureDate,
        people:numberOfPeople,
        pet_size_small:smallPetsCount,
        pet_size_medium:mediumPetsCount,
        pet_size_big: largePetsCount,
        user_coupon_id: 1
    };
    try {
      const response = await axios.post("/api/v1/order/", {
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(paymentData),
      });

      if (!response.ok) {
        throw new Error("서버 응답 실패");
      }

      const responseData = await response.json();
      console.log("서버 응답:", responseData);
    } catch (error) {
      console.error("서버 요청 실패:", error.message);
    }
  };

  const [, setShowPaymentInputs] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const totalPrice = () => {
    const basePrice = totalPricepay;
    const personPrice = numberOfPeople * 15000;
    const smallPetPrice = smallPetsCount * 6000;
    const mediumPetPrice = mediumPetsCount * 10000;
    const largePetPrice = largePetsCount * 15000;
    return (
      basePrice + personPrice + smallPetPrice + mediumPetPrice + largePetPrice
    );
  };

  const handleNumberOfPeopleChange = (amount) => {
    setNumberOfPeople((prevCount) => Math.max(1, prevCount + amount));
  };

  const handleSmallPetsChange = (amount) => {
    setSmallPetsCount((prevCount) => Math.max(0, prevCount + amount));
  };

  const handleMediumPetsChange = (amount) => {
    setMediumPetsCount((prevCount) => Math.max(0, prevCount + amount));
  };

  const handleLargePetsChange = (amount) => {
    setLargePetsCount((prevCount) => Math.max(0, prevCount + amount));
  };

  const toggleModal = () => {
    setIsModalOpen((prev) => !prev);
  };

  const handleSubmitChanges = () => {
    toggleModal();
    setShowPaymentInputs(false);
  };
  return (

    <div className="paymentpage-container">

      <div className="paymentpage-des">
        {travelData ? (
          <div>
            <h2>{travelData.name}</h2>
            <img
              src={travelData.product_img}
              alt="상품 이미지"
              className="paymentpage-img"
            />
            <hr />
            <h4>상세요금</h4>
            <h5>
              패키지 요금
              <span>₩{Number(travelData.price).toLocaleString()}원</span>
            </h5>
            <h5>
              추가 인원
              <span>₩{(numberOfPeople * 15000).toLocaleString()}원</span>
            </h5>
            <h5>
              추가 반려견<span>₩{(
                  smallPetsCount * 6000 +
                  mediumPetsCount * 10000 +
                  largePetsCount * 15000).toLocaleString()}원</span>
            </h5>
            <hr />
            <h5>
              총 합계(KRW)<span>₩{totalPrice().toLocaleString()}원</span>
            </h5>
            <p>저희 "DogGO" 를 이용해주셔서 감사합니다.</p>
          </div>
        ) : (
          <p>상품 정보를 불러오는 중입니다...</p>
        )}
      </div>

      <form
        className="paymentpage-form">
        <h2>
        <span className="material-symbols-outlined" onClick={handleBack}
        >undo</span>확인 및 결제</h2>
        
        <h3>예약정보</h3>
        <label>출발일</label>
        <input
          type="date"
          id="departureDate"
          value={departureDate}
          onChange={(e) => setDepartureDate(e.target.value)}
        />

        <div className="paymentpage-input">
          <div className="paymentpage-totalprice">
            <p>인원 / 반려동물</p>
            <p>
              {numberOfPeople}명 /{" "}
              {smallPetsCount + mediumPetsCount + largePetsCount} 마리
              <div className="paymentpage-input-btn">
              <button type="button" onClick={toggleModal}>
                수정하기
              </button>
              </div>
            </p>
            <CouponInfoComponent />
          </div>
        </div>

        <hr />
      <div className="paymentpage-form-info">
      <h3>환불정책</h3>
      <p>패키지구매 일 주일전까지 무료로 취소하실 수 있습니다.</p>
      <p>당일예약 취소시 50%의 수수료가 발생합니다</p>
      </div>
      <hr />
      <div className="paymentpage-form-totalpaybtn">
      <button type="submit"
          onClick={handlePayment}>예약확정</button>
      </div>
      </form>

      <PaymentPageModal
        isOpen={isModalOpen}
        onClose={toggleModal}
        className="paymentpage-check-modal"
      >
        <div className="paymentpage-check">
          <label>인원 수</label>
          <div className="paymentpage-check_control">
            <button
              type="button"
              onClick={() => handleNumberOfPeopleChange(-1)}
            >
              -
            </button>
            <span> {numberOfPeople} 명</span>
            <button type="button" onClick={() => handleNumberOfPeopleChange(1)}>
              +
            </button>
          </div>
        </div>

        <div className="paymentpage-check">
          <label>반려동물 소</label>
          <div className="paymentpage-check_control">
            <button type="button" onClick={() => handleSmallPetsChange(-1)}>
              -
            </button>
            <span>{smallPetsCount} 마리</span>
            <button type="button" onClick={() => handleSmallPetsChange(1)}>
              +
            </button>
          </div>
        </div>

        <div className="paymentpage-check">
          <label>반려동물 중</label>
          <div className="paymentpage-check_control">
            <button type="button" onClick={() => handleMediumPetsChange(-1)}>
              -
            </button>
            <span>{mediumPetsCount} 마리</span>
            <button type="button" onClick={() => handleMediumPetsChange(1)}>
              +
            </button>
          </div>
        </div>

        <div className="paymentpage-check">
          <label>반려동물 대</label>
          <div className="paymentpage-check_control">
            <button type="button" onClick={() => handleLargePetsChange(-1)}>
              -
            </button>
            <span>{largePetsCount} 마리</span>
            <button type="button" onClick={() => handleLargePetsChange(1)}>
              +
            </button>
          </div>
        </div>
        <hr />
        <div className="paymentpage-check-storage">
          <button onClick={handleSubmitChanges}>저장</button>
        </div>
      </PaymentPageModal>
    </div>
  );
}

export default PaymentPage;
