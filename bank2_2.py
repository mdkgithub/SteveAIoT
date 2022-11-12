class Customer:

    def __init__(self, name, c_id):
        self.name = name
        self.c_id = c_id
        # 딕셔너리 구조로 계좌 여러개 저장
        self.accounts = {}

    #해당 계좌에 금액 추가
    def add_amount(self, a_id, amount):
        if a_id in self.accounts:
            self.accounts[a_id] += amount
        else:
            print('해당 계좌가 없습니다')

    #해당 계좌에서 금액 제거
    def sub_amount(self, a_id, amount):
        if a_id in self.accounts:
            if self.accounts[a_id] > amount:
                self.accounts[a_id] -= amount
            else:
                print('계좌의 금액이 부족합니다.')
        else:
            print('해당 계좌가 없습니다.')

    #계좌 딕셔너리에 계좌 추가 (0으로 초기화)
    def add_account(self, a_id):
        if a_id in self.accounts:
            print('해당 계좌가 이미 존재합니다')
        else:
            self.accounts[a_id] = 0

    # 전체 계좌금액 합계
    def get_total_amount1(self,):
        total_amount = 0
        for a_id in self.accounts:
            total_amount += self.accounts[a_id]

        return total_amount

    def get_total_amount2(self,):
        amounts = []
        for a_id in self.accounts:
            amounts.append(self.accounts[a_id])

        return sum(amounts)

    def get_rat(self):
        total_amount = self.get_total_amount1()
        if total_amount > 100000:
            rat = 'vvip'
        elif total_amount > 10000:
            rat = 'vip'
        elif total_amount > 1000:
            rat = 'gold'
        elif total_amount > 100:
            rat = 'silver'
        else:
            rat = 'bronze'

        return rat

    def get_name(self):
        return self.name

    def get_id(self):
        return self.c_id

    def get_all_accounts(self):
        return self.accounts


def create_customer():
    c_name = input('고객 이름 입력:')
    c_id = input('고객 번호 입력:')
    customer = Customer(c_name, c_id)
    print('{} 고객이 생성 되었습니다.'.format(customer.get_name()))
    return customer


def show_list():
    for customer in customer_list:
        print('고객이름:{} 고객번호:{}'
              .format(customer.get_name(),
                      customer.get_id(),
                      ))

def search_customer(c_id):
    for customer in customer_list:
        if customer.get_id() == c_id:
            print('고객이름:{} 고객번호:{}'
                  .format(customer.get_name(),
                          customer.get_id()
                          ))
            return customer

    print('고객 번호를 찾지 못했습니다.')
    return None

def create_acount():
    print('고객 번호 입력:')
    c_id = input()
    customer = search_customer(c_id)
    if customer is None:
        return

    print('계좌번호 입력:')
    acount_num = input()
    customer.add_account(acount_num)
    print('{} 고객의 {} 계좌가 등록되었습니다'
          .format(customer.get_name(),
                  acount_num,
                  ))


def show_customer():
    print('고객 번호 입력:')
    c_id = input()
    customer = search_customer(c_id)
    if customer is None:
        return

    print('{} 고객님 등급:{} 총금액:{} 계좌정보:{}'
          .format(customer.get_name(),
                  customer.get_rat(),
                  customer.get_total_amount1(),
                  customer.get_all_accounts()
                  ))

def deposit():
    print('고객 번호 입력:')
    c_id = input()
    customer = search_customer(c_id)
    if customer is None:
        return

    print('계좌번호 입력:')
    acount_num = input()
    print('입금할 금액 입력:')
    amount = input()
    customer.add_amount(acount_num, int(amount))

def withdraw():
    print('고객 번호 입력:')
    c_id = input()
    customer = search_customer(c_id)
    if customer is None:
        return

    print('계좌번호 입력:')
    acount_num = input()
    print('출금할 금액 입력:')
    amount = input()
    customer.sub_amount(acount_num, int(amount))


# open()함수를 이용하여 customers.txt 파일 데이터 불러오기
# customers.txt 파일의 줄바꿈 기준으로 이름과 아이디를 가지는 고객리스트 생성
# readlines() 함수와 for 문을 이용할것
# customer_list 리스트에 Customer 객체로 담길것

# import json
def txt_to_customers():
    file = open('./customers.txt', 'r', encoding="utf-8")

    data = file.readlines()
    file.close()

    for item in data:
        # split(x): 문자열을 x 문자 구분으로 리스트로 치환
        # strip(): 문자열의 앞,뒤 공백 제거

        item = item.strip().split(" ")
        print(item)

        customer = Customer(item[0],item[1])
        customer_list.append(customer)



# 모듈 최상 위에 json 모듈 import
# customer_to_json 함수 생성
# 딕셔너리 구조를 활용하여 다음 구조를 만든후 입력받은 path로 json으로 저장
# 계좌생성 옵션 최소 2번이상 실행후 해당 계좌가 들어간 상태로 저장 되어야함

# *[{'name': '최원칠', 'c_id': '123', 'rating': 'bronze', 'total_amount': 0, 'accounts': {'1251': 0}},*
# *{'name': '이서혁', 'c_id': '124', 'rating': 'bronze', 'total_amount': 0, 'accounts': {'3463': 0}},*
# *{'name': '감바스', 'c_id': '125', 'rating': 'bronze', 'total_amount': 0, 'accounts': {}},*
# *{'name': '웨하스', 'c_id': '126', 'rating': 'bronze', 'total_amount': 0, 'accounts': {}},*
# *{'name': '초코하임', 'c_id': '127', 'rating': 'bronze', 'total_amount': 0, 'accounts': {}}]*

import json
def customer_to_json():

    customerlist = []

    for customer in customer_list:
            dict = {}
            dict["name"] = customer.get_name()
            dict["c_id"] = customer.get_id()
            dict["rating"] = customer.get_rat()
            dict["total_amount"] = customer.get_total_amount1()
            dict["accounts"] = customer.get_all_accounts()

            customerlist.append(dict)

    file = open('./test.json', 'w')
    json.dump(customerlist, file)
    file.close()


if __name__ == '__main__':
    customer_list = []

    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요')
        if input1 == '1':
            customer = create_customer()
            customer_list.append(customer)
        elif input1 == '2':
            create_acount()
        elif input1 == '3':
            deposit()
        elif input1 == '4':
            withdraw()
        elif input1 == '5':
            show_list()
        elif input1 == '6':
            show_customer()
        elif input1 == '7':
            txt_to_customers()
        elif input1 == '8':
            customer_to_json()
        else:
            print('존재하지 않는 명령어 입니다.')