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
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')

curr_handle = browser.current_window_handle
# print(curr_handle)  # 전체 윈도우 핸들 정보

# Try it yourself
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles    # 모든 핸들 정보
time.sleep(1)
for handle in handles:
    print(handle)
    browser.switch_to.window(handle)    # 각 핸들로 이동해서
    print(browser.title)    # 출력해보면 현재 핸들(브라우저)의 제목 표시
    print()
time.sleep(1)

# 새로 이동된 브라우저에서 뭔가 자동화 작업을 수행

# 그 브라우저를 종료
print("현재 핸들 닫기")
browser.close()
time.sleep(1)
# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
browser.switch_to.window(curr_handle)
time.sleep(1)

print(browser.title)

# 브라우저 컨트롤러 이동 확인
time.sleep(5)
browser.get("http://daum.net")

time.sleep(5)

