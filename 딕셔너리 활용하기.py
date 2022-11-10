name = ['최원칠','이서혁','aiot','새싹']
age = [30,29,34,72]
n_id = [125,2474,341,646]


order = []
totalage = 0
# for i in range(len(name)):
for i in range(0,4):
    # for ages in age:
    #     for n_ids in n_id:
    # dict = {}
    # dict["name"] = name[i]
    # dict["age"] = age[i]
    # dict["id"] = n_id[i]
    dict2 = {"name": name[i], "age": age[i], "id": n_id[i]}

    # if name[i] == '새싹':
    #     dict2["age"]=35


    totalage += age[i]
    # order.append(dict)
    order.append(dict2)

for i in range(4):
    if name[i] == '새싹':
        order[i]["age"]=35

# index = 0
# for n in name:
#     print(index)
#     index += 1
print('Total Age: ', totalage)
print(order)



# a. 다음과같은3개의리스트가있다.
# i. ['최원칠','이서혁','aiot','새싹']
# ii. [30,29,34,72]
# iii. [125,2474,341,646]
# b. for문을이용하여3개의리스트를다음과같은리스트-딕셔너리구조를만들어라
# i. [{'name':'최원칠','age':30,'id':125},{'name':'이서혁','age':29,'id':2474},{'name':
# 'aiot','age':34,'id':341},{'name':'새싹','age':72,'id':646}]
# c. 전체age의총합을자유롭게구해라
# i. 165
# d. for문과if문을이용하여새싹의나이를35로바꾸어라
# i. {'name':'새싹','age':35,'id':646}