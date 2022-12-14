# # 아래 동작을 자동으로 수행하는 프로그램을 작성하시오
# # 1. 그림판 실행(단축키 : win + r, 입력값 : mspaint) 및 최대화
# # 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
# #     - 입력 글자 :  "참 잘했어요"

# # 5초 대기 후 그림판 종료
# # 이 때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함
from cv2 import pyrUp
import pyautogui
import pyperclip

pyautogui.hotkey("win","r")
pyautogui.write("mspaint")
pyautogui.press("enter")
pyautogui.sleep(2)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]

if w.isMaximized == False:
    w.maximize()

# 400, 91
pyautogui.moveTo(400, 91, duration=0.5)
pyautogui.click()

pyautogui.move(-100,300, duration=0.5)
pyautogui.click()

# # 이미지를 상대기준으로 잡아서 해결
# btn_brush = pyautogui.locateOn.Screen("brush.png")
# pyautogui.click(btn_brush.left-200, btn_brush.top+200)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")
pyautogui.sleep(1)

my_write("참 잘했어요")
pyautogui.sleep(5)

w.close()
pyautogui.sleep(1)
pyautogui.hotkey("n")
