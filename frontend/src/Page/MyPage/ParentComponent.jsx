import React, { useState } from "react";
import Profile from "./Profile";

function ParentComponent() {
  const [coupons, setCoupons] = useState([]);

  const handleReceiveCoupon = (coupon) => {
    setCoupons([...coupons, coupon]);
  };

  return <Profile onReceiveCoupon={handleReceiveCoupon} />;
}

export default ParentComponent;
