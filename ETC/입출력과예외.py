import json

f = open('./test.txt', 'w', encoding="utf-8")
data = "안녕하세요"
f.write(data)
f.close()

t = open('./customers.txt', 'r', encoding="utf-8")
data = t.readlines()
t.close()
print(data)


# json 활용
file = open('./test.json','w')
json.dump(['foo',{'bar':('baz', None, 1.0,2)}],file)
file.close()


# bank.py에 json 활용

def customer_to_json():
