import React, { useState } from "react";
import { Button, Form } from "react-bootstrap";

const PaymentPage = () => {
  const [cardNumber, setCardNumber] = useState("");
  const [expiryDate, setExpiryDate] = useState("");
  const [cvv, setCvv] = useState("");
  const [name, setName] = useState("");

  const handlePayment = () => {
    // 여기서 결제를 처리하는 로직을 작성합니다.
    console.log("Payment processing...");
  };

  return (
    <div className="container mt-5">
      <h2>결제 정보 입력</h2>
      <Form>
        <Form.Group controlId="formCardNumber">
          <Form.Label>카드 번호</Form.Label>
          <Form.Control
            type="text"
            placeholder="카드 번호를 입력하세요"
            value={cardNumber}
            onChange={(e) => setCardNumber(e.target.value)}
          />
        </Form.Group>
        <Form.Group controlId="formExpiryDate">
          <Form.Label>만료일</Form.Label>
          <Form.Control
            type="text"
            placeholder="MM/YYYY 형식으로 입력하세요"
            value={expiryDate}
            onChange={(e) => setExpiryDate(e.target.value)}
          />
        </Form.Group>
        <Form.Group controlId="formCvv">
          <Form.Label>CVV</Form.Label>
          <Form.Control
            type="text"
            placeholder="CVV를 입력하세요"
            value={cvv}
            onChange={(e) => setCvv(e.target.value)}
          />
        </Form.Group>
        <Form.Group controlId="formName">
          <Form.Label>카드 소유자 이름</Form.Label>
          <Form.Control
            type="text"
            placeholder="이름을 입력하세요"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </Form.Group>
        <Button variant="primary" onClick={handlePayment}>
          결제하기
        </Button>
      </Form>
    </div>
  );
};

export default PaymentPage;
