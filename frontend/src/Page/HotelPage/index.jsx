import React, { useState } from 'react';
import './index.css';

function PetHousePage() {
  const [departureDate, setDepartureDate] = useState('');
  const [numberOfPeople, setNumberOfPeople] = useState(1);
  const [smallPetsCount, setSmallPetsCount] = useState(1);
  const [mediumPetsCount, setMediumPetsCount] = useState(0);
  const [largePetsCount, setLargePetsCount] = useState(0);
  const [showPetSizeInfo, setShowPetSizeInfo] = useState(false);

  const togglePetSizeInfo = () => {
    setShowPetSizeInfo((prevState) => !prevState);
  };

  const handleDateChange = (e) => {
    setDepartureDate(e.target.value);
  };

  const handlePeopleChange = (amount) => {
    setNumberOfPeople((prevCount) => Math.max(1, prevCount + amount));
  };

  const handlePetsChange = (size, amount) => {
    switch (size) {
      case 'small':
        setSmallPetsCount((prevCount) => Math.max(0, prevCount + amount));
        break;
      case 'medium':
        setMediumPetsCount((prevCount) => Math.max(0, prevCount + amount));
        break;
      case 'large':
        setLargePetsCount((prevCount) => Math.max(0, prevCount + amount));
        break;
      default:
        break;
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('출발일:', departureDate);
    console.log('인원수:', numberOfPeople);
    console.log('소 반려동물 수:', smallPetsCount);
    console.log('중 반려동물 수:', mediumPetsCount);
    console.log('대 반려동물 수:', largePetsCount);
  };

  return (
    <div className='test-page'>
      <div className='test-page_contnet'>
        <div>
        <h2>상세페이지 제목</h2>
          <img
            src='./images/캠핑.png'
            alt='상세페이지'
            className='test-page_product-img'
          />
        </div>
        <div className='test-page_contnet_review'>
        <h3>해당상품 리뷰</h3>
          <ul>
            <li>Woo play like woo 밤새 파티를 열어볼까 봐요</li>
            <li>둠바둠바둠바둠바둠바둠바웨둠바둠바둠바둠바둠바둠바웨</li>
            <li>앵두 같은 입술이 달린달린 달린 달린어여쁜 그대 얼굴이내 두 눈을 집어삼켜 버리곤</li>
            <li>Woo swallow woo책임져 아주 혼내줘야겠어요눈 깜빡하면 사라질 듯이실감이 안 나는 걸That's right</li>
          </ul>
        </div>
      </div>

      <div className='test-page2'>
        <div className='test-page_contnet_detail'>
          <img
            src='./images/상세설명이미지.png'
            alt='상세설명이미지'
            className='test-page_detail-img'
          />
        </div>
        <div className="reservation-form">
          <h3>가격 :  000,000 원</h3>
          <form onSubmit={handleSubmit}>
            <table>
              <tbody>
                <tr>
                  <td>출발일 : </td>
                  <td>
                    <input
                      type="date"
                      value={departureDate}
                      onChange={handleDateChange}
                      required
                      className="reservation-form-input"
                    />
                  </td>
                </tr>
                <tr>
                  <td>인원 수 : </td>
                  <td>
                    <button
                      onClick={() => handlePeopleChange(-1)}
                      className="counter-button"
                    >
                      -
                    </button>
                    <span>{numberOfPeople}</span>
                    <button
                      onClick={() => handlePeopleChange(1)}
                      className="counter-button"
                    >
                      +
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>반려동물 (소): </td>
                  <td>
                    <button
                      onClick={() => handlePetsChange('small', -1)}
                      className="counter-button"
                    >
                      -
                    </button>
                    <span>{smallPetsCount}</span>
                    <button
                      onClick={() => handlePetsChange('small', 1)}
                      className="counter-button"
                    >
                      +
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>반려동물 (중): </td>
                  <td>
                    <button
                      onClick={() => handlePetsChange('medium', -1)}
                      className="counter-button"
                    >
                      -
                    </button>
                    <span>{mediumPetsCount}</span>
                    <button
                      onClick={() => handlePetsChange('medium', 1)}
                      className="counter-button"
                    >
                      +
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>반려동물 (대): </td>
                  <td>
                    <button
                      onClick={() => handlePetsChange('large', -1)}
                      className="counter-button"
                    >
                      -
                    </button>
                    <span>{largePetsCount}</span>
                    <button
                      onClick={() => handlePetsChange('large', 1)}
                      className="counter-button"
                    >
                      +
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>

            <div className='petcount_add'>
              총 : 인원 {numberOfPeople}명 / 반려동물 {smallPetsCount + mediumPetsCount + largePetsCount} 마리
            </div>
            <div className='petsize-info'>
              <p>
                # 반려동물의 사이즈?{''}
                <span>
                  <button onClick={togglePetSizeInfo}>
                    {showPetSizeInfo ? '간략히' : '자세히'}
                  </button>
                </span>
              </p>
              {showPetSizeInfo && (
                <div>
                  <p>소 : 5kg 미만</p>
                  <p>중 : 5kg 이상 ~ 25kg 미만</p>
                  <p>대 : 25kg 이상</p>
                </div>
              )}
            </div>

            <button type="submit" className='reservation-btn'>
              예약하기
            </button>
          </form>

          <p>예약 확정 전에는 요금이 청구되지 않습니다.</p>
          <p>가격상세 : 000,000 원</p>
          <hr />
          <p>가격합계 : 000,000 원</p>
        </div>
      </div>
    </div>
  );
}

export default PetHousePage;

