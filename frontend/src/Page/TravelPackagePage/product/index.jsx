import React from "react";
import { Link } from "react-router-dom";
import "./index.css";

function Product({ products }) {
  console.log(products.product_img);
  return (
    <div className="product">
      <Link
        to={`/travel/${products.name.replace(/ /g, "")}`}
        className="product-link"
        state={{ id: products.id }}
      >
        <img
          src={
            products.product_img ? products.product_img : "/images/no_image.png"
          }
          alt="상품이미지"
          className="product-img"
        />
        <h3>{products.name}</h3>
        <p>{products.description_text}</p>
        <p>가격: {products.price.toLocaleString()}원</p>
        <p>죄회수 : {products.view_count}</p>
      </Link>
    </div>
  );
}

export default Product;
