"""
import requests

url='http://apis.data.go.kr/1360000/WthrWrnInfoService/getWthrWrnList'
params={'serviceKey':4,
'RyU8vp09GyAdmsH9z57XcTivzDrtN2nO52XqA8t4yZW+rEuNZKNDmrtTidRCdf2xh5xV3PgBNBiCkGbtgjraDg==',
    'pageNo':'1','numOfRows':'30',
    'dataType':'JSON','stnId':'108','fromTmFc':'20221201','toTmFc':'20221205'}

response=requests.get(url,params=params)
result=response.json()
result
"""

import requests

url='http://apis.data.go.kr/1360000/WthrWrnInfoService/getWthrWrnList'
params={'serviceKey':"5OgHKjPty2bs+dF/mYpspYDevQkc8STApOKWgbcP7xBtKK1qBb3Vlp5owkF/VORHLhg+n+XTji8g4DvDgNMw0w==",
    'pageNo':'1','numOfRows':'10',
    'dataType':'JSON','stnId':'184','fromTmFc':'20221201','toTmFc':'20221205'}

response=requests.get(url,params=params)
result=response.json()
print(result)