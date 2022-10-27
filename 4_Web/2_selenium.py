from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 쓸데없는 로그 숨김
options = Options()
options.add_experimental_option('detach', True) # 브라우저 바로 닫힘 방지
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거

# # *********** 웹드라이버 설치 없이 진행 할 수 있음
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)