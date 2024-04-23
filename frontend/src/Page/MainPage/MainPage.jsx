import React from "react";
import { Section, SectionsContainer } from "react-fullpage";
import Main1 from "./Main1/Main1";
import Main2 from "./Main2/Main2";
import Main3 from "./Main3/Main3";
import Main4 from "./Main4/Main4";
import "./MainPage.css";

function Mainpage() {
  let options = {
    anchors: ["sectionOne", "sectionTwo", "sectionThree", "sectionFour"],
  };

  return (
    <div className="main-page">
      <SectionsContainer {...options}>
        <Section>
          {" "}
          <Main1 />{" "}
        </Section>
        <Section>
          {" "}
          <Main2 />{" "}
        </Section>
        <Section>
          {" "}
          <Main3 />{" "}
        </Section>
        <Section>
          {" "}
          <Main4 />{" "}
        </Section>
      </SectionsContainer>
    </div>
  );
}

export default Mainpage;
