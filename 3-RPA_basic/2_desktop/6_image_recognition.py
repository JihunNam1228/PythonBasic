import pyautogui
import time
import sys

# # 이미지를 찾아서 수행하는 것보다 단축키가 정확도면에서 월등하다


# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# # 화면 내에서 지정한 아이콘들 지칭
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# # 속도 개선
# # 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# # 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(4620,888,150,150))
# pyautogui.moveTo(trash_icon)
# pyautogui.mouseInfo() # 위치 파악

# # 3. 정확도 조정(pip install opencv-python 설치)
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9)   # 정확도 90%
# pyautogui.moveTo(run_btn)

# # 자동화 대상이 바로 보여지지 않는 경우
# # 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notpad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notpad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_notepad)

# # 2. 일정 시간동안 기다리기 (TimeOut)
# timeout = 10
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notpad.png")
#     end = time.time()   # 종료 시간 설정
#     if end - start > timeout:   # 지정된 10초 초과하면
#         print("시간 종료")
#         sys.exit()


def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program")
        sys.exit()

# pyautogui.click(file_menu_notepad)

my_click("file_menu_notepad.png", 10)