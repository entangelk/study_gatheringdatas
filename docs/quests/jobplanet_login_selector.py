# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소  입력
browser.get("https://www.jobplanet.co.kr/job")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
element_login_button = browser.find_element(by=By.CSS_SELECTOR, value='header > div.right_box > div.login_before.show > a.btn_txt.login')
element_login_button.click()

element_login_field = browser.find_element(by=By.CSS_SELECTOR, value='#user_email')
element_login_field.send_keys("dyrkd12@naver.com")

element_password_field = browser.find_element(by=By.CSS_SELECTOR, value='#user_password')
element_password_field.send_keys("**")

element_login_button = browser.find_element(by=By.CSS_SELECTOR, value='div > section.section_email.er_r > fieldset > button')
element_login_button.click()
'''
element_search_field = browser.find_element(by=By.CSS_SELECTOR, value='#search_form > div > label')
element_search_field.send_keys("데이터분석")
pass

element_search_button = browser.find_element(by=By.CSS_SELECTOR, value='#search_form > div > button > i')
element_search_button.click()
pass
'''
# browser.save_screenshot('./formats.png')
# 브라우저 종료
browser.quit()