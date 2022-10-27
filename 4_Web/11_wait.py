from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()
browser.get('https://flight.naver.com/')

# 장소 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]').click()
time.sleep(1)

# 날짜 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[5]/button').click()
time.sleep(1)

# 항공권 검색
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# 다음 페이지 출력될 때까지 대기 후 처리 
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]/div')))
    print(elem.text)
except:
    print("실패했어요")

# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]/div')
# print(elem.text)
time.sleep(4)

