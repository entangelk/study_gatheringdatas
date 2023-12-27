# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from pymongo import MongoClient

mongoclient = MongoClient('mongodb://localhost:27017') #mongo접속
db_local = mongoclient['gatheringdatas']   #database 연결
insert_collection = db_local['11st_switch_iframe']


webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소  입력
browser.get("https://www.11st.co.kr/products/3940623089")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By

browser.switch_to.frame('ifrmReview')   # comment 창 진입
time.sleep(3)
while True: # 더보기 끝까지 호출하기
    try : 
        element_click = browser.find_element(by=By.CSS_SELECTOR,value='#review-list-page-area > div > button')
        element_click.click()
        time.sleep(3)
        pass
    except:
        break
    
page_area = browser.find_elements(by=By.CSS_SELECTOR,value='#review-list-page-area>ul')    # 카운팅 할 모든 엘리맨트 호출
count=0 # 카운터 초기화
for i in page_area: # 엘리멘트 갯수만큼
    count += 1  # 카운트 증가
    pass
pass



pass
for i in range(count):  # 총 엘리멘트 수 만큼 반복
    try:
        element_bundles = browser.find_elements(by=By.CSS_SELECTOR,value='#review-list-page-area > ul:nth-child({})'.format(i+1))   # 1차 코멘트 페이지
        for k in element_bundles:
            element_bundle = k.find_elements(by=By.CSS_SELECTOR,value='li') # 2차 개인 섹션
            for j in element_bundle:
                sec_count=0 # useless data 거름망을 위한 카운터 초기화
                try:
                    element_name = j.find_element(by=By.CSS_SELECTOR, value='dl > dt')  # 이름 추출
                    name = element_name.text
                except:
                    name = ""
                    sec_count+=1    # useless data 카운팅
                try:
                    try:
                        element_select = j.find_element(by=By.CSS_SELECTOR, value='div > p.option > dd')    # 옵션 추출 1차 트라이
                        select = element_select.text
                        pass
                    except:
                        try:
                            element_select = j.find_element(by=By.CSS_SELECTOR, value='div > p.option') # 옵션 추출 2차 트라이
                            select = element_select.text
                        except:
                            element_select = j.find_element(by=By.CSS_SELECTOR, value='div > dl > div > dd') # 옵션 추출 3차 트라이
                            select = element_select.text
                except:
                    select = ""
                    sec_count+=1 # useless data 카운팅
                try:
                    element_star = j.find_element(by=By.CSS_SELECTOR, value='div > p.grade > span > em')    # 평점 추출
                    star = element_star.text
                except:
                    star = ""
                    sec_count+=1 # useless data 카운팅
                try:
                    element_comment = j.find_element(by=By.CSS_SELECTOR, value='div > div > div.cont_text_wrap > p') # 코멘트 추출
                    comment = element_comment.text
                except:
                    comment = ""
                    sec_count+=1 # useless data 카운팅
                data ={
                    'Name' : name,
                    'Select' : select,
                    'Star' : star,
                    'Comment' : comment
                }
                if sec_count > 2: # useless data 라면 DB 인서트 하지 않기
                    pass
                else:
                    insert_collection.insert_one(data)
                pass
            pass
    except:
        break


# 브라우저 종료
browser.quit()