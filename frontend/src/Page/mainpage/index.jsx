import React from 'react';
import { Section, SectionsContainer } from 'react-fullpage';
import './index.css';
import Main1 from './main1';
import Main2 from './main2';
import Main3 from './main3';
import Main4 from './main4';

function Mainpage() {

  let options = {
    anchors: ['sectionOne', 'sectionTwo', 'sectionThree','sectionFour']
};

  return (
    <div className='main-page'>
    <SectionsContainer {...options}>
    <Section> <Main1 /> </Section>
    <Section> <Main2 /> </Section>
    <Section> <Main3 /> </Section>
    <Section> <Main4 /> </Section>
  </SectionsContainer>
    </div>
  );
}

export default Mainpage;
