# 상품 제목, 판매원가, 변경가격 그리고 나머지에 있는 배송방법# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://corners.auction.co.kr/corner/categorybest.aspx")

# - 가능 여부에 대한 OK 받음
pass

# - 정보 획득
from selenium.webdriver.common.by import By
selector_value = 'div.info'
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
for i in element_bundle[0:10]:
    # print(i.text) # 상품 정보들
    #상품 제목
    element_title = i.find_element(by=By.CSS_SELECTOR, value='em')
    title = element_title.text
    # 상품 원가
    try : 
        element_old_price = i.find_element(by=By.CSS_SELECTOR, value='span.cost')
        old_price = element_old_price.text
        pass
    except:
        old_price = ''
        pass
    try :
        element_new_price = i.find_element(by=By.CSS_SELECTOR, value='span.sale')
        new_price = element_new_price.text
        pass
    except:
        new_price=""
        pass
    try :
        element_delivery = i.find_elements(by=By.CSS_SELECTOR, value='div.item_icons')
        try : 
            for j in element_delivery:
                delivery_one = j.find_element(by=By.CSS_SELECTOR, value='div.icons.ic_allkill')
                text_delivery_one = delivery_one.text
                pass
        except :
                text_delivery_one = ""
                pass
        try : 
            for j in element_delivery:
                delivery_two = j.find_element(by=By.CSS_SELECTOR, value='div.icons.ic_smiledelivery')
                text_delivery_two = delivery_two.text
                pass
        except :
                text_delivery_two = ""
                pass
        try : 
            for j in element_delivery:
                delivery_three = j.find_element(by=By.CSS_SELECTOR, value='div.icons.ic_free')
                text_delivery_three = delivery_three.text
                pass
        except :
                text_delivery_three = ""
                pass                
        pass
    except:
        text_delivery_one = ""
        text_delivery_two = ""
        text_delivery_three = ""
        pass    
    print('title : {}, old price : {}, new price : {}, delivery method : {} {} {}'.format(title,old_price,new_price,text_delivery_one,text_delivery_two,text_delivery_three))
pass

# 브라우저 종료
browser.quit()