class C_Customer:

    def __init__(self, name, c_id):
        self.name = name
        self.c_id = c_id
        self.accounts = {}
        # 딕셔너리 구조로 계좌 여러개 저장

    #해당 계좌에 금액 추가
    def add_amount(self, account, input_money):
        self.accounts[account] += input_money


    #해당 계좌에서 금액 제거
    def sub_amount(self, account, output_money):
        self.accounts[account] -= output_money


    #계좌 딕셔너리에 계좌 추가 (0으로 초기화)
    def add_account(self, account):
        self.accounts[account] = 0


    # 전체 계좌금액 합계하는 함수 생성
    def get_total_amount1(self):
        total_amount = 0
        for total in self.accounts:
            total_amount += self.accounts[total]
        return total_amount


    def get_rat(self):
        amount = self.get_total_amount1()
        customer_rate = 'normal'

        if amount > 1000:
            customer_rate = 'silver'
            print('고객 등급은',customer_rate,'입니다.')

        elif amount > 2000:
            customer_rate = 'gold'
            print('고객 등급은', customer_rate, '입니다.')

        elif amount > 3000:
            customer_rate = 'Diamond'
            print('고객 등급은', customer_rate, '입니다.')

        else :
            return customer_rate


    def get_name(self):
        return self.name


    def get_id(self):
        return self.c_id


    # 전체 계좌 반환하는 함수 생성
    def get_all_accounts(self):
        return self.accounts



def create_customer():
    c_name = input('고객 이름 입력:')
    c_id = input('고객 번호 입력:')

    # 고객 인스턴스 생성
    customer = C_Customer(c_name,c_id)

    print('{} 고객이 생성 되었습니다.'.format(customer.get_name(),customer.get_id()))
    return customer



def show_list():
    for customer in customer_list:
        # print('고객이름:', before_customer.name, '고객번호:', before_customer.c_id)
        print('고객이름:', customer.get_name(), '고객번호:', customer.get_id())


def search_customer(c_id):

    for person in customer_list:
        if c_id == person.get_id():
            print('고객이름:{} 고객번호:{}'.format(person.get_name(),person.get_id()))
            return person

        else:
            print('고객 번호를 찾지 못했습니다.')
    return None


def create_acount():
    c_id = input('고객 번호 입력:')
    # search_customer 사용하여 고객을 못찾으면 함수 끝냄

    customer = search_customer(c_id)

    if customer == None:
        return

    acount_num = input('계좌번호 입력:')
    # 계좌 등록

    customer.add_account(acount_num)

    print('{} 고객의 {} 계좌가 등록되었습니다'.format(customer.get_name(),acount_num))


def show_customer():
    c_id = input('고객 번호 입력:')
    # search_customer 사용하여 고객을 못찾으면 함수 끝냄

    customer = search_customer(c_id)
    if customer == None:
        return

    print('{} 고객님 등급:{} 총금액:{} 계좌정보:{}'
          .format(customer.get_name(),
                  customer.get_rat(),
                  customer.get_total_amount1(),
                  customer.get_all_accounts()
                  ))


def deposit():
    c_id = input('고객 번호 입력:')
    # search_customer 사용하여 고객을 못찾으면 함수 끝냄

    customer = search_customer(c_id)
    if customer == None:
        return

    acount_num = input('계좌번호 입력:')
    amount = input('입금할 금액 입력:')

    # 계좌에 입금
    customer.add_amount(acount_num,int(amount))


def withdraw():
    c_id = input('고객 번호 입력:')
    # search_customer 사용하여 고객을 못찾으면 함수 끝냄

    customer = search_customer(c_id)
    if customer == None:
        return

    acount_num = input('계좌번호 입력:')
    amount = input('출금할 금액 입력:')

    # 계좌에 출금
    customer.sub_amount(acount_num, int(amount))


if __name__ == '__main__':
    customer_list = []

    print('1 - 고객 생성')
    print('2 - 계좌 생성')
    print('3 - 입금')
    print('4 - 출금')
    print('5 - 생성된 고객 리스트 출력')
    print('6 - 고객 정보 출력')


    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요')
        if input1 == '1':
            customer = create_customer()
            #리스트에 고객 추가
            customer_list.append(customer)

        elif input1 == '2':
            create_acount()
            #리스트에 계좌 생성


        elif input1 == '3':
            deposit()
            #리스트에 입금

        elif input1 == '4':
            withdraw()
            #리스트에 출금


        elif input1 == '5':
            show_list()
            #리스트에 생성된 고객 리스트 출력

        elif input1 == '6':
            show_customer()
            #리스트에 고객 정보 출력

        else:
            print('존재하지 않는 명령어 입니다.')
