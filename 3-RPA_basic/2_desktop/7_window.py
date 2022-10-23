import pyautogui

# # 현재 실행되고 있는 프로그램 기준에서 좌표 이동 가능
# fw = pyautogui.getActiveWindow()    # 현재 활성화된 창 (VSCode)
# print(fw.title) # 창의 제목 정보
# print(fw.size)  # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left+25, fw.top+25)

# for w in pyautogui.getAllWindows():
#     print(w)    # 모든 윈도우 가져오기(눈에 보이지 않는 프로그램도 출력)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate()  # 활성화 (맨 앞으로 가져오기)

pyautogui.sleep(1)

if w.isMaximized == False:  # 현재 최대화가 되지 않았다면
    w.maximize()    # 최대화

pyautogui.sleep(1)

# if w.isMinimized == False:  # 현재 최소화 되지 않았다면
#     w.minimize()

w.restore() # 화면 원복

w.close()   # 윈도우 닫기