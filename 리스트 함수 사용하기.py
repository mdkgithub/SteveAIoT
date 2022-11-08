# my_list1 = []
#
# for i in range(10,16):
#     my_list1.append(i)
# print(my_list1)
#
# my_list1.extend([9,8,7])
# print(my_list1)
#
# my_list1.sort()
# print(my_list1)


# 중첩리스트 다루기
my_list2 = [3,6,13,15,18]
my_list3 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]


for x in range(len(my_list3)):
    for y in range(len(my_list3[x])):
        if my_list3[x][y] in my_list2:
            my_list3[x][y] = '*'

print(my_list3)


for sub_list in my_list3:
    for j, v in enumerate(sub_list):
        if v in my_list2:
            sub_list[j] = '*'
print(my_list3)