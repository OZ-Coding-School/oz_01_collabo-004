import React from "react";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Navbar from "./Component/Navbar";
import Home from "./Page/HomePage";
import MyInfo from "./Page/MyInfoPage";
import PetHouse from "./Page/PetHousePage";
import PetRestaurant from "./Page/PetRestaurantPage";
import PetShop from "./Page/PetShopPage";
import Service from "./Page/ServicePage";
import Travel from "./Page/TravelPage";

function App() {
  return (
    <Router>
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
    </Router>
  );
}

export default App;
