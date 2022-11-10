users = {123:['최원칠','관악구'],
         124:['이서혁','구로구'],
         125:['새싹','용산구'],
         126:['aiot','용산구']}

products = {'a':{'name':'노트북', 'count':10},
            'b':{'name':'자전거', 'count':10},
            'c':{'name':'샴푸', 'count':10},
            'd':{'name':'셔츠', 'count':0},
            'e':{'name':'초코렛', 'count':10}}

orders = [{'user_id':123, 'products':['a','c']},
          {'user_id':125, 'products':['e']},
          {'user_id':124, 'products':['b','d','e']},
          {'user_id':126, 'products':['a']}]


delivery = {}

for order in orders:
    user_id_list = order['user_id']
    products_list = order['products']

    user = users[user_id_list]
    delivery[user[1]] = {}
    # user[0]
    # print(user[1])

    for products_id in products_list:
        product = products[products_id]
        if product['count'] > 0:
            p_name = product['name']
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
# print(delivery)

# delivery = {}
# ~
print(delivery)



# {'관악구': [('최원칠', '노트북'), ('최원칠', '샴푸')],
#  '용산구': [('새싹', '초코렛'), ('aiot', '노트북')],
# '구로구': [('이서혁', '자전거'), ('이서혁', '초코렛')]}