import React, { useState } from "react";
import Col from "react-bootstrap/Col";
import Nav from "react-bootstrap/Nav";
import Row from "react-bootstrap/Row";
import Tab from "react-bootstrap/Tab";
import Testaa from "../../Component/Testaa";
import Coupon from "./Coupon";
import "./MyPage.css";
import Order from "./Order";
import Profile from "./Profile";
import Review from "./Review/ReviewPage";
import WishList from "./WishList";

function MyPage() {
  const [userId, setUserId] = useState("");

  return (
    <Tab.Container id="left-tabs-example" defaultActiveKey="first">
      <Row>
        <Col sm={3}>
          <Nav variant="pills" className="flex-column">
            <Nav.Item>
              <Nav.Link eventKey="first">MY INFO</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="second">WISH LIST</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="third">BOOKING</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="fourth">COUPON</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="fifth">REVIEW</Nav.Link>
            </Nav.Item>
            {userId === "deokgeneral12, startez" ? (
              <Nav.Item>
                <Nav.Link eventKey="sixth">테스트</Nav.Link>
              </Nav.Item>
            ) : null}
          </Nav>
        </Col>
        <Col sm={8}>
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
              <Coupon/>
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
