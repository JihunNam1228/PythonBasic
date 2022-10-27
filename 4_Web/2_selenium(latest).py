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


driver.maximize_window()
url = "https://naver.com"
driver.get(url)
time.sleep(1)

# driver.find_element(By.CLASS_NAME, "input_text").send_keys("블랙핑크")
# time.sleep(1)

# driver.find_element(By.ID, "query").send_keys("뉴진스")
# time.sleep(1)

# driver.find_element(By.NAME, "query").send_keys("트와이스")
# time.sleep(1)

# # 다양한 정보들을 뽑을 수 있다
# driver.find_element(By.CSS_SELECTOR, "[title='검색어 입력']").send_keys("에스파")
# time.sleep(1)

# driver.find_element(By.XPATH, '//*[@id="query"]').send_keys("에스파")
# time.sleep(1)

# driver.find_element(By.LINK_TEXT,"쇼핑LIVE").click()

# # 일부분만 있어도 찾을 수 있다
# driver.find_element(By.PARTIAL_LINK_TEXT,"핑LI").click()



# # 잘 안쓰임
# navs = driver.find_elements(By.CSS_SELECTOR,".nav")

# for nav in navs:
#     print(nav.get_attribute("outerHTML"))
#     print()

# time.sleep(3)
