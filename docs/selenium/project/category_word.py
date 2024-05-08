# SSG 카테고리별

# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))


# 몽고db 저장
from pymongo import MongoClient
# mongodb에 접속
# mongoClient = MongoClient("mongodb://192.168.10.10:27017")
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["data_get"]
# collection 작업
news_get = database['ssg']

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
from selenium.webdriver.common.by import By

url = 'https://www.ssg.com/item/itemView.ssg?itemId=0000006615248&siteNo=6001&salestrNo=2037'


browser.get(url)
time.sleep(2)

element_body = browser.find_element(by=By.CSS_SELECTOR,value='body')





while True:

    # 타이틀
    try:
        selector_title = '#content > div.cdtl_cm_detail.v3.ty_ssg.ty_grocery.react-area > div.cdtl_row_top > div.cdtl_col_rgt > div.cdtl_prd_info.v2 > h2 > span > span'
        element_title = browser.find_element(by=By.CSS_SELECTOR,value=selector_title)
        title = element_title.text
    except:
        title = ""

        time.sleep(1)

    # 세일 유무
    merchEvent = False
    price_old = None
    try:
        selector_event = "#content > div.cdtl_cm_detail.v3.ty_ssg.ty_grocery.react-area > div.cdtl_row_top > div.cdtl_col_rgt > div.cdtl_info_wrap > div.cdtl_optprice_wrap > div > span.cdtl_new_price.notranslate > em"
        element_event = browser.find_element(by=By.CSS_SELECTOR,value=selector_event)
        merchEvent = True

        # 세일 중 현재가격
        price = element_price.text
        price = price.replace(',','') # ',' 삭제
        price = int(price) # int로 저장

        # 세일 중 이전가격
        selector_old_price = "#content > div.cdtl_cm_detail.v3.ty_ssg.ty_grocery.react-area > div.cdtl_row_top > div.cdtl_col_rgt > div.cdtl_info_wrap > div.cdtl_optprice_wrap > div > span.cdtl_old_price > em"
        element_old_price = browser.find_element(by=By.CSS_SELECTOR,value=selector_old_price)
        price_old = element_old_price.text[:-1] # '원' 삭제
        price_old = price_old.replace(',','') # ',' 삭제
        price_old = int(price_old) # int로 저장
    except:
        try:
            selector_price = "#content > div.cdtl_cm_detail.v3.ty_ssg.ty_grocery.react-area > div.cdtl_row_top > div.cdtl_col_rgt > div.cdtl_info_wrap > div.cdtl_optprice_wrap > div > span > em"
            element_price = browser.find_element(by=By.CSS_SELECTOR,value=selector_price)
            price = element_price.text
            price = price.replace(',','') # ',' 삭제
            price = int(price) # int로 저장
        except:
            price = ""



        

            # 내용
            content = ''
            try:
                selector_content_2= "#mArticle > div.news_view.fs_type1 > strong"
                element_content = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_content_2)
                content += element_content.text
                content += ' '
            except:
                pass
            try:
                selector_content_1= "#mArticle > div.news_view.fs_type1 > div.article_view"
                element_content = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_content_1)
                content += element_content.text
            except:
                pass

            # 언론사
            
            try:
                selector_media = "#mArticle > div.news_view.fs_type1 > p"
                element_media = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_media)
                text_list = list(element_media.text.split())
                media = text_list[1][:-1]
            except:
                media = ""

            # mongodb 저장
            data = {
                'news_title' : title,
                'news_date' : times,
                'news_brand' : media,
                'news_contents' : content
            }
            pass
            news_get.insert_one(data)

        time.sleep(2)


    # 다음 페이지 클릭
    try:
        element_click = browser.find_element(by=By.CSS_SELECTOR,value=f'#dnsColl > div:nth-child(2) > div > button.btn_next')
        element_click.click()
        time.sleep(2)
    except:
        break

        
        
    time.sleep(2)

# 브라우저 종료
browser.quit()