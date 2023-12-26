# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from pymongo import MongoClient

mongoclient = MongoClient('mongodb://localhost:27017') #mongo접속
db_local = mongoclient['gatheringdatas']   #database 연결
insert_collection = db_local['watch_comment']



webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소  입력
browser.get("https://pedia.watcha.com/ko-KR/contents/mOA2QVd/comments")
# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

element_body = browser.find_element(by=By.CSS_SELECTOR,value='body')

previous_scrollHeight = 0

while True: # 스크롤 끝까지 내리기
    element_body.send_keys(Keys.END)
    current_scrollHeight = browser.execute_script('return document.body.scrollHeight')
    if previous_scrollHeight >= current_scrollHeight:
        break
    else:
        previous_scrollHeight = current_scrollHeight
        pass
    time.sleep(3)


element_count = browser.find_elements(by=By.CSS_SELECTOR,value='section > div > div > div > ul>div') # 총 수집할 엘리멘츠 호출
count=0 # 카운트 초기화
for i in element_count: # 수입할 엘리멘츠 수만큼
    count +=1   # 카운트 증가
    pass

for i in range(count): # 총 엘리멘츠 수만큼 반복
    try:
        element_bundle = browser.find_elements(by=By.CSS_SELECTOR,value='section > div > div > div > ul> div:nth-child({})'.format(i))  # 번들 번호에 맞춰서 추출
        for j in element_bundle:
            try:    # 이름 추출
                element_name = j.find_element(by=By.CSS_SELECTOR,value='div.css-jqudug.egj9y8a3 > div.css-drz8qh.egj9y8a2 > a > div.css-eldyae.e10cf2lr1')
                name = element_name.text
            except:
                name = ""
            try:    # 별점 추출
                element_star = j.find_element(by=By.CSS_SELECTOR,value='div.css-jqudug.egj9y8a3 > div.css-31ods0.egj9y8a0 > span')
                star=element_star.text
            except:
                star=""
            try:    # 코멘트 추출
                element_comment = j.find_element(by=By.CSS_SELECTOR,value='div.css-2occzs.egj9y8a1 > a > div > span')
                comment=element_comment.text
            except:
                comment=""
            data = {
                    'Name': name,
                    'Star': star,
                    'Comment': comment
                    }
            insert_collection.insert_one(data)  # DB 저장
    except:
        break    

# 브라우저 종료
browser.quit()
