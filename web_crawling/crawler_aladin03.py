
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs
from bs4 import BeautifulSoup

d = datetime.today()
file_path = f'C:/myWorkspace/upload/알라딘 베스트셀러 1~400위_{d.year}_{d.month}_{d.day}.txt'

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

service = webdriver.ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=option)

driver.get('https://www.aladin.co.kr')

t.sleep(2)

driver.find_element(By.XPATH, '//*[@id="Wa_header1_headerTop"]/div[2]/div[3]/ul[1]/li[3]/a').click()

t.sleep(2)

with codecs.open(file_path, mode='w', encoding='utf-8') as f :
    # selenium으로 현재 페이지의 html 소스 코드를 전부 불러오기

    rank = 1
    index = 2

    while index <= 9:
        src = driver.page_source
        # print(src)
        
        soup = BeautifulSoup(src, 'html.parser')
        div_list = soup.find_all('div', class_='ss_book_box')
        # div_list = soup.select('div.ss_book_box')

        for div in div_list:
            book_info = div.find_all('li')

            if book_info[0].find('span', class_='ss_ht1') == None:
                # 첫 번째 li에 span class="ss_ht1"이 없다면 (사은품 없는 책)
                book_title = book_info[0].text
                book_author = book_info[1].text
                book_price = book_info[2].text

            else :      
                # span class="ss_ht1"이 존재함 (사은품 있는 책)
                book_title = book_info[1].text
                book_author = book_info[2].text
                book_price = book_info[3].text

            auth_info = book_author.split(' | ')

            f.write(f'# 순위 : {rank}위\n')
            f.write(f'# 제목 : {book_title}\n')
            f.write(f'# 저자 : {auth_info[0]}\n')
            f.write(f'# 출판사 : {auth_info[1]}\n')
            f.write(f'# 출판년월: {auth_info[2]}\n')
            f.write(f'# 가격 : {book_price.split(", ")[0]}\n')
            f.write('-' * 40 + '\n')

            rank += 1
        
        # 다음 페이지(탭)로 전환
        index += 1
        driver.find_element(By.XPATH, f'//*[@id="newbg_body"]/div[3]/ul/li[{index}]/a').click()
        del soup
        t.sleep(2)

'''
find(태그이름, class = ? or id = ?) : 조건에 맞는 첫 번째 요소를 반환합니다.
find_all(태그이름, class = ? or id = ?) : 조건에 맞는 모든 요소를 리스트 형태로 반환합니다.
select(선택자) : CSS 선택자를 사용해 요소를 선택합니다.
select_one(선택자) : CSS 선택자를 사용해 첫 번째 요소를 선택합니다.
find_parent() : 해당 요소의 부모 요소를 반환합니다.
find_parents() : 조건에 맞는 모든 부모 요소를 리스트 형태로 반환합니다.
find_next_sibling() : 다음 형제 요소를 반환합니다.
find_next_siblings() : 조건에 맞는 모든 다음 형제 요소를 리스트 형태로 반환합니다.
find_previous_sibling() : 이전 형제 요소를 반환합니다.
find_previous_siblings() : 조건에 맞는 모든 이전 형제 요소를 리스트 형태로 반환합니다.
find_next() : 다음 요소를 반환합니다.
find_all_next() : 조건에 맞는 모든 다음 요소를 리스트 형태로 반환합니다.
find_previous() : 이전 요소를 반환합니다.
find_all_previous() : 조건에 맞는 모든 이전 요소를 리스트 형태로 반환합니다.
'''