import React, { useEffect, useState } from 'react';
import axios from '../../api/axios';
import './PaymentCoupon.css';

const PaymentCoupon = ({setPaymentCoupon,paymentCoupon}) => {
  const [couponInfo, setCouponInfo] = useState([]);
  const [loading, setLoading] = useState(true); 
  const [showCoupon, setShowCoupon] = useState(false);
  
  // 쿠폰 정보 가져오는 함수
  const getCouponInfo = async () => {
    try {
      const response = await axios.get('/api/v1/coupon/mycoupon', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      });
      console.log(response)
      if (response.status === 200) {
        const data = response.data;
        setCouponInfo(data);
        setPaymentCoupon(data[0].id);
        console.log('coupon', response.data);
      }
    } catch (error) {
      console.log('쿠폰 정보를 불러오는 데 실패했습니다:', error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getCouponInfo();
  }, []);

  // 쿠폰 정보 토글 함수
  const toggleCouponInfo = () => {
    setShowCoupon(!showCoupon); 
  };
  
  const formatDate = (dateTimeString) => {
  // 주어진 날짜 문자열을 Date 객체로 변환
  const date = new Date(dateTimeString);

  // Date 객체에서 원하는 형식으로 날짜 및 시간 추출
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0'); // 월은 0부터 시작하므로 +1
  const day = String(date.getDate()).padStart(2, '0');
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  const seconds = String(date.getSeconds()).padStart(2, '0');

  // 포맷팅된 날짜와 시간 문자열 반환 (예: "2024-05-24T00:37:39")
  return `${year}-${month}-${day} / ${hours}시:${minutes}분`;
};

// 사용 예시
const originalDateTimeString = "2024-05-24T00:37:39.068413+09:00";
const formattedDateTimeString = formatDate(originalDateTimeString);
console.log(formattedDateTimeString); // "2024-05-24T00:37:39"

  return (
    <div className='payment-coupon-container'>
      <h4>쿠폰정보</h4>
      <div className='payment-coupon-container-btn'>
      <button type='button' onClick={toggleCouponInfo}>
      {showCoupon ? '쿠폰숨기기' : '쿠폰보기'}
      </button>
      </div>
      {showCoupon && (
      <div className='payment-coupon-info'>
          <div className='paymentCoupons'>
            {couponInfo.map((item, index) => (
              <div key={index}
              className='paymentCoupon'
              >
      <div className="paymentcoupon-box">
          <div className="paymentcoupon">
            <div className='paymentcoupon-title'>
            <h5>₩{Number(item.coupon_info.sale_price).toLocaleString()}원 할인쿠폰</h5>
            <p>{item.coupon_info.content}</p>
            </div>
          <div className="paymentcoupon-bottom">
          <div className="paymentcoupon-bottom-info">
            <p>{formatDate(item.expired_at)} 까지</p>
            <p>만료일 : {item.coupon_info.duration}일</p>
          </div>
          <div>
          <img src='./images/쿠폰이미지.jpg' alt='쿠폰이미지' />
          </div>
          </div>
        </div>
      </div>
            </div>
            ))}
          </div>
      </div>
      )}
    </div>
  );
};

export default PaymentCoupon;