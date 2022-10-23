import pyautogui
# 화면 테두리 끝을 대면 실행 종료가 되어 FAILSAFE 뜸. 그걸 없애는 옵션
# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용

# 마우스 실시간으로 위치와 지칭 색상 확인
# F1 사용해서 복사
# pyautogui.mouseInfo()


# 70,1044 255,255,255 #FFFFFF

for i in range(5):
    pyautogui.move(100,100)
    pyautogui.sleep(1)
