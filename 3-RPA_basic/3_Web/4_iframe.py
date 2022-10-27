from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# # //*[@id="html"]

options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # frame 전환
browser.find_element(By.XPATH,'//*[@id="html"]').click()  # 잡힘
browser.switch_to.default_content() # 상위로 빠져 나옴
browser.find_element(By.XPATH,'//*[@id="html"]').click()  # 안잡힘
time.sleep(3)

