import requests

# 기상청_관광코스별 관광지 상세 날씨 조회서비스
# form :  https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15056912

url='http://apis.data.go.kr/1360000/TourStnInfoService1/getCityTourClmIdx1'

params ={
    'serviceKey':'U7qOOR4KMrkRvFHfQjd8XQh1DJraaYLetyiqIfNiJEsrwG+HRWhPpfVffZDjB0aJtFc9eSmc6tR1iWQat2Stew==',
'pageNo': 1,
'numOfRows': 10,
'dataType': 'JSON',
'CURRENT_DATE' : 2018123110,
'DAY' : 3,
'CITY_AREA_ID' : 5013000000
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
collection = database['TourStnInfoService1']
# insert 작업 진행
result = collection.insert_many(contents['response']['body']['items']['item'])


pass