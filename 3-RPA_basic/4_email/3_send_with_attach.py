from fileinput import filename
import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"    # 제목
msg["From"] = EMAIL_ADDRESS     # 보내는 사람
msg["To"] = "ahtp0070@gmail.com"    # 받는 사람
msg.set_content("다운로드 하세요")

# MINE Type : 어떤 파일 양식을 보낼지에 따라 maintype/subtype 달라지니, 구글 검색
# msg.add_attachment()
# with open("run_btn.png", "rb") as f:
#     msg.add_attachment(f.read(), maintype="image", subtype="png", filename="f.name")

with open("test.pdf","rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("test.xlsx","rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)


