import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import CouponInfoComponent from "../../../Component/PaymentCoupon/PaymentCoupon";
import PaymentPageModal from "../../../Component/PaymentPageModal/PaymentPageModal";
import axios from "../../../api/axios";
import "./PaymentPage.css";

function PaymentPage() {
  const location = useLocation();
  const [couponId, setCouponId] = useState(0);

  const travelData = location?.state?.travelData;
  const posttravelData = location?.state?.posttravelData;
  const totalPricepay = location?.state?.totalPrice;

  const [couponiconClicked, setICouponiconClicked] = useState(false);
  const [departureDate, setDepartureDate] = useState(
    posttravelData?.departureDate
  );
  const [numberOfPeople, setNumberOfPeople] = useState(
    posttravelData?.numberOfPeople
  );
  const [smallPetsCount, setSmallPetsCount] = useState(
    posttravelData?.smallPetsCount
  );
  const [mediumPetsCount, setMediumPetsCount] = useState(
    posttravelData?.mediumPetsCount
  );
  const [largePetsCount, setLargePetsCount] = useState(
    posttravelData?.largePetsCount
  );
  const [paymentCoupon, setPaymentCoupon] = useState(0);
  const navigate = useNavigate();
  const couponPrice =
    paymentCoupon.id !== 0 && couponiconClicked
      ? paymentCoupon.coupon_info.sale_price
      : 0;

  const handleBack = () => {
    navigate(-1); //뒤로가기
  };

  const handlePayment = async (e) => {
    e.preventDefault();

    const paymentData = {
      product: location.state.productId,
      departure_date: departureDate,
      people: numberOfPeople,
      pet_size_small: smallPetsCount,
      pet_size_medium: mediumPetsCount,
      pet_size_big: largePetsCount,
    };
    if (couponiconClicked && couponPrice.id !== 0) {
      paymentData.user_coupon_id = paymentCoupon.id;
    }
    try {
      const response = await axios.post(`/api/v1/order/`, paymentData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });

      if (response.status === 201) {
        alert("예약이완료 되었습니다!");
        navigate("/travel");
      }
    } catch (error) {}
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
      basePrice +
      personPrice +
      smallPetPrice +
      mediumPetPrice +
      largePetPrice -
      couponPrice
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
              추가 반려견
              <span>
                ₩
                {(
                  smallPetsCount * 6000 +
                  mediumPetsCount * 10000 +
                  largePetsCount * 15000
                ).toLocaleString()}
                원
              </span>
            </h5>
            <h5>
              쿠폰
              <span>
                {couponPrice === 0 ? "" : "-"} ₩
                {Number(couponPrice).toLocaleString()}원
              </span>
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

      <form className="paymentpage-form">
        <h2>
          <span
            className="material-symbols-outlined paymentpage-goback-btn"
            onClick={handleBack}
          >
            undo
          </span>
          확인 및 결제
        </h2>
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
            <h4>인원 / 반려동물</h4>
            <p>
              {numberOfPeople}명 /{" "}
              {smallPetsCount + mediumPetsCount + largePetsCount} 마리
              <div className="paymentpage-input-btn">
                <button type="button" onClick={toggleModal}>
                  수정하기
                </button>
              </div>
            </p>
            <CouponInfoComponent
              paymentCoupon={paymentCoupon}
              setPaymentCoupon={setPaymentCoupon}
              couponiconClicked={couponiconClicked}
              setICouponiconClicked={setICouponiconClicked}
            />
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
          <button type="submit" onClick={handlePayment}>
            예약확정
          </button>
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
