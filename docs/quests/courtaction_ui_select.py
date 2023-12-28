from importselenium import selenium_running
from mongoconnect import mongo_connect
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

address = 'https://www.courtauction.go.kr/'
browser = selenium_running(address)
insert_collection = mongo_connect('mongodb://localhost:27017','gatheringdatas','courtaction_ui_select')

def into_screen():
    time.sleep(3)
    browser.switch_to.frame("indexFrame")
    element_click = browser.find_element(by=By.CSS_SELECTOR,value='#menu > h1:nth-child(5) > a')
    element_click.click()
    return

def selec_jiwon_index():
    numcount_bundle = browser.find_elements(by=By.CSS_SELECTOR,value='#idJiwonNm>option') # 지원 엘리멘츠 호출
    count=0
    for i in numcount_bundle:   # 엘리멘츠 갯수 카운팅
        count +=1

    for i in range(count-1):    # 마지막 전체섹터를 제외한 내용 호출
        selector_element = '#idJiwonNm'
        element_country = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
        Select(element_country).select_by_index(i)
        # 검색 버튼 클릭
        element_click = browser.find_element(by=By.CSS_SELECTOR,value='#contents > form > div.tbl_btn > a:nth-child(1)')
        element_click.click()
        time.sleep(3)
        # 페이지 이동 함수 호출
        page_move()
        pass
    return

def selec_jiwon_value():
    # 옵션값 전부 호출
    dropdown_bundle = browser.find_elements(by=By.CSS_SELECTOR,value='#idJiwonNm>option')
    # value로 select작성
    dropdown = browser.find_element(by=By.ID, value='idJiwonNm')
    select = Select(dropdown)
    for i in range(len(dropdown_bundle) - 1):  # 마지막 '전체' 옵션을 제외하고 반복
        dropdown_bundle = browser.find_elements(by=By.CSS_SELECTOR,value='#idJiwonNm>option')
        dropdown = browser.find_element(by=By.ID, value='idJiwonNm')
        select = Select(dropdown)
        time.sleep(3)
        option_value = dropdown_bundle[i].get_attribute('value')
        select.select_by_value(option_value)
        
        # 검색 버튼 클릭
        element_click = browser.find_element(by=By.CSS_SELECTOR, value='#contents > form > div.tbl_btn > a:nth-child(1)')
        element_click.click()
        time.sleep(3)
        # 페이지 이동 함수 호출
        page_move()
        pass
    return

def page_data_get():
    # 법원 이름 호출
    element_title = browser.find_element(by=By.CSS_SELECTOR, value='#search_title > ul > li:nth-child(1)')
    title = element_title.text
    # 내용 전체 호출
    element_casenum = browser.find_elements(by=By.CSS_SELECTOR, value='#contents > div.table_contents > form:nth-child(1) > table > tbody>tr')
    sec_count=0 # 다중 내용 저장 연결을 위한 카운팅 초키화
    for i in element_casenum:
        sec_count+=1   
        try:
            element_case = i.find_element(by=By.CSS_SELECTOR, value='td:nth-child(2)')
            case_num = element_case.text
            pass
        except:
            case_num=''
            pass
        element_contents = browser.find_elements(by=By.CSS_SELECTOR, value='tr:nth-child({})>td:nth-child(4)>div'.format(sec_count)) # 해당 칸의 내용 전부 호출
        for j in element_contents:
            try:
                content = j.text
                pass
            except:
                content =''
                pass
            data={
                'Court' : title,
                'Case_number' : case_num,
                'Content' : content
            }
            insert_collection.insert_one(data)  # 저장
            pass
        pass
    return

def page_move():
    # 리스트 번호의 맨 마지막 버튼의 위치 카운트
    element_lastcount = browser.find_elements(by=By.CSS_SELECTOR,value='#contents > div.table_contents > form:nth-child(2) > div > div.page2>a')
    lastcount=0
    for i in element_lastcount:
        lastcount += 1

    try:
        # 맨 마지막 페이지로 이동
        element_click = browser.find_element(by=By.CSS_SELECTOR,value='#contents > div.table_contents > form:nth-child(2) > div > div.page2 > a:nth-child({})'.format(lastcount))
        element_click.click()
        pass
   

        # 맨 마지막 장의 페이지 숫자 저장 후 첫페이지로 이동
        element_finalnum = browser.find_element(by=By.CSS_SELECTOR, value='#contents > div.table_contents > form:nth-child(2) > div > div.page2 > span')
        count = int(element_finalnum.text)
        element_click = browser.find_element(by=By.CSS_SELECTOR,value='#contents > div.table_contents > form:nth-child(2) > div > div.page2 > a:nth-child(1)')
        element_click.click()    


        for i in range((count//10)+1):  # 10페이지씩 이동할 수 있는 상태 +1 동안 반복 (마지막 반복에 오류로 브레이크)
            try:
                local_count = 0
                for j in range(2,12):

                    page_data_get() # 페이지 정보 저장 함수 호출

                    if local_count==0: # 맨 첫번째 페이지 에서 클릭
                        element_click = browser.find_element(by=By.CSS_SELECTOR,value='#contents > div.table_contents > form:nth-child(2) > div > div.page2 > a:nth-child({})'.format(j))
                        element_click.click()
                        local_count=1   # 첫번재 클릭 이후 두번째 클릭 고려로 이동 조건
                        time.sleep(2)
                        pass

                    elif local_count==1:    # 두번째 부터 버튼 갯수 고려해서 클릭
                        element_click = browser.find_element(by=By.CSS_SELECTOR,value='#contents > div.table_contents > form:nth-child(2) > div > div.page2 > a:nth-child({})'.format(j+1))
                        element_click.click()
                        time.sleep(2)
                        pass

                    elif local_count == 2:  # 리스트의 숫자가 10개가 넘어갔을 경우 클릭
                        element_click = browser.find_element(by=By.CSS_SELECTOR,value='#contents > div.table_contents > form:nth-child(2) > div > div.page2 > a:nth-child({})'.format(j+2))
                        element_click.click()
                        time.sleep(2)
                        pass

                local_count = 2 # 리스트의 숫자가 10개가 넘어갔을 때 조건

                # 다음 리스트 페이지로 이동
                element_click = browser.find_element(by=By.CSS_SELECTOR,value='#contents > div.table_contents > form:nth-child(2) > div > div.page2 > a:nth-child(12)')
                element_click.click()

            except: # 다음 페이지가 없을 시 이전 버튼 클릭
                element_click = browser.find_element(by=By.CSS_SELECTOR,value='#contents > div.table_contents > div.tbl_btn > a:nth-child(5)')
                element_click.click()
                break
    except: # 경매 매물이 없을경우
        element_click = browser.find_element(by=By.CSS_SELECTOR,value='#contents > div.table_contents > div.tbl_btn > a:nth-child(5)')
        element_click.click()
    return

into_screen()
# selec_jiwon_index() # index로 진입
selec_jiwon_value()  # value로 진입
browser.quit()