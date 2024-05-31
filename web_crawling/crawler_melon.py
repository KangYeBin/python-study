
'''
# 순위
# 가수명
# 앨범명
# 노래 제목

# 멜론일간차트순위_2024년_5월_31일_11시기준.txt
'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs
from bs4 import BeautifulSoup

d = datetime.today()
file_path = f'C:/myWorkspace/upload/멜론일간차트순위_{d.year}년_{d.month}월_{d.day}일_{d.hour}시기준.txt'

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

service = webdriver.ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=option)

driver.get('https://www.melon.com/chart/index.htm')

t.sleep(2)

with codecs.open(file_path, mode='w', encoding='utf-8') as f :

    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')
    tr_list = soup.select('tr.lst50, tr.lst100')
    rank = 1

    for tr in tr_list :
        song_info = tr.select('a')

        f.write(f'# 순위 : {rank}위\n')
        f.write(f'# 가수명 : {song_info[3].text}\n')
        f.write(f'# 앨범명 : {song_info[5].text}\n')
        f.write(f'# 노래 제목 : {song_info[2].text}\n')
        f.write('-' * 40 + '\n')

        rank += 1