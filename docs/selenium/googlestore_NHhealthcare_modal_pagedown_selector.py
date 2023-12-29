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
browser.get("https://play.google.com/store/apps/details?id=com.nhlife.customer.healthcare&hl=ko-KR&pli=1")

# - 가능 여부에 대한 OK 받음
pass

# - 정보 획득
from selenium.webdriver.common.by import By


# 모달 화면 띄우기
selector_element = '#ow68 > section > header > div > div:nth-child(2)'
browser.find_element(by=By.CSS_SELECTOR, value=selector_element).click()

# 정보 획득
selector_element = 'div.fysCi'
element_scrollableDiv = browser.find_element(by=By.CSS_SELECTOR, value=selector_element).click()

# 댓글 개수 확인 : div.RHo1pe
selector_element = 'div.RHo1pe'
element_comment = browser.find_element(by=By.CSS_SELECTOR, value=selector_element).click()
print('count comment after done scroll : {}'.format(len(element_scrollableDiv)))

# 스크롤 부분
previous_scrollHeight = 0
while True:
    # python 방식 변수 매칭
    print('{0}.scrollTo({1}, {0}.scrollHeight)'.format(element_scrollableDiv,previous_scrollHeight))
    # javascript와 python 결합 방식 변수 매칭
    browser.execute_script("arguments[0].scrollto(arguments[1], arguments[0].scrollHeight):"
                           ,element_scrollableDiv,previous_scrollHeight)
    current_scrollHeight = browser.execute_script("return arguments[0].scrollHeight",
                                                  element_scrollableDiv)
    
    
    if previous_scrollHeight >= current_scrollHeight:
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(1)
    pass

pass
# browser.save_screenshot('./formats.png')
# 브라우저 종료
browser.quit()