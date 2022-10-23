import pyautogui
from pyscreeze import pixel
# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")  # 파일로 저장
# 868,459 178,196,168 #B2C4A8
# pyautogui.mouseInfo()

pixel = pyautogui.pixel(868,459)
print(pixel)    # 해당 위치의 색상을 출력

#print(pyautogui.pixelMatchesColor(868,459, (178,196,168)))
#print(pyautogui.pixelMatchesColor(868,459, pixel))
print(pyautogui.pixelMatchesColor(868,459, (18,196,168)))
