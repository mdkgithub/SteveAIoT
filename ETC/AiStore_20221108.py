class C_AiStore:

    def __init__(self, store_name, store_id, store_address):
        self.store_name = store_name
        self.store_id = store_id
        self.store_address = store_address
        self.product_stock = 0
        self.product_price = 0


    # 상품개수, 상품가격을 파라미터 변수에 저장한다.
    def set_product(self, product_stock, product_price):
        # info = input('상품개수: ')
        self.product_price = product_price
        self.product_stock = product_stock

    # 구매개수, 입력금액(지불할돈)
    def buy_item(self, order_unit, input_money):

        # info = input('구매개수: ')
        # self.order_unit = input(info)
        self.product_stock = self.product_stock - order_unit

        if self.product_stock < order_unit:
            print('재고가 부족합니다')

        # info = input('지불금액: ')
        # self.input_money = input(info)

        if input_money < self.product_price:
            print('금액이 부족합니다')

        total_price = order_unit*self.product_price

        return_money = input_money - total_price
        print('잔돈은', return_money , '입니다')


    def get_name(self):
        return self.store_name

    def get_id(self):
        return self.store_id

    def get_locate(self):
        return self.store_address

    def get_count(self):
        return self.order_unit

    def get_price(self):
        return self.product_price



if __name__ == '__main__':

    print('스토어 지점이름 입력:')
    s_name = input()
    print('스토어 지점아이디 입력:')
    s_id = input()
    print('스토어 위치 입력:')
    s_locate = input()

    # print('구매 수량:')
    # s_stock = input()
    # print('상품 가격:')
    # s_price = input()
    # print('입금 가격:')
    # s_money = input()


    aistore = C_AiStore(s_name, s_id, s_locate)
    print('스토어 지점이름: ', aistore.store_name, '스토어 지점ID: ', aistore.store_id, '스토어 위치', aistore.store_address, '스토어가 생성되었습니다.')



    for button in range(0, 10):
        print('소트어 조회는 1번, 구매는 2번, 상품 관리는 3번, 종료는 4번을 눌려주세요')
        button = int(input())

        if button == 1:
            print('스토어 이름: ', aistore.store_name)
            # aistore.store_name(info)
            print('스토어 아이디: ', aistore.store_id)
            # aistore.store_id(info)
            print('재고개수: ', aistore.product_stock)
            # aistore.product_stock(info)
            print('상품가격: ', aistore.product_price)
            # aistore.product_price(info)

        elif button == 2:
            info = int(input('구매할 상품 개수 입력: '))
            # aistore.buy_item(info)

            product_totalprice = aistore.product_price*info
            print('상품 가격은 ', product_totalprice, '입니다')

            info_1 = int(input('필요한 금액 출력: '))

            aistore.buy_item(info, info_1)
            # aistore.buy_item(info)

        elif button == 3:
            info = int(input('상품 재고 입력: '))
            # aistore.product_stock(info)

            info_1= int(input('상품 가격 입력: '))
            aistore.set_product(info, info_1)

        elif button == 4:
            break
        # customer.get_rat()