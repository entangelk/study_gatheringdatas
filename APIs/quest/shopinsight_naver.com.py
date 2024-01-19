# from : https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4

import requests  # postman app 역할

# request API 요청
url = "https://openapi.naver.com/v1/datalab/shopping/categories"

params =  {
    "startDate":"2017-08-01",
    "endDate":"2018-09-30",
    "timeUnit":"month",
    "category":[
        {"name":"패션의류","param":["50000000"]},
        {"name":"화장품/미용","param":["50000002"]}
        ],
    }
headers ={
    'Host' : 'openapi.naver.com',
    'X-Naver-Client-Id' : 'UO2S9XsZaoMlGjRKN8Ut',
    'X-Naver-Client-Secret' : 'a9tB6EspHA',
    'Content-Type' : 'application/json',
    'Content-Length' : '360'
}

response = requests.post(url, json=params, headers=headers)

raw_content = response.content

# json 변환
import json
contents = json.loads(raw_content)

pass
shopinsight_info = [
    {
        'startDate' : contents['startDate'],
        'endDate' : contents['endDate'],
        'timeUnit' : contents['timeUnit'],
    }
]

# mongodb 저장

from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["naver"]
# collection 작업
collection_info = database['shopinsight_info']
collection_item = database['shopinsight_results']

# insert 작업 진행
result_info = collection_info.insert_many(shopinsight_info)

elements_info = collection_info.find_one({},{'_id' : 1})
id_relative = elements_info['_id']

result_list = contents['results']

for i in range(len(result_list)):
    result_list[i]['id_relative'] = id_relative
    pass

result_item = collection_item.insert_many(result_list)

pass