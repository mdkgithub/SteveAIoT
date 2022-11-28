class AiStore:

    def __init__(self, name, s_id, locate):
        self.name = name
        self.s_id = s_id
        self.locate = locate
        self.products = {'커피':10}
        self.prices = {'커피':1000}

    # 상품 주문 개수를 확인할 수 있어야 한다. 상품 가격을 확인 할 수 있어야 한다.
    # 없는 상품이면 상품 주문 개수에 할당하지 않는다.
    def set_product(self, product, count, price):
        if product in self.products:
            self.products[product] += count
            self.prices[product] = price

        else :
            self.products[product] = count
            self.prices[product] = price
            return


    # 구매한 상품 수량이 재고 수량보다 작으면 상품 재고 수량을 차감한다.
    # 지불 금액에서 상품 가격을 차감하여 잔돈을 계산한다.

    def buy_product(self, product, count, amount):
        if count * self.products[product] < amount:
            self.products[product] -= count
            changes = amount - count * self.prices[product]
            print('잔돈은' + str(changes))

        else :
            print('금액이 부족합니다')
            return


    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_products(self):
        return self.products

    def get_prices(self):
        return self.prices

def create_store():
    s_name = input('스토어 이름 입력: ')
    s_id = input('스토어 아이디 입력: ')
    locate = input('스토어 위치 입력: ')

    store = AiStore(s_name, s_id, locate)

    print('{} 스토어가 생성 되었습니다.'.format(store.get_name()))
    return store


def show_list():
    for store in store_list:
        print('스토어 이름:{} 스토어 아이디:{} 스토어 위치:{}'.format(store.get_name(), store.get_id(), store.get_products()))


def search_store(s_id):
    for store in store_list:
        if store.get_id == s_id:
            return store
        print('스토어 아이디를 찾지 못했습니다.')
        return None

def show_store():
    s_id = input('스토어 아이디 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    print('{} 스토어 재고 현황: {}'.format(store.get_products()))
    print('{} 스토어 가격 현황: {}'.format(store.get_price()))


def buy():
    s_id = input('스토어 아이디 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    product = input('상품 입력: ')
    count = input('구매 개수 입력: ')
    # 옵션 '총 가격은 {} 입니다.' 출력

    if product in store.get_products():
        print('총 가격은 {} 입니다'.format(store.get_prices()[product] * count))

    price = input('가격 입력: ')
    price = int(price)

    store.buy_product(product, count, price)


def manager_product():

    s_id = input('스토어 번호 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    product = input('상품 입력: ')
    count = input('재고 개수 입력: ')
    price = input('상품 가격 입력: ')

    store.set_product(product, count, price)


def txt_to_store():
    pass


import json
def store_to_json():
    pass


if __name__ == '__main__':
    store_list = []

    print('1 - 스토어 생성')
    print('2 - 스토어 리스트 출력')
    print('3 - 스토어 정보 출력')
    print('4 - 상품 구매')
    print('5 - 상품 관리')
    print('6 - txt 파일로 스토어 생성')
    print('7 - json 파일로 스토어 정보 출력')


    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요: ')
        if input1 == '1':
            store = create_store()
            store_list.append(store)
        elif input1 == '2':
            store = show_list()
        elif input1 == '3':
            store = show_store()
        elif input1 == '4':
            store = buy()
        elif input1 == '5':
            store = manager_product()
        elif input1 == '6':
            pass
        elif input1 == '7':
            pass
        else:
            print('존재하지 않는 명령어 입니다.')