import React, { useState } from "react";
import { useLocation } from "react-router-dom";

function PaymentPage() {
  const location = useLocation();
  const travelData = location.state.travelData;
  const posttravelData = location.state.posttravelData;
  console.log(location.state);

  const [departureDate, setDepartureDate] = useState("");
  const [numberOfPeople, setNumberOfPeople] = useState(0);
  const [smallPetsCount, setSmallPetsCount] = useState(0);
  const [mediumPetsCount, setMediumPetsCount] = useState(0);
  const [largePetsCount, setLargePetsCount] = useState(0);

  const handlePayment = (e) => {
    e.preventDefault();
    console.log("출발일:", departureDate);
    console.log("인원수:", numberOfPeople);
    console.log("소 반려동물 수:", smallPetsCount);
    console.log("중 반려동물 수:", mediumPetsCount);
    console.log("대 반려동물 수:", largePetsCount);
  };

  const totalPrice = () => {
    const basePrice = travelData?.price || 0;
    const personPrice = numberOfPeople * 15000;
    const smallPetPrice = smallPetsCount * 6000;
    const mediumPetPrice = mediumPetsCount * 10000;
    const largePetPrice = largePetsCount * 15000;
    return (
      basePrice +
      personPrice +
      smallPetPrice +
      mediumPetPrice +
      largePetPrice
    );
  };

  return (
    <div className="payment-page">
      <h2>결제 정보</h2>
      {travelData ? (
        <>
          <p>상품명: {travelData.name}</p>
          <p>가격: {Number(travelData.price).toLocaleString()}원</p>
        </>
      ) : (
        <p>상품 정보를 불러오는 중입니다...</p>
      )}

      <form onSubmit={handlePayment}>
        <label htmlFor="departureDate">출발일:</label>
        <input
          type="date"
          id="departureDate"
          value={posttravelData.departureDate}
          onChange={(e) => setDepartureDate(e.target.value)}
        />

        <label htmlFor="numberOfPeople">인원 수:</label>
        <input
          type="number"
          id="numberOfPeople"
          value={posttravelData.numberOfPeople}
          onChange={(e) => setNumberOfPeople(Number(e.target.value))}
        />

        <label htmlFor="smallPetsCount">소 반려동물 수:</label>
        <input
          type="number"
          id="smallPetsCount"
          value={posttravelData.smallPetsCount}
          onChange={(e) => setSmallPetsCount(Number(e.target.value))}
        />

        <label htmlFor="mediumPetsCount">중 반려동물 수:</label>
        <input
          type="number"
          id="mediumPetsCount"
          value={posttravelData.mediumPetsCount}
          onChange={(e) => setMediumPetsCount(Number(e.target.value))}
        />

        <label htmlFor="largePetsCount">대 반려동물 수:</label>
        <input
          type="number"
          id="largePetsCount"
          value={posttravelData.largePetsCount}
          onChange={(e) => setLargePetsCount(Number(e.target.value))}
        />

        <p>총 예약 가격: {totalPrice().toLocaleString()}원</p>

        <button type="submit">결제하기</button>
      </form>
    </div>
  );
}

export default PaymentPage;
