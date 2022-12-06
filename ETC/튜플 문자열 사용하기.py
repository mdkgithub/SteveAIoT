def abc():
    a = 1
    b = 2
    c = 'c'
    return a,b,c

t = abc()
print(t)


s = '제 나이는 {}살 입니다'.format(30)
print(s)

r = '나는 빨리 집에 가고 싶다'
sl = r.split(' ')
print(sl)


g = '나는 빨리 집에 가고 싶다'
sl = '-'.join(sl)
print(sl)

q = '나는 빨리 집에 가고 싶다'
sl = q.encode('utf-8')
print(sl)

y = '나는 빨리 집에 가고 싶다'
sl = y.split(sl)
print(sl)

