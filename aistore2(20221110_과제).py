class AiStore:

    def __init__(self, name, s_id, locate):
        self.name = name
        self.s_id = s_id
        self.locate = locate
        self.products = {'커피':10}
        self.prices = {'커피':1000}


    def set_product(self, product_count, product_price, total_product_price):
        info = input('상품개수: ')
        total_product_price = product_price * info

        if product_count > 0:
                product_count += product_count
            up_product_price = product_price

        else product_count < 0:
            self.products = {'커피': 10}
            self.prices = {'커피': 1000}


    def buy_product(self, product, count, amount):
        self.products -= self.products
        self.amount = self.products * count

        if self.count < count :
            print('재고가 부족합니다')
            return
        total_price = count * self.amount

        if amount < total_price :
            print('금액이 부족합니다')
            return

        self.count -= count
        changes = amount - total_price
        print('잔돈은 %i입니다' % changes)


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
    ~
    print('{} 스토어가 생성 되었습니다.'.format(store.get_name()))
    return ~


def show_list():
    for store in store_list:
        print('스토어 이름:{} 스토어 아이디:{} 스토어 위치:{}'
              .format(~,
                      ~,
                      ~
                      ))

def search_store(s_id):
    ~

    print('스토어 아이디를 찾지 못했습니다.')
    return None


def show_store():
    s_id = input('스토어 아이디 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    print('{} 스토어 재고 현황: {}'
          .format(~,
                  ~
                  ))
    print('{} 스토어 가격 현황: {}'
          .format(~,
                  ~
                  ))

def buy():
    s_id = input('스토어 아이디 입력: ')
    ~
    product = input('상품 입력:')
    count = input('구매 개수 입력: ')
    # 옵션 '총 가격은 {} 입니다.' 출력
    price = input('가격 입력: ')
    ~

def manager_product():

    s_id = input('스토어 번호 입력: ')
    ~

    product = input('상품 입력: ')
    count = input('재고 개수 입력: ')
    price = input('상품 가격 입력: ')

    store.set_product(~)

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
            ~
        elif input1 == '2':
            ~
        elif input1 == '3':
            ~
        elif input1 == '4':
            ~
        elif input1 == '5':
            ~
        elif input1 == '6':
            pass
        elif input1 == '7':
            pass
        else:
            print('존재하지 않는 명령어 입니다.')