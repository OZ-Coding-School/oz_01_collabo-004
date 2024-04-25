import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const LogoutPage = () => {
  const navigate = useNavigate();
  useEffect(() => {
    navigate("/");
  }, []);

  return <div>Logout</div>;
};

export default LogoutPage;
