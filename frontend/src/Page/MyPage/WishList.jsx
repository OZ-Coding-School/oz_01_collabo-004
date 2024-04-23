import React, { useEffect, useState } from "react";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import { useNavigate } from "react-router-dom";
import axios from "../../api/axios";
import "./WishList.css";

function WishList() {
  const [cards, setCards] = useState([]);
  const navigate = useNavigate();
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get("/api/v1/wishlist/", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });
      setCards(response.data);
    } catch (error) {
      console.log("Error fetching data:", error);
    }
  };

  const handleClickPackage = (productId) => {
    navigate(`/travel/${productId.name.replace(/ /g, "")}`, {
      state: {
        id: productId.id,
      },
    });
  };
  return (
    <>
      {cards.map((card) => (
        <Card
          key={card?.id}
          style={{
            margin: "120px",
            width: "18rem",
          }}
        >
          <Card.Img variant="top" src={card.product?.product_img} />
          <Card.Body>
            <Card.Title>{card.product?.name}</Card.Title>
            <Card.Text>{card.product?.description_text}</Card.Text>

            <Button
              variant={card.isBookmarked ? "success" : "dark"}
              onClick={() => handleClickPackage(card.product)}
            >
              여행하러갈까?
            </Button>
          </Card.Body>
        </Card>
      ))}
    </>
  );
}

export default WishList;
