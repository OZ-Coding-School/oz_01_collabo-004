import React, { useState } from 'react';
import './index.css';

const Main4 = () => {
    const qaData = [
    {
        id: 1,
        question: '반려동물 동반 여행 서비스란 무엇인가요?',
        answer: '도고는 제주도를 반려동물과 함께하는 여행을 전문적으로 지원하는 서비스 입니다.'
    },
    {
        id: 2,
        question: '도고는 어떻게 이용하나요?',
        answer: '도고 웹사이트에 (로그인 / 회원가입) 후에 사이트에 해당하는 카테고리 추천을 통해 정보를 확인하고 숙박 및 여행상품을 예약합니다.'
    },
    {
        id: 3,
        question: '도고의 이용료는 얼마인가요?',
        answer: '도고는 기본 서비스로 무료로 이용 가능합니다. 숙박 예약 등 일부 서비스는 이용 수수료가 발생할 수 있습니다.'
    },
];

    const [selectedQuestion, setSelectedQuestion] = useState(null);

    const handleQuestionClick = (id) => {
    setSelectedQuestion((prev) => (prev === id ? null : id));
};

return (
    <div className="q-a-container">
        <div className="q-a-container-title">
            <h3>자주 묻는 질문 (Q&A)</h3>
            <h1>사이트에 대한</h1>
            <h1>궁금한 점?</h1>
        </div>
        <div className="q-a-container-content">
        <div className="q-a-container-description">
            <h2>도고사이트란?</h2>
            <p>사랑하는 반려동물과 제주도여행이 처음이라면</p>
            <p>숙소 예약이 어렵고, 댕댕이와 동반 가능한 여행지 정보도 찾기 힘들어요.</p>
            <p>여행 중 댕댕이의 안전과 건강을 걱정하면 긴장하게 돼요.</p>
            <p>하지만 이제 걱정하지 마세요! "DogGo"가 당신의 고민을 해결해 드립니다.</p>
        </div>
        <div className="q-a-container-qa">
        <div className="qa-list">
        {qaData.map((item) => (
        <div key={item.id} className="qa-item">
        <div
            className={`question ${selectedQuestion === item.id ? 'active' : ''}`}
            onClick={() => handleQuestionClick(item.id)}
        >
        {item.question}
        </div>
        <div
            className={`answer ${selectedQuestion === item.id ? 'show' : ''}`}
        >
        {item.answer}
        </div>
        </div>
    ))}
        </div>
        </div>
        </div>
        </div>
);
};

export default Main4;
