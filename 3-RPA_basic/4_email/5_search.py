from imap_tools import MailBox
from account import *

# # 방법1
# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# mailbox.logout() -- 이거 필요하지만 아래 방법으로 간단하게 처리할 수 있음

# 방법2
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=5, reverse=True): # 전체 메일 다 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(UNSEEN)', reverse=True): # 읽지 않은 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # for msg in mailbox.fetch('(FROM ahtp0070@gmail.com)', limit=3, reverse=True): # 특정인이 보낸 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # # 작은 따옴표로 먼저 감싸고 실제 TEXT 부분은 큰 따옴표로 감싸주셈
    # for msg in mailbox.fetch('(TEXT "test mail")'): # 어떤 글자를 포함하는 메일 (제목, 본문)
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # # 한글 제약
    # for msg in mailbox.fetch('(SUBJECT "test mail")'): # 어떤 글자를 포함하는 메일 (제목만)
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # # 한글 우회 방법
    # for msg in mailbox.fetch(limit=5, reverse=True): # 어떤 글자(한글) 포함하는 메일 필터링(제목만)
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))
    
    # for msg in mailbox.fetch('(SENTSINCE 09-NOV-2020)', reverse=True, limit=5): # 특정 날짜 이후의 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # for msg in mailbox.fetch('(ON 09-NOV-2020)', reverse=True, limit=5): # 특정 날짜에 온 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(ON 09-NOV-2020)', reverse=True, limit=5): # 특정 날짜에 온 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # # 2가지 이상의 조건을 모두 만족하는 메일
    # for msg in mailbox.fetch('(ON 09-NOV-2020 SUBJECT "test mail")', reverse=True, limit=5): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건 중 하나라도 만족하는 메일 (또는 조건)
    for msg in mailbox.fetch('(OR ON 09-NOV-2020 SUBJECT "test mail")', reverse=True, limit=5): 
        print("[{}] {}".format(msg.from_, msg.subject))
    

