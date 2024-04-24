import React, { useEffect, useState } from 'react';
import axios from '../../api/axios';
import './PaymentCoupon.css';

const CouponInfoComponent = ({ token }) => {
  const [couponInfo, setCouponInfo] = useState([]);
  const [loading, setLoading] = useState(true); 
  const [showCoupon, setShowCoupon] = useState(false);
  
  // 쿠폰 정보 가져오는 함수
  const fetchCouponInfo = async () => {
    try {
      const response = await axios.get('/api/v1/coupon/mycoupon', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      });

      if (response.status === 200) {
        const data = response.data;
        setCouponInfo(data);
        console.log('coupon', response.data);
      }
    } catch (error) {
      console.log('쿠폰 정보를 불러오는 데 실패했습니다:', error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCouponInfo();
  }, []);

  // 쿠폰 정보 토글 함수
  const toggleCouponInfo = () => {
    setShowCoupon(!showCoupon); 
  };

  return (
    <div className='payment-coupon-container'>
      <p>쿠폰정보</p>
      <div className='payment-coupon-container-btn'>
      <button type='button' onClick={toggleCouponInfo}>
      {showCoupon ? '쿠폰 숨기기' : '쿠폰보기'}
      </button>
      </div>
      {showCoupon && (
        <div className='payment-coupon-info'>
          <div className='paymentCoupons'>
            {couponInfo.map((item, index) => (
              <div key={index}
              className='paymentCoupon'
              >
              <p>{item.coupon_info.content}</p>
              <p>할인금액 : ₩ {item.coupon_info.sale_price}원</p>
              <p></p>
              <p>유효 기간</p>
              <p>{item.expired_at}</p>
              <button type='button'>적용하기</button>
            </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default CouponInfoComponent;
