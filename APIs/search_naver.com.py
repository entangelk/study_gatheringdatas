# from : https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4

import requests  # postman app 역할

# request API 요청
url = 'https://openapi.naver.com/v1/search/news'

params = {
    'query':'인공지능'
}

headers ={
    'X-Naver-Client-Id' : 'NtLeqJGtcTpNKXOlmtzV',
    'X-Naver-Client-Secret' : '3ndCmeLwzE'
}

response = requests.get(url, params=params, headers=headers)

raw_content = response.content

# json 변환
import json
contents = json.loads(raw_content)

pass