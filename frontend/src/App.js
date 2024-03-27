import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Search from "./Component/Header/index.jsx";
import Navbar from "./Component/Header/navbar/index.jsx";
import Home from "./Page/Homepage/index.jsx";
import MyInfo from "./Page/MyInfoPage";
import PetHouse from "./Page/PetHousePage";
import PetRestaurant from "./Page/PetRestaurantPage";
import PetShop from "./Page/PetShopPage";
import Service from "./Page/ServicePage";
import Travel from "./Page/TravelPage";

function App() {
  return (
    <BrowserRouter>
      <Search />
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/petshop" element={<PetShop />} />
        <Route path="/pethouse" element={<PetHouse />} />
        <Route path="/petrestaurant" element={<PetRestaurant />} />
        <Route path="/travel" element={<Travel />} />
        <Route path="/myinfo" element={<MyInfo />} />
        <Route path="/service" element={<Service />} />
        <Route path="*" element={<h2>Page Not Found</h2>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
