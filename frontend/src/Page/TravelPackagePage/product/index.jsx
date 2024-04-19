import React from 'react';
import { Link } from 'react-router-dom';
import './index.css';

function Product({ products }) {


    return (
        <div className="product">
            <Link
                to={`/travel/${products.name}`}
                className="product-link"
                state={{ products }}
            >
                <img
                    src={products.product_img}
                    alt='상품이미지'
                    className='product-img'
                />
                <h3>{products.name}</h3>
                <p>{products.description_text}</p>
                <p>가격: {products.price.toLocaleString()}원</p>
                <p>조회수: {products.view_count}</p>
            </Link>
        </div>
    );
}

export default Product;
