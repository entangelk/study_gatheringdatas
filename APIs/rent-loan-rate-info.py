import requests

# 한국주택금융공사_전세자금대출 금리 정보
# form :  https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15082033

url='http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

params ={
    'serviceKey':'U7qOOR4KMrkRvFHfQjd8XQh1DJraaYLetyiqIfNiJEsrwG+HRWhPpfVffZDjB0aJtFc9eSmc6tR1iWQat2Stew==',
'pageNo': 1,
'numOfRows': 10,
'dataType': 'JSON'
}


response = requests.get(url,params=params)


import json
contents = json.loads(response.content)

type(contents)
# <class 'dict'>
contents['header']
# {"resultCode": "00", "resultMsg": "정상"}
contents['header']['resultCode']
# '00'
contents['body']['totalCount']
# 18
type(contents['body']['items'])
# <class 'list'>


# mongodb 저장

from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["data_go_kr"]
# collection 작업
collection = database['rent-loan-rate-info']
# insert 작업 진행
result = collection.insert_many(contents['body']['items'])

pass