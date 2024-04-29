import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "../../../api/axios";
import "./Product.css";

function Product({ products }) {

  const [isClicked, setIsClicked] = useState(false);

  const wishlistClick = async() => {
    setIsClicked(!isClicked);
    try {
      const response = await axios.post('/api/v1/wishlist/',
        {
            product: products.id
        },{
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${localStorage.getItem("token")}`,
                },
        });
            if (response.status === 200) {
                console.log('서버 응답:', response);
            }
        } catch (error) {
            console.log('서버 요청 실패:', error.message);
        }
  };

    const handleLinkClick = async () => {
    try {
      const response = await axios.post(`/api/v1/products/`,
        {}, {
              headers: {
                  'Content-Type': 'application/json',
                  Authorization: `Bearer ${localStorage.getItem("token")}`,
            },
        });
      if (response.status === 200) {
        console.log("조회수 증가 완료");
      }
    } catch (error) {
      console.log("조회수 증가 실패:", error.message);
    }
  };
  return (

    <div className="product">
      <Link
        to={`/travel/${products.name.replace(/ /g, "")}`}
        className="product-link"
        state={{ id: products.id }}
        onClick={handleLinkClick}
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