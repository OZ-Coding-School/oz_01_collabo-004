import React, { useState } from "react";
import axios from "../api/axios";

const Testaa = () => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [productName, setProductName] = useState("");
  const [productImg, setProductImg] = useState("");
  const [descriptionText, setDescriptionText] = useState("");
  const [price, setPrice] = useState(0);
  const [travelPeriod, setTravelPeriod] = useState(0);
  const [discount, setDiscount] = useState(0);
  const [viewCount, setViewCount] = useState(0);
  const [status, setStatus] = useState(true);
  const productId = 6;
  const handleReview = async () => {
    const response = await axios.post(
      "/api/v1/review/",
      {
        title,
        content,
        view_count: 0,
        product: productId,
      },
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
    console.log(response);
  };

  const onChangeUserImg = (e) => {
    const file = e.target.files && e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        setProductImg(file);
        console.log(file);
      };
      reader.readAsDataURL(file);
    } else {
    }
  };

  const formData = new FormData();
  formData.append("name", productName);
  formData.append("description_text", descriptionText);
  formData.append("price", price);
  formData.append("travel_period", travelPeriod);
  formData.append("discount", discount);
  formData.append("view_count", viewCount);
  formData.append("status", status);
  formData.append("product_img", productImg);
  const data = {
    name: productName,
    product_img: productImg,
    description_text: descriptionText,
    price: price,
    travel_period: travelPeriod,
    discount: discount,
    view_count: viewCount,
    status: status,
  };
  console.log(data);
  const handleProduct = async () => {
    try {
      const response = await axios.post("/api/v1/product/", formData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
          "Content-Type": "multipart/form-data",
        },
      });
      console.log(response);
    } catch (error) {
      console.log("상품등록 에러", error);
    }
  };

  const handleDelete = async () => {
    const response = await axios.delete(
      `/api/v1/product/${productId}/`,
      {},
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
    console.log(response);
  };

  return (
    <div>
      <div>
        <h1>리뷰쓰기</h1>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <br />
        <input
          type="text"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <br />
        <button onClick={handleReview}>리뷰쓰기</button>
      </div>
      <br />
      <div>
        <h1>상품등록</h1>
        <label>제목</label>
        <input
          type="text"
          value={productName}
          placeholder="상품명"
          onChange={(e) => setProductName(e.target.value)}
        />
        <br />
        <label>내용</label>
        <input
          type="text"
          placeholder="내용"
          value={descriptionText}
          onChange={(e) => setDescriptionText(e.target.value)}
        />
        <br />
        <label>가격</label>
        <input
          type="number"
          placeholder="가격"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
        <br />
        <label>여행기간</label>
        <input
          type="text"
          placeholder="여행기간"
          value={travelPeriod}
          onChange={(e) => setTravelPeriod(e.target.value)}
        />
        <br />
        <label>할인율</label>
        <input
          type="text"
          placeholder="할인율"
          value={discount}
          onChange={(e) => setDiscount(e.target.value)}
        />
        <br />
        <input type="file" onChange={(e) => onChangeUserImg(e)} />
        <br />
        <button onClick={handleProduct}>상품등록</button>
      </div>
      <div>
        <button onClick={handleDelete}>상품 삭제{productId}</button>
      </div>
    </div>
  );
};

export default Testaa;
