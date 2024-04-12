import React, { useEffect, useState } from 'react';
import request from '../../axios';
import './index.css';
import Product from './prouct';



function Travelpackage() {  
  const [products, setProducts] = useState([]);
  useEffect(() => {
    fetchProduct()
  }, [])
  


  const fetchProduct = async() => {
    try{
      const response = await request.get(`/api/v1/product/`,{
        headers: {
          "Content-Type": "application/json",
          "ngrok-skip-browser-warning": "69420",
        },
        withCredentials: true,
      });      
      console.log(response.data);
      if (response.status === 200){
        console.log("데이터받아오기 성공!!")
        setProducts(response.data);
        console.log(products)
      }else if(response.status === 404) {
        console.log("데이터 받기 실패!!")
      }
    }catch (error){
      console.error(error);
    }
  }



  const [searchTerm, setSearchTerm] = useState('');


  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };


  const filteredProducts = products.filter((product) =>
    product.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
      <div className="petshop-page">
      <div className="petshop-page-title">
      <h1>Welcome to DogGO!</h1>
      <p>도고에서 준비한 색다른 컨텐츠를 둘러보세요!</p>
      <input
        type="text"
        placeholder="검색어"
        value={searchTerm}
        onChange={handleSearchChange}
      />
      </div>
      <h3>상품목록</h3>
      <div className="product-list">
        {filteredProducts.map((products) => (
          <Product
          key={products.id}
          products={products}
          />
        ))}
      </div>
    </div>
  );
}

export default Travelpackage;







