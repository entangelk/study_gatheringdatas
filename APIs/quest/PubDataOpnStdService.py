import requests

# 조달청_나라장터 공공데이터개방표준서비스
# form :  https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15058815

url='http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo'

params ={
    'serviceKey':'U7qOOR4KMrkRvFHfQjd8XQh1DJraaYLetyiqIfNiJEsrwG+HRWhPpfVffZDjB0aJtFc9eSmc6tR1iWQat2Stew==',
'pageNo': 1,
'numOfRows': 10,
'type': 'json',
'bidNtceBgnDt' : '201712010000',
'bidNtceEndDt' : '201712312359'
}


response = requests.get(url,params=params)

import json
contents = json.loads(response.content)

# mongodb 저장

from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["data_go_kr"]
# collection 작업
collection = database['PubDataOpnStdService']
# insert 작업 진행
result = collection.insert_many(contents['response']['body']['items'])

pass