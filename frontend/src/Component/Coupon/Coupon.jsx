import React, { useEffect, useState } from 'react';
import axios from '../../api/axios';

const CouponInfoComponent = ({ token }) => {
  const [couponInfo, setCouponInfo] = useState(null); //쿠폰정보저장
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCouponInfo = async () => {
      try {
        const response = await axios.get('/api/v1/coupon/mycoupon', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        });

        if (response.status === 200) {
          const data = response.data;
          setCouponInfo(data);
        }
      } catch (error) {
        console.log('쿠폰 정보를 불러오는 데 실패했습니다:', error.message);
          setLoading(false);
      }
    console.log('coupon',couponInfo)
    };

    fetchCouponInfo();
  }, [token]);

  return (
    <div>
      {loading ? (
        <p>쿠폰 정보를 불러오는 중...</p>
      ) : (
        <div>
          {couponInfo ? (
            <div>
              <h3>쿠폰 정보</h3>
              <p>쿠폰 코드: {couponInfo.coupon_info.sale_price}</p>
              <p>할인율: {couponInfo.discountPercentage}</p>
            </div>
          ) : (
            <p>쿠폰 정보가 없습니다.</p>
          )}
        </div>
      )}
    </div>
  );
};

export default CouponInfoComponent;
