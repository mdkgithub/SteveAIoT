import numpy as np

mat3 = [1,2,'a']
mat3 = np.asarray(mat3)
print(mat3, type(mat3))


rand1 = np.random.rand(5,10)
sub1 = rand1[0][0:3]
print(rand1)
# print("###"*10)
sub_rand1 = np.concatenate((rand1[0][0:3],rand1[1][4:6]), axis=0)
print(sub_rand1)
print(sub_rand1.shape)


print("---"*10)
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]
]

# 1번 축의 가장 큰 값 추출
amat = np.asarray(matrix)
max_mat1 = np.max(amat, axis=1)
print(max_mat1)

print("---"*10)

#  0번 축의 가장 큰 값 추출
max_mat2 = np.max(amat, axis=0)
print(max_mat2)
#

# (5,6)의 모양을 가지는 랜덤한 배열을 생성하고
# b의(5,10)모양의 배열과 1번축을 합쳐 주어라 최종 모양은(5,16)이되어야한다.
rand2 = np.random.rand(5,6)
# rand1 = np.random.rand(5,10)
cat_rand = np.concatenate((rand2,rand1), axis=1)
# cat_rand = np.sum(amat, axis=1)
print(cat_rand)
print(cat_rand.shape)