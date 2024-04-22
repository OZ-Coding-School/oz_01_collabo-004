import React, { useState } from "react";
import Col from "react-bootstrap/Col";
import Nav from "react-bootstrap/Nav";
import Row from "react-bootstrap/Row";
import Tab from "react-bootstrap/Tab";
import Testaa from "../../Component/Testaa";
import Coupon from "./Coupon";
import Order from "./Order";
import Profile from "./Profile";
import Review from "./Review/ReviewPage";
import WishList from "./WishList";
import "./index.css";

function MyPage() {
  const [userId, setUserId] = useState("");

  return (
    <Tab.Container id="left-tabs-example" defaultActiveKey="first">
      <div></div>
      <Row>
        <Col sm={3}>
          <Nav variant="pills" className="flex-column">
            <Nav.Item>
              <Nav.Link eventKey="first">내 정보</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="second">찜 목록</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="third">예약 내역</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="fourth">쿠 폰</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="fifth">리 뷰</Nav.Link>
            </Nav.Item>
            {userId === "startez" ? (
              <Nav.Item>
                <Nav.Link eventKey="sixth">테스트</Nav.Link>
              </Nav.Item>
            ) : null}
          </Nav>
        </Col>
        <Col sm={9}>
          <Tab.Content>
            <Tab.Pane eventKey="first">
              <Profile setUserId={setUserId} />
            </Tab.Pane>
            <Tab.Pane eventKey="second">
              <WishList />
            </Tab.Pane>
            <Tab.Pane eventKey="third">
              <Order />
            </Tab.Pane>
            <Tab.Pane eventKey="fourth">
              <Coupon />
            </Tab.Pane>
            <Tab.Pane eventKey="fifth">
              <Review />
            </Tab.Pane>
            <Tab.Pane eventKey="sixth">
              <Testaa />
            </Tab.Pane>
          </Tab.Content>
        </Col>
      </Row>
    </Tab.Container>
  );
}

export default MyPage;
