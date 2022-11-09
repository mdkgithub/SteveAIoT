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

print(users)

for n_id, ps in users:
     print(n_id)

# print(search_users)
# for name in sorted(users.keys()):
# for name in sorted(users.values()):
#         print(name)

# print(users)

products = {'a':'노트북',
            'b':'자전거',
            'c':'샴푸',
            'd':'셔츠',
            'e':'초코렛'}
#
# # print(products)
#
orders = [{'user_id':123, 'products':['a','c']},
         {'user_id':125, 'products':['e']},
         {'user_id':124, 'products':['b','d','e']}]

# for order_dic in orders:
#     order_dic_value = order_dic.values()
#     print(order_dic_value)

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