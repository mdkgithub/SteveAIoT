class AiStore:

    def __init__(self, s_name, s_id, s_locate):
        self.s_name = s_name
        self.s_id = s_id
        self.s_locate = s_locate
        self.p_count = 0
        self.p_price = 0

    def set_product(self, p_count, p_price):
        self.p_count = p_count
        self.p_price = p_price

    def buy_item(self, p_count, input_money):
        if self.p_count < p_count :
            print('재고가 부족합니다')
            return
        need_price = self.p_price * count

        if input_money < need_price :
            print('금액이 부족합니다')
            return

        self.p_count -= p_count
        change_money = input_money - need_price
        print('잔돈은', int(change_money), '입니다')
        # print('잔돈은 %i입니다' % change_money)

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

    print(store.get_name(), ' 스토어가 생성 되었습니다.')

    for i in range(10):

        print('스토어 조회는 1번, 구매는 2번, 상품 관리는 3번, 종료는 4번 을 눌러주세요')
        num = input()
        if num =='1':
            print(store.get_name(), store.get_id(), store.get_locate(), '스토어가 생성되었습니다')

        elif num == '2':
            # count = int(input('구매할 상품 개수 입력'))
            count = int(input('구매할 상품 개수 입력'))
            need_price = store.p_price * count
            # amount = int(input(str(need_price) + ' 금액을 입력해 주세요'))
            amount = int(input(str(need_price) + ' 금액을 입력해 주세요'))
            store.buy_item(count, amount)

        elif num == '3':
            count = input('상품 재고 입력')
            price = input('상품 가격 입력')

            store.set_product(int(count), int(price))

        elif num == '4':
            print('종료합니다')
            break

        else:
            print('잘못된 입력입니다')