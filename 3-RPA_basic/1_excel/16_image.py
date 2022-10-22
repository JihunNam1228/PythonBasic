from openpyxl import Workbook
from openpyxl.drawing.image import Image
# # pip install Pillow 설치해야 이미지 삽입 가능

wb = Workbook()
ws = wb.active

img = Image("img.png")

# C3 위치에 img.png 파일의 이미지를 삽입
ws.add_image(img, "C3")

wb.save("sample_image.xlsx")