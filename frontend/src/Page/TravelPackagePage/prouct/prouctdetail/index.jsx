import React from 'react';
import { useLocation } from 'react-router-dom';
import './index.css';

function ProductDetail(props) {
    const gangone = useLocation()

return (
    <div className='productdetailpage'>
    <h1>상세 페이지</h1>
    <img src={`.${gangone.state.product.imageUrl}`}/*로컬환경에서 이미지경로 문제로 => 변수를선언후에 앞에 " ." 붙혀줌*/
    alt='상품이미지' 
    className='product-img'
    />
    <p>상품명 : {gangone.state.product.name}</p>
    <p>상세설명 : {gangone.state.product.description}</p>
    <p>가격 : {gangone.state.product.price.toLocaleString()} 원</p>
    </div>
);
}

export default ProductDetail;
