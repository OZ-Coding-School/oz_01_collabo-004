import React from "react";
import axios from "../../../api/axios";
import "./Main3.css";

function Main3() {
  const postCoupon = async () => {
    try {
      const response = await axios.post(`/api/v1/coupon/issue/`);
      if (response.status === 200) {
        console.log("쿠폰이 성공적으로 발급되었습니다!");
      } else {
        throw new Error("서버 응답 실패");
      }
    } catch (error) {
      console.error("쿠폰 발급 요청 실패:", error.message);
    }
  };
  return (
    <div className="Main3-contanier">
      <div className="image_box_01">
        <div className="WC">
          <button onClick={postCoupon}>₩50,000</button>
        </div>
        <div className="WC2">
        </div>
      </div>
      <div className="image_box_02"></div>
      {/* <div className="image_box_03"></div> */}
    </div>
  );
}

export default Main3;
