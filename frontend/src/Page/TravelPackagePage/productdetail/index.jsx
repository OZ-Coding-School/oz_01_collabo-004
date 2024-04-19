import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import './index.css';

function ProductDetail(props) {
    const location = useLocation()
    const data = location.state

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

const countTotalPrice = () => {
    const basePrice = data.products.price;
    const PersonToTalPrice = (numberOfPeople - 1) * basePrice; 
    const smallPetsTotalPrice = smallPetsCount * 6000; 
    const mediumPetsTotalPrice = mediumPetsCount * 10000; 
    const largePetsTotalPrice = largePetsCount * 15000;

    const totalPrice =
        basePrice +
        PersonToTalPrice +
        smallPetsTotalPrice +
        mediumPetsTotalPrice +
        largePetsTotalPrice;

    return totalPrice;
};

    const handleSubmit = (e) => {
    e.preventDefault();
    const totalPrice = countTotalPrice ();
    console.log('출발일:', departureDate);
    console.log('인원수:', numberOfPeople);
    console.log('소 반려동물 수:', smallPetsCount);
    console.log('중 반려동물 수:', mediumPetsCount);
    console.log('대 반려동물 수:', largePetsCount);
    console.log('총 예약 가격:', totalPrice.toLocaleString(), '원');
};

    return (
    <div className='productdetail-page'>

    <div className='productdetail-page_contnet'>
        <div className='productdetail-page-title'>
        <h2>{data.products.name}</h2>
        <img
        src={data.products.product_img}
        alt='상품이미지'
        className='productdetail-page_product-img'
        />
        <p>조회수 : {data.products.view_count}</p>
        </div>
        <div className='productdetail-page_contnet_review-content'>
        <h3>해당상품 리뷰</h3>
        <div className='productdetail-page_contnet_review'>
            <ul>
            <li>Woo play like woo 밤새 파티를 열어볼까 봐요</li>
            <li>둠바둠바둠바둠바둠바둠바웨둠바둠바둠바둠바둠바둠바웨</li>
            <li>앵두 같은 입술이 달린달린 달린 달린어여쁜 그대 얼굴이내 두 눈을 집어삼켜 버리곤</li>
            <li>Woo swallow woo책임져 아주 혼내줘야겠어요눈 깜빡하면 사라질 듯이실감이 안 나는 걸That's right</li>
            <li>You are my baby 이젠 내 사랑 My darling 평생 내 옆자리에서 웃어요 행복한 기분이 샘솟아 눈물이 다 나올 때까지</li>
            </ul>
        </div>
        </div>
    </div>

    <div className='productdetail-page2'>
        <div className='productdetail-page_contnet_detail'>
        <p>상세설명 : {data.products.description_text}</p>
        </div>
        <div className="reservation-form">
            <h3>상품가격 : {data.products.price.toLocaleString()} 원</h3>
            <form onSubmit={handleSubmit}>
            <table className='reservation-form-table'>
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
                # 반려동물 요금 및 상세정보{''}
                <span>
                <button onClick={togglePetSizeInfo}>
                    {showPetSizeInfo ? '간략히' : '자세히'}
                </button>
                </span>
            </p>
            {showPetSizeInfo && (
                <div>
                <p>소 : (6000원) 5kg 미만 </p>
                <p>중 : (10000원) 5kg 이상 ~ 25kg 미만 </p>
                <p>대 : (15000원) 25kg 이상 </p>
                </div>
            )}
            </div>

            <button type="submit" className='reservation-btn'>
            예약하기
            </button>
        </form>
        <p>예약 확정 전에는 요금이 청구되지 않습니다.</p>
        <p>모든 상품은 인원수,반려동물의수의 따라 변결될수있습니다.</p>
        <hr />
        <p>총 예약 가격 : {countTotalPrice().toLocaleString()} 원</p>
        </div>
    </div>
    
    </div>
    );
}

export default ProductDetail;