# # pip install selenium
# # chromedriver : 크롬으로 자동 제어 가능,주소창에 'chrome://version' 검색후 버전 확인 ex)106
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()    # 오픈되어 있는 폴더 아니라면 디렉토리 적어야댐 ex) "c:/downloads/chromedriver.exe"

# 1. 네이버 이동
browser.get("https://www.naver.com/")

# 2. 로그인 버튼 클릭
print("1111111111111111111")
elem = browser.find_element(By.CLASS_NAME, 'link_login')
print("23222222222222222")
elem.click()
print("333333333333333333333")
# browser.close()

# # 3. id, pw 입력
# browser.find_element_by_id("id").send_keys("ahtp0070")
# browser.find_element_by_id("pw").send_keys("sdfsdfdsfs@#23")

# # 4. 로그인 버튼 클릭
# browser.find_element_by_id("log.login").click()

# time.sleep(3)

# # 5. id를 새로 입력
# # browser.find_element_by_id("id").send_keys("my_id")
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("my_id")

# # 6. html 정보 출력
# print(browser.page_source)

# # 7. 브라우저 종료
# # browser.close() # 현재 탭만 종료
# browser.quit()  # 전체 브라우저 종료
