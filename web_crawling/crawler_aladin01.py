
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t

# 뷰티풀 수프 임포트
from bs4 import BeautifulSoup

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

service = webdriver.ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=option)

driver.get('https://www.aladin.co.kr')

t.sleep(2)

# 베스트셀러 탭 클릭
driver.find_element(By.XPATH, '//*[@id="Wa_header1_headerTop"]/div[2]/div[3]/ul[1]/li[3]/a').click()

t.sleep(2)

# selenium으로 현재 페이지의 html 소스 코드를 전부 불러오기
src = driver.page_source
# print(src)

# 뷰티풀 수프 객체 생성
# 객체를 생성하면서 셀레늄이 가지고 온 html 소스 코드를 전달하고
# 해당 소스 코드를 html 문법으로 변환
soup = BeautifulSoup(src, 'html.parser')

'''
- 뷰티풀 수프를 사용하여 수집하고 싶은 데이터가 들어있는 태그를 부분 추출

- find_all() 메서드는 인수값으로 추출하고자 하는 태그의 이름을 적으면
    해당 태그만 전부 추출하여 리스트에 담아 대입한다
'''
div_list = soup.find_all('div', class_='ss_book_box')
print('div_list에 들어있는 데이터 수 :', len(div_list)) # 50개
print(div_list[0])  # 1위 책만 출력

#li 안에 우리가 필요로하는 텍스트가 존재하면
# 그중에서도 2, 3, 4번째 li의 텍스트를 가져와야 한다
# 1위 책 내용에서 모든 li 추출
first_book = div_list[0].find_all('li')

# text는 태그를 제외한 사용자가 실제로 브라우저에서 확인 가능한
# 텍스트만을 추출하여 문자열 형태로 반환한다


book_title = first_book[1].text # 두 번째 li를 지목하기 위해 1번 인덱스로 지목
book_author = first_book[2].text
boook_price = first_book[3].text

auth_info = book_author.split('|')

print(f'제목 : {book_title}')
print(f'저자 : {auth_info[0]}')
print(f'출판서 : {auth_info[1]}')
print(f'출판년월: {auth_info[2]}')
print(f'가격 : {boook_price.split(", ")[0]}')