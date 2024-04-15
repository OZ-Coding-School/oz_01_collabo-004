import React from 'react';
import { useLocation } from 'react-router-dom';
import './index.css';

function ProductDetail(props) {
    const gangone = useLocation()
    const data = gangone.state
return (
    <div className='productdetailpage'>
    <h1>상세 페이지</h1>
    <img src={data.products.product_img} /*로컬환경에서 이미지경로 문제로 => 변수를선언후에 앞에 " ." 붙혀줌*/
    alt='상품이미지' 
    className='product-img'
    />
    <p>상품명 : {data.products.name}</p>
    <p>상세설명 : {data.products.description_text}</p>
    <p>가격 : {data.products.price.toLocaleString()} 원</p>
    <p>조회수 : {data.products.view_count}</p>
    </div>
);
}

export default ProductDetail;
