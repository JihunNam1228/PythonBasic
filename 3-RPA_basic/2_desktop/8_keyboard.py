import pyautogui
# w = pyautogui.getWindowsWithTitle("제목 없음")[0]   # 메모장 1개 띄운 상태에서 가져옴
# w.activate()

# pyautogui.write("12345465")
# pyautogui.write("NadoCoding", interval=0.2)

# # 치명적 단점 : 한글 지원 X
# pyautogui.write("나도 코딩")

# pyautogui.write(["t","e","s","t","left","left","right", "l", "a","enter"], interval=0.2)
# r# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 2번, l a 순서대로 적고 enter 입력

# 'automate the boring stuff with python' 검색 후 홈피 접속해서 chapter20> 키보드 관련 속성들 참고

# # 특수 문자
# # shift 4 -> $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4")    # 숫자 4를 입력하고
# pyautogui.keyUp("shift")    # shift 키를 뗀다

# # 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# # 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# # Ctrl > Alt > Shift > A > A > Shift > Alt > Ctrl
# pyautogui.hotkey("ctrl", "a")


# # 한글 우회 사용 방법
# # pip install pyperclip
# import pyperclip
# # pyperclip.copy("나도코딩")  # '나도코딩' 글자를 클립보드에 저장
# # pyautogui.hotkey("ctrl","v")    # 클립보드에 있는 내용을 붙여넣기

# def my_write(text):
#     pyperclip.copy(text)
#     pyautogui.hotkey("ctrl","v")

# my_write("나도코딩")

# # 자동화 프로그램 종료
# # win : ctrl + alt + del
# # mac : cmd + shift + option + q