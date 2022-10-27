# 구글 환경설정
# 비번 2차 인증 On, 앱비밀번호 생성
import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 잘 수립되는지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)   # 로그인

    subject = "test mail"   # 메일 제목
    body = "mail body"  # 메일 본문

    msg = f"Subject: {subject}\n{body}"
    # 발신자 수신자 정해진메시지
    smtp.sendmail(EMAIL_ADDRESS, "ahtp0070@gmail.com", msg)
    


