import React from 'react';
import { useLocation } from 'react-router-dom';
import './index.css';

function ProductDetail(props) {
    const location = useLocation()
    const data = location.state

return (
    <div className='productdetailpage'>
    <h1>상세 페이지</h1>
    <img src={data.products.product_img}
    alt='상품이미지' 
    className='product-img'
    />
    <p>상품명 : {data.products.name}</p>
    <p>상세설명 : {data.description_text}</p>
    <p>가격 : {data.price.toLocaleString()} 원</p>
    <p>조회수 : {data.products.view_count}</p>
    </div>
);
}

export default ProductDetail;
