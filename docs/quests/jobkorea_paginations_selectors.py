# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=10

# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
browser.get('https://www.coupang.com/np/campaigns/348?page=1') # 초기 화면 겟
element_paginations_button = browser.find_elements(by=By.CSS_SELECTOR, value='#product-list-paging > div>a') # 번호 갯수 겟
count=-2 # 좌우 버튼을 처리하기 위해 count에 -2
for i in element_paginations_button: # 번호 갯수만큼 카운팅
    count+=1
pass
# - 주소  입력
for i in range(1,count): #획득한 번호만큼 브라우져 겟
    browser.get('https://www.coupang.com/np/campaigns/348?page={}'.format(i))
    html = browser.page_source
    time.sleep(3)

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)

# - 정보 획득

# 브라우저 종료
browser.quit()