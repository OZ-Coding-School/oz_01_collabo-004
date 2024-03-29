import React from "react";

// 최근 본 상품을 나타내는 컴포넌트
function RecentlyViewedSection() {
  // 최근 본 상품 데이터 - 실제 데이터로 대체되어야 함
  const recentlyViewedProducts = [
    {
      id: 1,
      title: "상품 제목",
      imageUrl: "https://via.placeholder.com/150", // 이미지 URL
      price: 10000, // 가격
    },
    {
      id: 2,
      title: "다른 상품 제목",
      imageUrl: "https://via.placeholder.com/150", // 이미지 URL
      price: 15000, // 가격
    },
    // 추가 상품 데이터...
  ];

  return (
    <div className="recently-viewed">
      <h2>최근 본 상품</h2>
      <div className="product-list">
        {recentlyViewedProducts.map((product) => (
          <div className="product-card" key={product.id}>
            <img src={product.imageUrl} alt={product.title} />
            <div className="product-info">
              <h3>{product.title}</h3>
              <p>{product.price}원</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default RecentlyViewedSection;
