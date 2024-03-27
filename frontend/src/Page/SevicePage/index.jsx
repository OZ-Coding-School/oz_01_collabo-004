import React from "react";
import "./index.css";

const faqs = [
  {
    question: "주문 상태를 어떻게 확인하나요?",
    answer: '로그인 후, "내 주문" 페이지에서 주문 상태를 확인할 수 있습니다.',
  },
  {
    question: "반품 정책은 어떻게 되나요?",
    answer:
      "상품 수령 후 30일 이내에 반품이 가능합니다. 자세한 내용은 반품 정책 페이지를 참조하세요.",
  },
  // 여기에 더 많은 FAQ를 추가할 수 있습니다.
];

function SupportPage() {
  return (
    <div className="support-container">
      <h2>고객센터</h2>
      <p>질문이 있으신가요? 아래 FAQ를 확인하거나 저희에게 연락해 주세요.</p>

      <h3>연락처 정보</h3>
      <p>이메일: support@example.com</p>
      <p>전화: 123-456-7890</p>

      <h3>자주 묻는 질문(FAQ)</h3>
      <ul>
        {faqs.map((faq, index) => (
          <li key={index}>
            <strong>{faq.question}</strong>
            <p>{faq.answer}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default SupportPage;
