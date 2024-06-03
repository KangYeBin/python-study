
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
import codecs
from bs4 import BeautifulSoup

# pip install mysql-connector-python
import mysql.connector

# DB 접속을 위한 정보 셋팅
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='mysql',
    database='jpa'
)

# sql 실행을 위한 커서 생성
mycursor = mydb.cursor()

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체 리턴
driver = webdriver.Chrome(service=service, options=option)

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.aladin.co.kr')

t.sleep(2)

# 베스트셀러 탭 클릭
driver.find_element(By.XPATH, '//*[@id="Wa_header1_headerTop"]/div[2]/div[3]/ul[1]/li[3]/a').click()

t.sleep(2)


rank = 1
index = 2

while index <= 8:
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

        auth_name, company, pub_day = [info.strip() for info in auth_info]

        # sql을 문자열로 작성하고, 변수가 들어갈 위치를 %d, %s 등으로 표현한다
        # 값은 tuple에 순서대로 세팅해서 mycursor.execute()에 전달한다 
        query = 'INSERT INTO tbl_crawling (data_rank, title, author, company, publish_date, price) VALUES(%s, %s, %s, %s, %s, %s)'
        values = (rank, book_title, auth_name, company, pub_day, book_price.split(', ')[0])
        mycursor.execute(query, values)


        '''
        SELECT를 했다면 excute로 sql을 실행하고나서

        for row in mycursor:
            print(str(row[컬럼명]))
        '''

        rank += 1
    
    # 다음 페이지(탭)로 전환
    index += 1
    driver.find_element(By.XPATH, f'//*[@id="newbg_body"]/div[3]/ul/li[{index}]').click()
    del soup
    t.sleep(2)

mydb.commit()
# mydb.rollback() -> 예외 처리와 함께 사용해서, 중간에 에러가 발생했을 시 롤백 처리

driver.close()
mycursor.close()
mydb.close()