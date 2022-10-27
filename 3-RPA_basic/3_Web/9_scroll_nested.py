from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# # //*[@id="html"]

options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()
browser.get('https://www.w3schools.com/html/')

time.sleep(3)

# 특정 영역 스크롤
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[62]')

# # 방법1. ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()


# 방법2 : 좌표 정보 이용
xy = elem.location_once_scrolled_into_view  # 함수 x () x
print("type : ", type(xy))   # dict
print("value : ", xy)

elem.click()
time.sleep(3)

