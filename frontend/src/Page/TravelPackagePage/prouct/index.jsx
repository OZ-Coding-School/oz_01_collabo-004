import React from 'react';
import { Link } from 'react-router-dom';
import './index.css';

function Product({products}) {
console.log(products.product_img)
return (
    <div className="product">
    
    <Link to={`/petshop/${products}`}
    
    className="product-link" 
    state={{products}}>
    <img src={products.product_img} 
    alt='상품이미지' 
    className='product-img'
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
