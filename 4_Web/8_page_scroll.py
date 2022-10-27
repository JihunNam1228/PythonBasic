from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# # //*[@id="html"]

options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()
browser.get('https://shopping.naver.com/home')

elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div/input')
elem.send_keys("무선마우스")
elem.send_keys(Keys.ENTER)

# # 스크롤
# # 지정한 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 1080)')  # 1920*1080
# time.sleep(1)
# browser.execute_script('window.scrollTo(0, 2080)')

# # 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')



# *****************************   동적 페이지에 대해서 마지막까지 스크롤 반복 수행 ******************************
interval = 2    # 2초에 한번씩 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    time.sleep(interval)

    curr_height = browser.execute_script('return document.body.scrollHeight')

    if curr_height == prev_height:
        break
    
    prev_height = curr_height

time.sleep(1)
# 맨 위로 올리기
browser.execute_script('window.scrollTo(0,0)')

time.sleep(3)