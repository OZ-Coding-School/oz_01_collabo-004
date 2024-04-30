import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "../../../api/axios";
import "./Product.css";

function Product({ products }) {
  const [isClicked, setIsClicked] = useState(false);

  const wishlistClick = async () => {
    setIsClicked(!isClicked);
    try {
      const response = await axios.post(
        "/api/v1/wishlist/",
        {
          product: products.id,
        },
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );
      if (response.status === 200) {
      }
    } catch (error) {}
  };

  // //리뷰증가시에 서버에
  const reviewOnClick = async () => {
    try {
      const response = await axios.post(
        `/api/v1/product/${products.id}/`,
        {},
        {}
      );
    } catch (error) {}
  };

  return (
    <div className="product">
      <Link
        to={`/travel/${products.name.replace(/ /g, "")}`}
        className="product-link"
        state={{ id: products.id }}
        onClick={reviewOnClick}
      >
        <img
          src={products.product_img}
          alt="상품이미지"
          className="product-img"
        />
        <div className="product-info">
          <h3>{products.name}</h3>
          <p>{products.description_text}</p>
          <p>가격: {products.price.toLocaleString()}원</p>
          <p>조회수: {products.view_count}</p>
        </div>
      </Link>
      <div className="wishlist-btn">
        <button
          onClick={wishlistClick}
          type="button"
          className={isClicked ? "wishlist-btn-clicked" : ""}
        >
          <span className="material-symbols-outlined favorite">pets</span>
        </button>
      </div>
    </div>
  );
}

export default Product;
