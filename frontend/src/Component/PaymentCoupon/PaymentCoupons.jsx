import React from "react";
import "./PaymentCoupons.css";

function PaymentCoupon({ item }) {

  return (
    <div className="paymentcoupon-box">
      <div className="paymentcoupon">
        <div className="paymentcoupon-image">
          <h5>할인금액</h5>
          <h5> - ₩{item.coupon_info.sale_price}원</h5>
          <h5>{item.coupon_info.content}</h5>
        </div>
        <div className="paymentcoupon-bottom">
          <div className="dotted"></div>
          <p>유효 기간</p>
          <p>{item.expired_at}</p>
          <p>만료일 : {item.coupon_info.duration}일</p>
        </div>
      </div>
    </div>
  );
}

export default PaymentCoupon;
// <p>{item.coupon_info.content}</p>
// <p>할인금액 : -₩ {item.coupon_info.sale_price}원</p>
// <p></p>
// <p>유효 기간</p>
// <p>{item.expired_at}</p>
// <button type='button'>적용하기</button>