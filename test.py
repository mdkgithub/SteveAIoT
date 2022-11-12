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

# delivery[u_locate] = []
for order in orders:
    uid = order['user_id']
    u_name = users[uid][0]
    u_locate = users[uid][1]
    p_ids = order['products']

    # delivery = {}

    if u_locate not in delivery:
        delivery[u_locate] = []
    # print(delivery)

    for p in p_ids:
        if products[p]['count'] > 0:
            product = products[p]['name']
            delivery[u_locate].append((u_name, product))


print(delivery)