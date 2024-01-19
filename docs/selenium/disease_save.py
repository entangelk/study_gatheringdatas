# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from mongoconnect import mongo_connect

from bs4 import BeautifulSoup

insert_collection = mongo_connect('mongodb://localhost:27017','teamplays','diseases')

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소  입력
browser.get("https://helpline.kdca.go.kr/cdchelp/ph/rdiz/selectRdizInfList.do?menu=A0100&pageIndex=1&fixRdizInfTab=&rdizCd=&schKor=&schEng=&schCcd=&schGuBun=dizNm&schText=&schSort=kcdCd&schOrder=desc")


# - 정보 획득
from selenium.webdriver.common.by import By


click_url=''
while True:
    for j in range(5,15):
        element_list = browser.find_elements(by=By.CSS_SELECTOR, value='#frm > div > table > tbody > tr')
        count=0
        now_url = browser.current_url
        for i in element_list:
            count+=1
            element_html = i.get_attribute('outerHTML')
            soup = BeautifulSoup(element_html, 'html.parser')
            try :
                dt = soup.select_one('dt')
                if dt:
                    p = dt.find('p')
                    if p:
                        p.extract()
                    title_ko = dt.get_text(strip=True)
                    pass
                else:
                    title_ko = ''
                    pass
            except :
                title_ko = ''
                pass             
            try :
                element_title_en = i.find_element(by=By.CSS_SELECTOR,value='tr > td > dl > dt > p')
                title_en = element_title_en.text
            except :
                title_en = ''
                pass
            try:
                li_kcd = soup.select_one('dd > ul > li:nth-child(4)')
                kcd = li_kcd.get_text(strip=True).split(':')[-1].strip() if li_kcd else ''
            except:
                kcd = ''
                pass
            try:
                li_spc_code = soup.select_one('dd > ul > li:nth-child(5)')
                spc_code = li_spc_code.get_text(strip=True).split(':')[-1].strip() if li_spc_code else ''
            except:
                spc_code = ''
                pass
            try:
                li_group = soup.select_one('dd > ul > li:nth-child(1)')
                group = li_group.get_text(strip=True).split(':')[-1].strip() if li_group else ''
            except:
                group = ''
                pass
            try:
                li_support = soup.select_one('dd > ul > li:nth-child(3)')
                support = li_support.get_text(strip=True).split(':')[-1].strip() if li_support else ''
            except:
                support = ''
                pass                                       
            try :
                element_click = browser.find_element(by=By.CSS_SELECTOR,value=f'tr:nth-child({count}) > td:nth-child(3)')
                element_click.click()
                time.sleep(2)
                url = browser.current_url
                if url == now_url:
                    url = ''
            except :
                url = ''
                pass
            data={
    'dise_name_kr': title_ko,
    'dise_name_en': title_en,
    'dise_KCD_code' : kcd,
    'dise_spc_code' : spc_code,
    'dise_group' : group,
    'dise_support': support,
    'dise_url' : url
            }
            insert_collection.insert_one(data)
            if url == '':
                pass
            else:
                browser.back()
        try:
            element_click = browser.find_element(by=By.CSS_SELECTOR,value=f'#frm > div > ul.paging > li:nth-child({j}) > a')
            element_click.click()
            time.sleep(1)
        except:
            element_click = browser.find_element(by=By.CSS_SELECTOR,value=f'#frm > div > ul.paging > li.pc_n > a')
            element_click.click()
            time.sleep(1)
            click_url = browser.current_url
            if click_url == now_url:
                break
        if click_url == now_url:
                break
    if click_url == now_url:
        break
pass
# browser.save_screenshot('./formats.png')
# 브라우저 종료
browser.quit()
