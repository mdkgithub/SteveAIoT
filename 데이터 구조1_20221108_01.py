# d = {'a':1, 'b':2, 'c':3}
# print(d['a'])
#
# d['d'] = 4
# print(d)
#
# d['e'] = 5
# print(d)
#
# t = d.get('f',5)
# print(t)
#
# c = list(d)
# print(c)

# c = {'a':1,'b':2,'c':3}
# c['x'] = 0
# c['y'] = 25
# c['z'] = 30
# print(c)

# alien_0 = {'color':'green', 'points':5}
# print(alien_0)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# d = dict(a=1, b=2, c=3)
# print(d)


users = {123:['최원칠','관악구'],
         124:['이서혁','구로구'],
         125:['새싹','용산구']}

products = {'a':'노트북',
            'b':'자전거',
            'c':'샴푸',
            'd':'셔츠',
            'e':'초코렛'}

orders = [{'user_id':123, 'products':['a','c']},
         {'user_id':125, 'products':['e']},
         {'user_id':124, 'products':['b','d','e']}]

delivery = []

for order in orders:
    user_id_list = order['user_id']
    products_list = order['products']

    user = users[user_id_list]

    for products_id in products_list:
        product = products[products_id]

        dict = {}
        dict["name"] = user[0]
        dict["product"] = product
        dict["locate"] = user[1]

        # delivery = []
        # print(user[0], product, user[1])
        # delivery.append(user[0], product, user[1])
        delivery.append(dict)

print(delivery)






# for users in user:
#     print('name:', user,'product:', product, 'locate:',user )


    # print(delivery)

    # print(delivery)

    # for product_num in products :
        # print(product_num)



    # for u_id, ps in order:
    #     if u_id == user():


# [ {'name': '최원칠', 'product': '노트북', 'locate': '관악구'},
#
# {'name': '최원칠', 'product': '샴푸', 'locate': '관악구'},
#
# {'name': '새싹', 'product': '초코렛', 'locate': '용산구'},
#
# {'name': '이서혁', 'product': '자전거', 'locate': '구로구'},
#
# {'name': '이서혁', 'product': '셔츠', 'locate': '구로구'},
#
# # {'name': '이서혁', 'product': '초코렛', 'locate': '구로구'} ]

# for id, ps in orders:
#     print(id)
    # for ps_1 in ps:
    #     print(ps_1.title())

# print(orders[0].keys())

# delivery = [
#     users,
#     products,
#     orders,
#     ]

# print(delivery)


# for order in orders:
#     for id, pd in order():
#         if id.value() == users.keys():

# for sub_list in my_list3:
#     for j, v in enumerate(sub_list):
#         if v in my_list2:
#             sub_list[j] = '*'
# print(my_list3)


# print(delivery)