import React, { useEffect, useState } from "react";
import axios from "../../api/axios";
import "./Coupon.css";

const PaymentCoupon = () => {
  const [couponInfo, setCouponInfo] = useState([]);
  const [loading, setLoading] = useState(true);

  // 쿠폰 정보 가져오는 함수
  const getCouponInfo = async () => {
    try {
      const response = await axios.get("/api/v1/coupon/mycoupon", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });

      if (response.status === 200) {
        const data = response.data;
        setCouponInfo(data);
        console.log("coupon", response.data);
      }
    } catch (error) {
      console.log("쿠폰 정보를 불러오는 데 실패했습니다:", error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getCouponInfo();
  }, []);

  return (
    <div className="mypage-payment-coupon-container">
      <h3>쿠폰정보</h3>
      <div className="mypage-payment-coupon-info">
        <div className="paymentCoupons">
          {couponInfo.map((item, index) => (
            <div key={index} className="paymentCoupon">
              <div className="maypage-paymentcoupon-box">
                <div className="maypage-paymentcoupon">
                  <div className="maypage-paymentcoupon-image">
                    <h5>할인금액</h5>
                    <h5> - ₩{item.coupon_info.sale_price}원</h5>
                    <h5>{item.coupon_info.content}</h5>
                  </div>
                  <div className="maypage-paymentcoupon-bottom">
                    <div className="dotted"></div>
                    <p>유효 기간</p>
                    <p>{item.expired_at}</p>
                    <p>만료일 : {item.coupon_info.duration}일</p>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default PaymentCoupon;
