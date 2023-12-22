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
browser.get("https://event.ssg.com/eventDetail.ssg?nevntId=1000000010637&domainSiteNo=7018#7000804248")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
pass
from selenium.webdriver.common.by import By

## 하나의 Element 가져오기 - 거의 쓰지않음 왜? 여러개를 불러올꺼니까
selector_value = "#_section7000804248 > div.mnemitem_grid.v2 > ul > li:nth-child(1) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit"
element_path = browser.find_element(by=By.CSS_SELECTOR,value=selector_value)
# browser.find_element(By.CSS_SELECTOR,value="#_section7000804248 > div.mnemitem_grid.v2 > ul > li:nth-child(1) > div > a > div.mnemitem_tit > span")
# get text in tag
element_path.text
pass

## 여러개 elements 정보 가져오기
selector_value = "span.mnemitem_goods_tit"
elements_path = browser.find_elements(by=By.CSS_SELECTOR,value=selector_value)
type(elements_path)
# <class 'list'>
elements_path[0].text
# '뜨끈한 국/탕/찌개/전골/국수 밀키트 모음딜 (NEO)'

for webelement in elements_path:
    title = webelement.text
    print("{}".format(title))
    pass

pass

# 브라우저 종료
browser.quit()