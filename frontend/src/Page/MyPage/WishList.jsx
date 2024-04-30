import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../../api/axios";
import "./WishList.css";

function WishList() {
  const [cards, setCards] = useState([]);
  const [isClicked, setIsClicked] = useState(false);
  const [count, setCount] = useState(0);
  const navigate = useNavigate();

  const wishlistClick = async (id) => {
    setCount((prev) => prev + 1);
    try {
      const response = await axios.post(
        "/api/v1/wishlist/",
        {
          product: id,
        },
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );
      if (response.status === 200) {
        setCards(cards.filter((card) => card.product.id !== id));
      }
    } catch (error) {}
  };

  const fetchData = async () => {
    try {
      const response = await axios.get("/api/v1/wishlist/", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });
      setCards(response.data);
    } catch (error) {}
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleClickPackage = (productId) => {
    navigate(`/travel/${productId.name.replace(/ /g, "")}`, {
      state: {
        id: productId.id,
      },
    });
  };
  return (
    <div className="card-list">
      <div className="card-item">
        {cards.map((card) => (
          <div className="card-deck" key={card.id}>
            <img
              className="card-img"
              src={card.product.product_img}
              alt={card.product.name}
            />
            <div className="card-details">
              <h2>{card.product.name}</h2>
              <p>{card.product.description_text}</p>
            </div>
            <button
              className="go-title"
              onClick={() => handleClickPackage(card.product)}
            >
              여행하러 갈까?
            </button>
            <div className="wishlist-bt">
              <button
                onClick={() => wishlistClick(card.product.id)}
                type="button"
              >
                다음에 가자..
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default WishList;
