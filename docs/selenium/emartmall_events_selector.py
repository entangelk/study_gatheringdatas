# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=10

# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소  입력
for page_num in range(6):
    url = 'https://www.coupang.com/np/categories/194831?page='
    browser.get("{}{}".format(url,page_num+1))
    time.sleep(3)
    html = browser.page_source

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)

# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
pass
# browser.save_screenshot('./formats.png')
# 브라우저 종료
browser.quit()