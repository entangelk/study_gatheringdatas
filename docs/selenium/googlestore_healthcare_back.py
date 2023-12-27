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
browser.get("https://play.google.com/store/search?q=%ED%97%AC%EC%8A%A4%EC%BC%80%EC%96%B4%EC%95%B1&c=apps&hl=ko-KR&pli=1")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)

# - 정보 획득
from selenium.webdriver.common.by import By
# #yDmH0d > c-wiz.SSPGKf.glB9Ve > div > div > c-wiz > c-wiz > c-wiz > section > div > div > div > div:nth-child(1) > div > div > div > a
element_companies = browser.find_elements(by=By.CSS_SELECTOR, value='div>a.Si6A0c Gy4nib') # a 다음 그 클래스 적기
for company in element_companies:
    company.click()
    time.sleep(1)   #화면 완성 텀
    element_title = browser.find_element(by=By.CSS_SELECTOR, value='div > h1')
    print("App company Name : {}".format(element_title.text))
    browser.back() # 제품 리스트로 이동
    time.sleep(1)   # 화면 완성 텀

pass
# browser.save_screenshot('./formats.png')
# 브라우저 종료
browser.quit()