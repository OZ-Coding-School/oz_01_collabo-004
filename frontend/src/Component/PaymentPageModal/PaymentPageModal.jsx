import React from "react";
import "./PaymentPageModal.css";

function PaymentPageModal({ isOpen, onClose, children }) {
  if (!isOpen) return null;

  return (
    <div className="paymentpage-modal-overlay">
      <div className="paymentpage-modal">
        <div className="paymentpage-modalclose-btn">
          <button onClick={onClose}>x</button>
        </div>
        <p>
          이 패키지의 최대 인원은 4명(유아 제외)입니다. 반려동물은 최소 1마리
          이상 포함되어야 합니다.
        </p>
        {children}
        <button onClick={onClose} className="paymentpage-modalclose-btn2">
          취소
        </button>
      </div>
    </div>
  );
}

export default PaymentPageModal;
