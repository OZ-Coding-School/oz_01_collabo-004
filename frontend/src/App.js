import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import {
  BrowserRouter,
  Outlet,
  Route,
  Routes,
  useLocation,
} from "react-router-dom";
import Footer from "./Component/Footer/Footer.jsx";
import HeaderBar from "./Component/Header/Header.jsx";
import ScrollTop from "./Component/ScrollTop.jsx";
import Testaa from "./Component/Testaa.jsx";
import Hotel from "./Page/HotelPage/HotelPage.jsx";
import Auth from "./Page/Loginpage/Auth.jsx";
import Login from "./Page/Loginpage/LoginPage.jsx";
import MainPage from "./Page/MainPage/MainPage.jsx";
import MyPage from "./Page/MyPage/MyPage.jsx";
import Travel from "./Page/RecommendedSpotPage/RecommendedSpotPage.jsx";
import Restaurant from "./Page/RestaurantPage/RestaurantItem.jsx";
import Service from "./Page/SevicePage/SevicePage.jsx";
import SignupForm from "./Page/SignUpPage/SignUpPage.jsx";
import PaymentPage from "./Page/TravelPackagePage/PaymentPage/PaymentPage.jsx";
import ProductDetail from "./Page/TravelPackagePage/ProductDetail/ProductDetail.jsx";
import TravelPackagePage from "./Page/TravelPackagePage/TravelPackagePage.jsx";

const Layout = () => {
  const location = useLocation();
  return (
    <div>
      <HeaderBar />
      <div style={{ height: location.pathname === "/" ? "0" : "70px" }}></div>
      <Outlet />
      <Footer />
    </div>
  );
};

function App() {
  return (
    <BrowserRouter>
      <ScrollTop />
      <HeaderBar />
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<MainPage />} />
          <Route path="/travel" element={<TravelPackagePage />} />
          <Route path="/travel/:id" element={<ProductDetail />} />
          <Route path="/hotel" element={<Hotel />} />
          <Route path="/restaurant" element={<Restaurant />} />
          <Route path="/recommend" element={<Travel />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignupForm />} />
          <Route path="/mypage" element={<MyPage />} />
          <Route path="/service" element={<Service />} />
          <Route path="/test" element={<Testaa />} />
          <Route path="/paymentpage" element={<PaymentPage />} />
          <Route path="/auth" element={<Auth />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
