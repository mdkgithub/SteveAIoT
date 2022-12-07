"""
sample_products = {"apple": 1000, "orange": 100, "banana": 50}
# product = "apple"
# sample_products[product] # 1000
# sample_products[product] += 50 # {"apple": 1050, "orange": 100, "banana": 50}
print(sample_products['apple'])
print(sample_products.values().)
"""

class AiStore:

    def __init__(self, name, s_id, locate, p_id):
        self.name = name
        self.s_id = s_id
        self.locate = locate
        self.products = {'커피':10}
        self.prices = {'커피':1000}
        self.p_id = p_id


    def set_product(self, product, count, price):
        if product in self.products:
            self.products[product] += count
            self.prices[product] = price
        else:
            self.products[product] = count
            self.prices[product] = price
            return


    # def get_p_id(self):
    #     product = self.products[self.products['p_id'] == p_id]
    #     # 질문8: 14번째 줄에서 사용한 함수이다. 동일하게 다시 사용한 이유는 ?
    #     # if len(product) == 0:
    #     return self.p_id


    def buy_product(self, product, count, amount):
        # 제품 수량이 재고 수량보다 작은면
        # 구매한 제품 가격이 지불한 금액보다 작으면
        # 재고에서 구매한 제품 수량만큼 차감하고
        # 잔돈은 지불한 금액에서 구매한 제품 가격을 뺀다

        # p_id를 사용해서 다시 변경해볼것

        if product in self.products:
        #if self.products['product'] == product:

            if count < self.products[product]:

                # p_id 설정으로 물품명 있는지 확인
                # product = self.products[self.products['p_id'] == p_id]
                # if len(product) == 0:
                #     print('상품이 존재하지 않습니다.')
                #     return

                if count * self.prices[product] < amount:
                    self.products[product] -= count
                    changes = amount - count * self.prices[product]
                    print('잔돈은 ' + str(changes))

                else :
                    print('금액이 부족합니다.')

        else:
            print('상품 재고가 부족합니다.')


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

    p_id = input('상품명 입력: ')

    # 클래스에 있는 생성자를 사용하여 새로운 변수에 할당
    store = AiStore(s_name, s_id, locate, p_id)

    print('{} 스토어가 생성 되었습니다.'.format(store.get_name()))
    return store


def show_list():
    for store in store_list:
        print('스토어 이름:{} 스토어 아이디:{} 스토어 위치:{}'
              .format(store.get_name(),store.get_id(),store.get_locate()))


def search_store(s_id):
    for store in store_list:
        if store.get_id() == s_id:
            return store
        print('스토어 아이디를 찾지 못했습니다.')
        return None



def show_store():
    s_id = input('스토어 아이디 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    print('{} 스토어 재고 현황: {}'.format(store.get_name(),store.get_products()))
    print('{} 스토어 가격 현황: {}'.format(store.get_name(),store.get_prices()))


def buy():
    s_id = input('스토어 아이디 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    product = input('상품 입력:')
    count = input('구매 개수 입력: ')
    count = int(count)
    # 옵션
    # 상품의 가격을 가져오는 함수에서 상품 가격 업데이트
    if product in store.get_products():
        print('총 가격은 {} 입니다.'.format(store.get_prices()[product] * count))

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



# def txt_to_store():
#     pass


import json
# def store_to_json():
#     pass


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



"""
class AiStore:

    def __init__(self, name, s_id, locate):
        self.name = name
        self.s_id = s_id
        self.locate = locate
        self.products = {'커피':10}
        self.prices = {'커피':2000}

    def set_product(self, product, count, price):

        if product in self.products:
            self.products[product] += count
            self.prices[product] = price
        else:
            self.products[product] = count
            self.prices[product] = price

    def buy_product(self, product, count, amount):
        if count < self.products[product]:
            if count * self.prices[product] < amount:
                self.products[product] -= count
                changes = amount - count * self.prices[product]
                print('잔돈은 ' + str(changes))
            else:
                print('금액이 부족합니다.')
        else:
            print('재고가 부족합니다.')


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
        print('스토어 이름:{} 스토어 아이디:{} 스토어 위치:{}'
              .format(store.get_name(),
                      store.get_id(),
                      store.get_locate()
                      ))

def search_store(s_id):
    for store in store_list:
        if store.get_id() == s_id:
            return store

    print('스토어 아이디를 찾지 못했습니다.')
    return None


def show_store():
    s_id = input('스토어 아이디 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    print('{} 스토어 재고 현황: {}'
          .format(store.get_name(),
                  store.get_products()
                  ))
    print('{} 스토어 가격 현황: {}'
          .format(store.get_name(),
                  store.get_prices()
                  ))

def buy():
    s_id = input('스토어 아이디 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    product = input('상품 입력:')
    count = input('구매 개수 입력: ')
    count = int(count)
    # 옵션
    if product in store.get_products():
        print('총 가격은 {} 입니다.'.format(store.get_prices()[product] * count))

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

    store.set_product(product, int(count), int(price))

def txt_to_store():
    path = input('파일 경로입력: ')

    with open(path, 'r', encoding='utf-8') as f:
        for data in f.readlines():
            sdata = data.split(' ')
            print(sdata)
            store_list.append(
                AiStore(sdata[0].strip(), sdata[1].strip(), sdata[2].strip())
            )


import json
def store_to_json():
    path = input('파일 경로입력: ')

    json_data = []

    for s in store_list:
        s_dict = {
            'name': s.get_name(),
            's_id': s.get_id(),
            'locate': s.get_locate(),
            'products': s.get_products(),
            'prices': s.get_prices()
        }
        json_data.append(s_dict)

    with open(path, 'w') as f:
        json.dump(json_data,f)

    f.close()
    print(json_data)

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
            show_list()
        elif input1 == '3':
            show_store()
        elif input1 == '4':
            buy()
        elif input1 == '5':
            manager_product()
        elif input1 == '6':
            txt_to_store()
        elif input1 == '7':
            store_to_json()
        else:
            print('존재하지 않는 명령어 입니다.')
"""