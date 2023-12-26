# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://pages.coupang.com/p/104978")

# - 가능 여부에 대한 OK 받음
pass

# - 정보 획득
from selenium.webdriver.common.by import By
selector_value = 'div.product-unit.product-unit--medium.product-unit--pc'
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
for i in element_bundle:
    # print(i.text) # 상품 정보들
    #상품 제목
    element_title = i.find_element(by=By.CSS_SELECTOR, value='span.product-unit-info__title')
    title = element_title.text
    # 상품 원가
    try : 
        element_old_price = i.find_element(by=By.CSS_SELECTOR, value='del.discount-price__base-price')
        old_price = element_old_price.text
        pass
    except:
        old_price = ''
        pass
    print('title : {}, old price : {}'.format(title,old_price))
pass

# 브라우저 종료
browser.quit()