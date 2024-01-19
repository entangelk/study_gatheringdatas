import requests

url='http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

params ={
    'serviceKey':'U7qOOR4KMrkRvFHfQjd8XQh1DJraaYLetyiqIfNiJEsrwG%2BHRWhPpfVffZDjB0aJtFc9eSmc6tR1iWQat2Stew%3D%3D',
'pageNo': 1,
'numOfRows': 10,
'dataType': 'JSON'
}


response = requests.get(url,params=params)

print(response.content)
