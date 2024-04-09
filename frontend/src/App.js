import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Headerbar from "./Component/Header/index.jsx";
import Footer from "./Component/footer/index.jsx";
import Hotel from "./Page/HotelPage/index.js";
import Login from "./Page/Loginpage/index.jsx";
import Home from "./Page/MainPage/index.jsx";
import MyPage from "./Page/MyPage/index.jsx";
import Travel from "./Page/RecommendedSpotPage/index.js";
import Restaurant from "./Page/RestaurantPage/index.js";
import Service from "./Page/SevicePage/index.jsx";
import SignupForm from "./Page/SignUpPage/index.jsx";
import PetShop from "./Page/TravelPackagePage/index.jsx";

function App() {
  return (
    <BrowserRouter>
      <Headerbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/petshop" element={<PetShop />} />
        <Route path="/hotel" element={<Hotel />} />
        <Route path="/restaurant" element={<Restaurant />} />
        <Route path="/travel" element={<Travel />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignupForm />} />
        <Route path="/mypage" element={<MyPage />} />
        <Route path="/service" element={<Service />} />
        <Route path="*" element={<h2>Page Not Found</h2>} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
