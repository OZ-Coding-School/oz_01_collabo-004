import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import "./WishList.css";

function BasicExample() {
  const [cards, setCards] = useState([
    {
      id: 1,
      title: "리센 오션파크 호텔",
      description: "속초해수욕장 근방 속초해수욕장 도보1분",
      imageUrl:
        "https://yaimg.yanolja.com/v5/2023/08/11/11/1280/64d61a0087a949.08624244.jpg",
      isBookmarked: false,
    },
  ]);
  const [productDetail, setProductDetail] = useState("");

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
