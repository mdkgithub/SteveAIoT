users = {123:['최원칠','관악구'],
         124:['이서혁','구로구'],
         125:['새싹','용산구'],
         126:['aiot','용산구']}
# print(users[124][1])

products = {'a':{'name':'노트북', 'count':10},
            'b':{'name':'자전거', 'count':10},
            'c':{'name':'샴푸', 'count':10},
            'd':{'name':'셔츠', 'count':0},
            'e':{'name':'초코렛', 'count':10}}

orders = [{'user_id':123, 'products':['a','c']},
          {'user_id':125, 'products':['e']},
          {'user_id':124, 'products':['b','d','e']},
          {'user_id':126, 'products':['a']}]

# 최원칠,[노트북, 샴푸]
# 새싹,[초코렛]
# 이서혁,[자전거, 셔츠, 초코렛]
# aiot,[노트북]

delivery = {}

# orders 리스트 안의 세부 데이터로 접근하기 위하여 for문을 사용하여 order 변수 설정
# order 변수를 사용해서 내부의 '' 와 '' 키에 접근해서 각각의 값을 가지는 변수 설정
for order in orders:
    user_id_list = order['user_id']
    products_list = order['products']

    # print(order['products'])


    # '' 값 정보를 가지고 users 키에 접근하여 값을 가져온다.
    # user 에는 각 딕셔너리의 값이 들어 있다.

    user = users[user_id_list]
    # print(user)
    # delivery[user[1]] = {}

    # print(user[1])

    for products_id in products_list:
        product = products[products_id]
        # print(products[products_id]['name'])
        # print(products[product])

        if product['count'] > 0:
            p_name = product['name']
            # print(p_name)

            p_order = order['products']
            # print(p_order)


            # 질문: 왜 안되는가? print(delivery[user[1]])
            # 주소에 따라 구매자와 상품 정보
            # 단. 셔츠 상품은 제외이기에 총 3개의 주문만 성립
            delivery[user[1]] = [(user[0], p_name)],[(user[0], p_name)]
            # delivery[user[1]].append(p_name)

            # dict = {}
            # dict["name"] = user[0]
            # dict["product"] = product
            # dict["locate"] = user[1]

# print(delivery)
            # delivery= delivery[user[1]].append(p_name)
            # 이름에 해당하는 상품은 모두 표기하는 방법


            # print(delivery[user[1]])
            # print(user[1])
            # print(p_name)

        # if delivery[user[1]] == user[1]:
            # print(user[1])
            # delivery[user[1]] = [(user[0], p_name),(user[0], p_name)]

            # else
            # if delivery[user[1]] == user[1]:
            # delivery[user[1]] = delivery[user[1]].append(delivery[user[1]])

                # else
                # delivery[user[1]] = [(user[0], p_name)]

            # print(p_name)
            # print(user[0], p_name)
        # print(product)


            # dict = user[1]
            # dict[] = product[1]
            # print(dict)
            # dict["locate"] = user[1]
    #
#         # delivery = []
#         # print(user[0], product, user[1])
#         # delivery.append(user[0], product, user[1])
#             delivery.append(dict)
#         print(delivery)
#
print(delivery)


# 관악구 : 최원칠,[노트북, 샴푸]
# 용산구 : 새싹,[초코렛]
# 구로구 : 이서혁,[자전거, 셔츠, 초코렛]
# 용산구 : aiot,[노트북]


# {'관악구': [('최원칠', '노트북'), ('최원칠', '샴푸')],
#  '용산구': [('새싹', '초코렛'), ('aiot', '노트북')],
# '구로구': [('이서혁', '자전거'), ('이서혁', '초코렛')]}