import { faChevronLeft, faChevronRight, } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "../../../api/axios";
import "./Main2.css";

function Main2() {
  const [productData, setProductData] = useState([]);

  useEffect(() => {
    const handleNextClick = () => {
      const items = document.querySelectorAll(".item");
      document.querySelector(".slide").appendChild(items[0]);
    };

    const handlePrevClick = () => {
      const items = document.querySelectorAll(".item");
      document.querySelector(".slide").prepend(items[items.length - 1]);
    };

    const nextButton = document.querySelector(".next");
    const prevButton = document.querySelector(".prev");

    if (nextButton && prevButton) {
      nextButton.addEventListener("click", handleNextClick);
      prevButton.addEventListener("click", handlePrevClick);
    }

    return () => {
      if (nextButton && prevButton) {
        nextButton.removeEventListener("click", handleNextClick);
        prevButton.removeEventListener("click", handlePrevClick);
      }
    };
  }, []);

  const getData = async () => {
    try{
      const response = await axios.get("/api/v1/product/");
      setProductData(response.data);
    }catch(error){
      console.log(error);
    }
  };
  useEffect(() => {
    getData();
  }, [])
  


  return (
    <div className="main2-contanier">
      <div className="main2slideshow-container">

        <div className="slide">
          {productData.map((item,index) =>(
            <div
              key={index}
              className="item"
              style={{ backgroundImage: `url(${item.product_img})` }}
            >
            <div className="main2slideshow-content">
            <div className="main2slideshow-content-title">
            <h2>{item.name}</h2>
                  <h5>{item.description_text}</h5>
                </div>
                <Link
                  to={`/travel/${item.name.replace(/ /g, "")}`} state={{ id: item.id }} >
                  <button>SEE MORE</button>
                  </Link>
            </div>
            </div>
          ))}

        </div>

        <div className="main2slideshow-btn">
          <button className="prev">
            <FontAwesomeIcon icon={faChevronLeft} />
          </button>
          <button className="next">
            <FontAwesomeIcon icon={faChevronRight} />
          </button>
        </div>
      </div>
    </div>
  );
}

export default Main2;