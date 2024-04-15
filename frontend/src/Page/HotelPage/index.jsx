import React from 'react'
import './index.css'

function PetHousePage() {
  return (
    <div className='test-page'>
      <h2>상세페이지 제목</h2>
      <div className='test-page_contnet'>
        <div>
        <img src='./images/산책1.jpg'alt='상세페이지'/>
        </div>
        <div className='test-page_contnet_review'>
          <h3>리뷰</h3>
          <ul>
            <li>리뷰1번asasdasdasdasdasd</li>
            <li>리뷰2번asdasdasdasdasd</li>
            <li>리뷰3번asdasdasdasdasd</li>
            <li>리뷰4번asdasdasadasdasd</li>
          </ul>
        </div>
      </div>
      <div className='test-page2'>
        <div className='test-page_contnet_detail'>
        <h2>상세설명</h2>
        <h3>대 제목</h3>
        <p>상세설명 :</p> 
        <p>블라블라블라블라블라블라블라블라블라</p>
        <p>블라블라블라블라블라블라블라블라블라</p>
        <p>블라블라블라블라블라블라블라블라블라</p>
        </div>
      <div class="payment-form">
        <h2>결제페이지입니다.</h2>
        <h3>가격</h3>
        <p>결제페이지 내용(체크인, 체크아웃 시간설정)</p>
        <p>인원</p>
        <button>결제하기</button>
        <p>예약 확정 전에는 요금이 청구되지 않습니다.</p>
        <p>가격상세 :</p>
        <hr />
        <p>가격합계 :</p>
      </div>
      </div>
    </div>
  )
}

export default PetHousePage
