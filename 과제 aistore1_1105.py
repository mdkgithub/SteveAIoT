class AiStore:

"""
생성자
파라미터: 매점이름, 매점아이디, 매점위치
파라미터 셀프변수에 저장: 매점이름, 매점아이디, 매점위치
셀프변수 값 초기화: 상품개수, 상품가격
"""
    def __init__(self, s_name, s_id, s_locate):
        self.s_name = s_name
        self.s_id = s_id
        self.s_locate = s_locate
        self.p_count = 0
        self.p_price = 0

    def set_product(self, p_count, p_price):
        self.p_count = p_count
        self.p_price = p_price

"""
- 파라미터: 구매개수, 입력금액
- 상품개수에서 구매개수 차감
- 상품가격과 구매개수로부터 필요금액 산출
- 입력금액에서 필요금액 차감하여 '잔돈은 ~입니다' 출력(print)
- 상품개수가 모자라면 '재고가 부족합니다.' 출력(print)
- 입력금액이 부족하면 '금액이 부족합니다.' 출력(print)
"""
    def buy_item(self, order_unit, input_money):
        self.order_unit = order_unit
        self.input_money = input_money
        self.change_money = 0

        p_count =- order_unit
        need_price = self.p_price*order_unit

        if self.change_money == input_money - need_price:
            print('잔돈은', 'change_money', '입니다')

        if self.p_count < order_unit:
            print('재고가 부족합니다')

        if self.input_money < need_price:
            print('금액이 부족합니다')



    def get_name(self):
        return self.s_name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.s_locate

    def get_count(self):
        return self.p_count

    def get_price(self):
        return self.p_price


if __name__ == '__main__':

    s_name = input('스토어 지점이름 입력:')
    s_id = input('스토어 지점번호 입력:')
    s_locate = input('스토어 위치 입력:')

    store = AiStore(s_name, s_id, s_locate)

    print(store.get_name() + ' 스토어가 생성 되었습니다.')

    for i in range(10):

        print('스토어 조회는 1번, 구매는 2번, 상품 관리는 3번, 종료는 4번 을 눌러주세요')
        num = input()
        if num =='1':
            store.get_name()

        elif num == '2':
            order_unit = input('구매할 상품 개수 입력')
            store.buy_item()

            need_price = self.p_price * order_unit

            amount = input(str(need_price) + ' 금액을 입력해 주세요')
            ~

        elif num == '3':
            ~ = input('상품 재고 입력')
            ~ = input('상품 가격 입력')
            ~

        elif num == '4':
            print('종료합니다')
            break
        else:
            print('잘못된 입력입니다')