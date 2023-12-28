# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException

from pymongo import MongoClient

mongoclient = MongoClient('mongodb://localhost:27017') #mongo접속
db_local = mongoclient['gatheringdatas']   #database 연결
insert_collection = db_local['11st_item_comments_back']
insert_sec_collection = db_local['11st_comment']


webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소  입력
browser.get("https://www.11st.co.kr/category/DisplayCategory.tmall?method=getDisplayCategory3Depth&dispCtgrNo=865018")
main_window_handle = browser.current_window_handle # 초기 창 핸들로 저장
# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)

# - 정보 획득
from selenium.webdriver.common.by import By

element_itmes = browser.find_elements(by=By.CSS_SELECTOR, value=' div.list_info > p.info_tit > a') # a 다음 그 클래스 적기
for itme in element_itmes:
    itme.click()
    
    time.sleep(3)   #화면 완성 텀

    all_window_handles = browser.window_handles # 모든 창 저장

    # 새 창 핸들을 찾기
    new_window_handle = None
    for handle in all_window_handles:
        if handle != main_window_handle:    #현재 창이 메인창이 아닐때
            new_window_handle = handle  # 현재 창이 새로운창으로 핸들
            break

    # 새 창 핸들로 전환
    browser.switch_to.window(new_window_handle) # 현재창으로 핸들

    # 새 창의 URL 가져오기
    new_window_url = browser.current_url
    browser.get(new_window_url)

    new_page = browser.find_elements(by=By.CSS_SELECTOR, value=' body') #새창의 엘리맨츠 가져오기
    for in_item in new_page:
        try:    # 타이틀 출력
            element_title = in_item.find_element(by=By.CSS_SELECTOR, value='#layBodyWrap > div > div.s_product.s_product_detail > div.l_product_cont_wrap > div > div.l_product_view_wrap > div.l_product_summary > div.l_product_side_info > div.c_product_info_title > h1')
            title = element_title.text
            pass
        except:
            title=''
            pass
        try:    # 이미지 주소 출력
            element_img = in_item.find_element(by=By.CSS_SELECTOR, value='#productImg > div.img_full > img')
            img = element_img.get_attribute('src')
        except:
            img = ''
            pass
        try:    # 할인 이전 가격 출력
            element_price_regular = in_item.find_element(by=By.CSS_SELECTOR, value=' dd.price_regular > del')
            price_regular = element_price_regular.text
            pass
        except:
            price_regular=''
            pass
        try:    # 할인 후 가격 출력
            element_finalDscPrcArea = in_item.find_element(by=By.CSS_SELECTOR, value=' #finalDscPrcArea > dd.price>strong')
            finalDscPrc = element_finalDscPrcArea.text
            pass
        except:
            finalDscPrc=''
            pass
        try:    # 상품 정보 iframe 진입
            browser.switch_to.frame("prdDescIfrm")
            iframe_pages = browser.find_elements(by=By.CSS_SELECTOR, value=' body') # 해당 imrame의 앨리맨츠 추출
            detail=[]   # 정보담을 리스트 초기화
            for iframe_page in iframe_pages:
                try:
                    element_detail = iframe_page.find_element(by=By.CSS_SELECTOR, value='body > div.ifrm_prdc_detail > font > p:nth-child(2)')
                    detail.append(element_detail.text)  # 여러개의 정보 리스트에 저장
                except:
                    element_detail = iframe_page.find_element(by=By.CSS_SELECTOR, value='body > div > section > div.bk11st_detail')
                    detail.append(element_detail.text)  # 1차 주소에 값이 없을 시, 2차 주소 값 리스트 저장
            pass
        except:
            detail = ''
            pass
        data={
            'Title' : title,
            'Img_lnk' : img,
            'Old_price' : price_regular,
            'Dsc_price' : finalDscPrc,
            'Detail' : detail
        }
        insert_collection.insert_one(data)  # 데이터 베이스 업로드

    try:
        browser.switch_to.frame('ifrmReview')
    except:
        pass
       # comment 창 진입
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
                        insert_sec_collection.insert_one(data)
                    pass
                pass
        except:
            break



    browser.close() # 새로 열린창 닫기
    browser.switch_to.window(main_window_handle)    # 다시 처음 창으로 전환

    # 처음창이 충분히 열릴 때까지 기다림
    wait = WebDriverWait(browser, 10)   # 10초마다 체크
    wait.until(EC.presence_of_element_located((By.XPATH, '//body')))    # 새창에서 body가 로딩될때까지

pass
# browser.save_screenshot('./formats.png')
# 브라우저 종료
browser.quit()