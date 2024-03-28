import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Search from "./Component/Header/index.jsx";
import Footer from "./Component/footer/index.jsx";
import Navbar from "./Component/navbar/index.jsx";
import Home from "./Page/Homepage/index.jsx";
import Login from "./Page/Loginpage/index.jsx";
import PetHouse from "./Page/PetHousePage/index.js";
import PetRestaurant from "./Page/PetRestauntPage/index.js";
import PetShop from "./Page/PetShopPage/index.js";
import Service from "./Page/SevicePage/index.jsx";
import SignupForm from "./Page/SignUpPage/index.jsx";
import Travel from "./Page/TravelPage/index.js";

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
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignupForm />} />
        <Route path="/service" element={<Service />} />
        <Route path="*" element={<h2>Page Not Found</h2>} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
