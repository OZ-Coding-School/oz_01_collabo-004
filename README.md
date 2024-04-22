FE: 민덕기, 김태율
BE: 임대용, 김형빈
BD: 김기철, 유용준

<메인페이지>
api/v1/ : 내려줄 데이터 {
                            'mostview' : {},
                            'high_repurchase_rate' : {},
                            'recommended' : {}
                        }

<제품관련>
- category number

trip = 100 번대 : 여행상품
foods = 200 번대 : 식당, 레스토랑
lodgings = 300 번대 : 숙소
nearby = 400 번대 : 주변여행지

api/v1/products
api/v1/products/{카테고리번호} : 선택한 카테고리의 제품들 반환 (페이지네이션)
api/v1/products/{카테고리번호}/{제품번호} : 선택한 제품의 디테일 반환
api/v1/products/search
api/v1/products/search&categories=~

<유저 정보>
api/v1/user/non-login
api/v1/user/login
api/v1/user/signup
api/v1/user/mypage : get - 회원정보, put - 수정, delete - 회원탈퇴(30일간 데이터보존)
api/v1/user/mypage/wish : get - 위시리스트 상품, delete - 선택한 상품 삭제

<주문, 결제>
api/v1/payment/{결제정보 id} : get - 결제할 상품들의 데이터, post - 결제
apu/v1/orderdetails/{주문번호} : get - 주문번호의 결제 상세페이지, post - 배송지, 연락처 등등 수정

<고객센터>
- question category number

- feedback category number

api/v1/cs : get - 고객센터 메인페이지 : 자주묻는질문, 카테고리 내려주기
api/v1/cs/{category_num}: get - 해당 질문 카테고리의 질문 페이지로 이동
api/v1/cs/feedbacks : get - 문의 카테고리 넘버 내려주기
api/v1/cs/feedbacks/{ct_num} : get - 문의사항 작성페이지, post - 문의사항 제출

