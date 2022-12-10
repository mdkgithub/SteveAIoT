#!/usr/bin/env python
# coding: utf-8

# In[1]:


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
#cred = credentials.Certificate('./aiot-nuguna-03687aeaa9e6.json')
cred = credentials.Certificate('./steveproject-1dad4-90d56d068c60.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


# In[3]:


# 데이터 추가
doc_ref = db.collection('customer').document('c1')
doc_ref.set({
    'c_id': 'c1',
    'name': '최원칠',
    'total_amount':500,
    'rat': 'silver',
    'test':'test'
})


# In[4]:


# 데이터 id로 읽기
doc_ref = db.collection('customer').document('c1')

doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such document!')


# In[5]:


# 데이터 전체 읽기
users_ref = db.collection('customer')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')


# In[6]:


# 데이터 쿼리
cities_ref = db.collection('customer')
q = cities_ref.where('total_amount', '<=', 1000).stream()
for doc in q:
    print(f'{doc.id} => {doc.to_dict()}')

#.whrere


# In[16]:


# 데이터 업데이트
doc_ref = db.collection('customer').document('c1')

doc_ref.update({'account_num': 1,
                'accounts':{'11a':{'a_id':'11a', 'c_id':'c1', 'amount':100}}
               })

doc_ref = db.collection('customer').document('c1')

doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such document!')


# In[17]:


# 데이터 업데이트
doc_ref = db.collection('customer').document('c1')

# 특수 필드 사용
# 특정 맵의 필드를 추가하기위해 < 맵.필드 : 값 > 사용
doc_ref.update({'account_num': firestore.Increment(1),
                'total_amount' : firestore.Increment(400)
                'edit_time': firestore.SERVER_TIMESTAMP,
                'accounts.12a':{'a_id':'12a', 'c_id':'c1', 'amount':400}
               })

doc_ref = db.collection('customer').document('c1')

doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such document!')


# In[2]:


# py파일 또는 ipynb 파일 새로 생성하여 진행
# 파이어스토어 db 인스턴스 생성
# bank4.json 파일내의 데이터를 파이어스토어 customer 컬렉션에 고객 아이디를 아이디로 가지는 문서들로 추가
# {아이디: 5c, 이름: 본인이름, 계좌개수:0, 총금액:0, 등급:normal, 계좌:비어있는 딕셔너리} 고객 customer 컬렉션에 추가
# 5c 고객에 임의의 계좌 추가 (고객의 계좌, 총금액, 계좌개수, 등급, 수정시간 업데이트되어야함)
# 계좌개수, 총금액은 firestore.Increment() 사용

import json

bank4.jason = input(': ')

firestore_dbinstance = []

with open('bank4.json','r') as f:
    data = json.load(f)



# In[19]:


# 트랜젝션

transaction = db.transaction()
doc_ref = db.collection('customer').document('c1')

@firestore.transactional
def update_in_transaction(transaction, doc_ref):
    snapshot = doc_ref.get(transaction=transaction)
    total_amount = snapshot.get('total_amount')
    ntotal_amount = total_amount + 1000
    
    transaction.update(doc_ref, {
            'total_amount': ntotal_amount
        })
    
    return ntotal_amount

result = update_in_transaction(transaction, doc_ref)
result


# In[ ]:




