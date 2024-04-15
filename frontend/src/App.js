import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import {
  BrowserRouter,
  Outlet,
  Route,
  Routes,
  useLocation,
} from "react-router-dom";
import Headerbar from "./Component/Header/index.jsx";
import Footer from "./Component/footer/index.jsx";
import Hotel from "./Page/HotelPage/index.jsx";
import Login from "./Page/Loginpage/index.jsx";
import Mainpage from "./Page/MainPage/index.jsx";

import PaymentPage from "./Page/MyPage/PaymentPage.jsx";
import MyPage from "./Page/MyPage/index.jsx";
import Travel from "./Page/RecommendedSpotPage/index.js";
import Restaurant from "./Page/RestaurantPage/index.js";
import Service from "./Page/SevicePage/index.jsx";
import SignupForm from "./Page/SignUpPage/index.jsx";
import TravelPackagePage from "./Page/TravelPackagePage/index.jsx";
import ProductDetail from "./Page/TravelPackagePage/product/productdetail/index.jsx";

const Layout = () => {
  const location = useLocation();
  return (
    <div>
      <Headerbar />
      <div style={{ height: location.pathname === "/" ? "0" : "70px" }}></div>
      <Outlet />
      <Footer />
    </div>
  );
};

function App() {
  return (
    <BrowserRouter>
      <Headerbar />
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Mainpage />} />
          <Route path="/travel" element={<TravelPackagePage />} />
          <Route path="/travel/:id" element={<ProductDetail />} />
          <Route path="/hotel" element={<Hotel />} />
          <Route path="/restaurant" element={<Restaurant />} />
          <Route path="/recommend" element={<Travel />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignupForm />} />
          <Route path="/mypage" element={<MyPage />} />
          <Route path="/service" element={<Service />} />
          <Route path="/payment" element={<PaymentPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
