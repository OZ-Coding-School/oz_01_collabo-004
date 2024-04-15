import React from 'react';

function AlertModal({ message, onClose }) {
  return (
    <div className="modal-overlay">
      <div className="alert-modal">
        <p>{message}</p>
        <button onClick={onClose}>닫기</button>
      </div>
    </div>
  );
}

export default AlertModal;