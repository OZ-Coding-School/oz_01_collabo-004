import React, { useEffect, useState } from "react";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import axios from "../../api/axios";
import "./WishList.css";

function BasicExample() {
  const [cards, setCards] = useState([]);
  const [loading, setLoading] = useState(true);

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
      console.log(response.data);
      setCards(response.data);
      setLoading(false);
    } catch (error) {
      console.log("Error fetching data:", error);
      setLoading(false);
    }
  };

  const handleBookmarkToggle = (id) => {
    setCards(
      cards.map((card) => {
        if (card.id === id) {
          return { ...card, isBookmarked: !card.isBookmarked };
        }
        return card;
      })
    );
  };

  return (
    <>
      {cards.map((card) => (
        <Card
          key={card.id}
          style={{
            margin: "120px",
            width: "18rem",
          }}
        >
          <Card.Img variant="top" src={card.imageUrl} />
          <Card.Body>
            <Card.Title>{card.title}</Card.Title>
            <Card.Text>{card.description}</Card.Text>
            <Button
              variant={card.isBookmarked ? "success" : "dark"}
              onClick={() => handleBookmarkToggle(card.id)}
              href={`/product/${card.id}`}
            >
              {card.isBookmarked ? "이동 중..." : "예약하러가기"}
            </Button>
          </Card.Body>
        </Card>
      ))}
    </>
  );
}

export default BasicExample;
