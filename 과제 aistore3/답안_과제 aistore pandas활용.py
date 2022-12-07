import pandas as pd
import json

class AiStore:

    def __init__(self, name, s_id, locate, products_num, inventory):
        self.name = name
        self.s_id = s_id
        self.locate = locate
        self.products_num = products_num
        self.inventory = inventory

    def is_product(self, p_id):
        product = self.inventory[self.inventory['p_id'] == p_id]
        if len(product) == 0:
            return False
        else:
            return True

    def add_product(self, p_id, count, price, idx):
        # 인덱스가 재할당이 안되게 코드를 짜주는것이 정적으로 데이터를 사용하는데엔 좋음
        # 데이터 분석을 위한 용도에는 컷캣등의 함수를 사용해도 무관
        # pandas 의 사용목적은 데이터보관(DB)의 목적보단 보관된 데이터의 분석 목적이 더 강함
        n_product = {'p_id': p_id, 'count': count, 'price': price, 's_id': self.s_id}
        self.inventory.loc[idx] = n_product
        self.products_num = len(self.inventory)
        return n_product
    def set_product(self, p_id, count, price):
        # if in 을 사용하기위해선 시리즈를 배열로 바꿔야할것 문서 참고
        # try 문사용 가능
        # 쿼리후 개수로 파악 가능
        product =  self.inventory[self.inventory['p_id'] == p_id]
        product['count'] += count
        product['price'] = price
        self.inventory.update(product)

    def buy_product(self, p_id, count, amount):
        product =  self.inventory[self.inventory['p_id'] == p_id]

        if len(product) == 0:
            print('상품이 존재하지 않습니다.')
            return

        product = product[product['count'] > count]
        if len(product) == 0:
            print('재고가 부족합니다')
            return

        product = product[product['price']*count <= amount]
        if len(product) == 0:
            print('가격이 부족합니다.')
            return

        changes = amount - count * product['price']
        print('잔돈은 {}'.format(changes.iloc[0]))
        product['count'] -= count
        self.inventory.update(product)

    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_products_num(self):
        return self.products_num
    def show_products(self, p_df):
        for product in self.inventory.iloc:
            p_id = product['p_id']
            p_name = p_df.loc[p_id,'product']
            price = product['price']
            count = product['count']
            print('상품명:{} - 가격:{} (재고{}) id:{}'.format(p_name, int(price), int(count), p_id))

    def get_price(self, p_id):
        product =  self.inventory[self.inventory['p_id'] == p_id]
        if len(product) == 0:
            return None

        return product['price'].iloc[0]

    def update_data(self, s_df, iv_df):
        s_df[self.s_id] = {'s_id': self.s_id,
                           'name': self.name,
                           'locate': self.locate,
                           'products_num': self.products_num,}

        # update 함수보단 for 문을 통한 loc 방식이 더 좋다고 판다스가 말함
        # iv_df.update(self.inventory)
        for idx in self.inventory.index:
            iv_df.loc[idx] = self.inventory.loc[idx]

def create_store():
    s_name = input('스토어 이름 입력: ')
    s_id = input('스토어 번호 입력: ')
    locate = input('스토어 위치 입력: ')
    store = {'s_id': s_id, 'name': s_name,
             'locate': locate,
             'products_num': 0,}

    s_df.loc[s_id] = store
    print('{} 스토어가 생성 되었습니다.'.format(store['name']))


def show_list():
    for store in s_df.iloc:
        print('스토어 이름:{} 스토어 번호:{} 스토어 위치:{}'
              .format(store['name'],
                      store['s_id'],
                      store['locate']
                      ))

def search_store(s_id):
    if s_id in s_df.index:
        store = s_df.loc[s_id]
        inventory = iv_df[iv_df['s_id'] == s_id]
        return AiStore(store['name'],
                       store['s_id'],
                       store['locate'],
                       store['products_num'],
                       inventory)
    else:
        print('스토어를 찾지 못했습니다.')
        return None


def show_store():
    s_id = input('스토어 번호 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    print('{}스토어 위치:{} 등록상품:{}'
          .format(store.get_name(),
                  store.get_locate(),
                  store.get_products_num(),
                  ))

    store.show_products(p_df)
def buy():
    s_id = input('스토어 번호 입력: ')
    store = search_store(s_id)
    if store is None:
        return
    print('구매 가능 상품')
    store.show_products(p_df)

    p_id = input('상품 아이디 입력:')
    count = input('구매 개수 입력: ')
    count = int(count)
    # 옵션
    price = store.get_price(p_id)
    if price is not None:
        print('총 가격은 {} 입니다.'.format(price * count))

    price = input('가격 입력: ')
    price = int(price)
    store.buy_product(p_id, count, price)
    store.update_data(s_df,iv_df)
def manager_product():

    s_id = input('스토어 번호 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    print('등록 가능 상품')
    print(p_df)
    p_id = input('상품 아이디 입력: ')
    count = input('재고 개수 입력: ')
    price = input('상품 가격 입력: ')

    if store.is_product(p_id):
        store.set_product(p_id, int(count), int(price))
        store.update_data(s_df,iv_df)
    else:
        idx = len(iv_df)
        n_product = store.add_product(p_id, int(count), int(price), idx)
        iv_df.loc[idx] = n_product


import json
def products_counts():
    ivp_df = iv_df.merge(p_df, on='p_id')
    pc_df = ivp_df[['product','count']].groupby(by = 'product').sum()
    print(pc_df)

if __name__ == '__main__':

    s_df = pd.read_csv('./stores.csv')
    s_df = s_df.set_index('s_id', drop= False)
    p_df = pd.read_csv('./products.csv')
    p_df = p_df.set_index('p_id')
    iv_df = pd.read_csv('./inventory.csv')


    print('1 - 스토어 생성')
    print('2 - 스토어 리스트 출력')
    print('3 - 스토어 정보 출력')
    print('4 - 상품 구매')
    print('5 - 상품 관리')
    print('6 - csv 파일로 스토어, 재고현황 파일 출력')
    print('7 - 상품명별 전체 재고 개수 출력')


    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요: ')
        if input1 == '1':
            create_store()
        elif input1 == '2':
            show_list()
        elif input1 == '3':
            show_store()
        elif input1 == '4':
            buy()
        elif input1 == '5':
            manager_product()
        elif input1 == '6':
            s_df.to_csv('store_v2.csv', index= False)
            iv_df.to_csv('inventory_v2.csv', index= False)
        elif input1 == '7':
            products_counts()
        else:
            print('존재하지 않는 명령어 입니다.')