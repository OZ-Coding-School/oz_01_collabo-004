import React from "react";
import axios from "./axios";

const Test = () => {
  const getData = async () => {
    try {
      const response = await axios.post("");
      console.log(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div>
      <button onClick={getData}>보내기</button>
    </div>
  );
};

export default Test;
