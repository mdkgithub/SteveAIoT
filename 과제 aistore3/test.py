"""
스토어데이터프레임(s_df)는 'stores.csv’ 에 저장된 테이블형 스토어 데이터
    - 인덱스: 스토어아이디
    - 컬럼: 스토어아이디, 이름, 지역, 등록상품개수
재고데이터프레임(iv_df)는'inventory.csv’ 에 저장된 테이블형 재고 데이터
    - 인덱스: 순서
    - 컬럼: 상품아이디, 재고개수, 상품가격, 스토어아이디
상품데이터프레임(p_df)는'product.csv’ 에 저장된 테이블형 상품데이터
    - 인덱스: 상품아이디
    - 컬럼: 상품아이디, 상품이름
"""
import pandas as pd
import json

s_df = pd.read_csv('./stores.csv')
s_df = s_df.set_index('s_id', drop= False)
#print(s_df)

p_df = pd.read_csv('./products.csv')
p_df = p_df.set_index('p_id')
print(p_df)

iv_df = pd.read_csv('./inventory.csv')