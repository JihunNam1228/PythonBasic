# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*10)

# # 참 / 거짓
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not 5 > 10)

# # 애완동물을 소개해주세요
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# print("우리집 "+animal+"의 이름은 "+name+"예요")

# hobby = "공놀이"
# # print("연탄이는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
# print("연탄이는 ",age,"살이며, "+hobby+"을 아주 좋아해요")
# print("연탄이는 어른일까요? "+str(is_adult))

# '''
# 이렇게 하면 여러 문장이 주석
# 처리됩니다
# '''

# # Quiz) 변수를 이용하여 다음 문장을 출력하시오

# 변수명 : station
# 변수값 : "사당","신도림","인천공항" 순서대로 입력
# 출력 문장 : xx행 열차가 들어오고 있습니다

# station = "사당"
# print(str(station)+"행 열차가 들어오고 있습니다")
# station = "신도림"
# print(str(station)+"행 열차가 들어오고 있습니다")
# station = "인천공항"
# print(str(station)+"행 열차가 들어오고 있습니다")



# ########################### 연산자 ###########################
# print(1+1)
# print(3-1)
# print(5*2)
# print(6/3)

# print(2**3) #2^3
# print(5%3) #나머지 구하기 2
# print(10%3) #1
# print(5//3) #몫1
# print(10//3) #몫3

# print(10>3) #True
# print(4>=7) #False
# print(10<3) #False
# print(5<=5) #True


# # 좌우값이 같은지
# print(3==3) #True
# print(4==2) #False
# print(3+4 == 7) #True
# print(1!=3) #True
# print(not(1!=3)) #False

# print((3>0) and (3<5)) #True
# print((3>0) & (3<5)) #True

# print((3>0) or (3>5)) #True
# print((3>0)|(3>5)) #True

# print(5>4>3) #True
# print(5>4>7) #False



# ############################## 간단한 수식 ###########################
# print(2+3*4) #14
# print((2+3)*4) #20
# number = 2+3*4 #14
# print(number)
# number = number + 2 #16
# print(number)
# number += 2 #18
# print(number)
# number *= 2 #36
# print(number)
# number /= 2 #18
# print(number)
# number -= 2 #16
# print(number)
# number %= 5 #1
# print(number)



# ############################### 숫자 처리 함수 ###########################
# print(abs(-5)) #5
# print(pow(4,2)) #4^2 = 4*4 = 16
# print(max(5,12)) #12
# print(min(5,12)) #5
# print(round(3.14)) #3
# print(round(4.99)) #5

# from math import *
# print(floor(4.99)) #내림 4
# print(ceil(3.14)) #올림 3
# print(sqrt(16)) #제곱근 4



################################# 랜덤 함수 ###########################
# from random import *
# print(random()) #0.0~1.0 미만의 임의의 값 생성
# print(random()*10) #0.0~10.0 미만의 임의의 값 생성
# print (int(random()*10)) #0~10 미만의 임의의값 생성
# print (int(random()*10)) #0~10 미만의 임의의값 생성
# print (int(random()*10)) #0~10 미만의 임의의값 생성
# print (int(random()*10)+1) #1~10 이하의 임의의값 생성
# print (int(random()*10)+1) #1~10 이하의 임의의값 생성
# print (int(random()*10)+1) #1~10 이하의 임의의값 생성
# print (int(random()*10)+1) #1~10 이하의 임의의값 생성
# print (int(random()*10)+1) #1~10 이하의 임의의값 생성

# print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
# print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
# print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
# print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
# print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
# print(int(random()*45)+1) #1~45 이하의 임의의 값 생성

# print(randrange(1,46)) #1~46미만의 임의의 값 생성
# print(randrange(1,46)) #1~46미만의 임의의 값 생성
# print(randrange(1,46)) #1~46미만의 임의의 값 생성
# print(randrange(1,46)) #1~46미만의 임의의 값 생성
# print(randrange(1,46)) #1~46미만의 임의의 값 생성
# print(randrange(1,46)) #1~46미만의 임의의 값 생성
# print(randrange(1,46)) #1~46미만의 임의의 값 생성

# print(randint(1, 45)) #1~45이하의 임의의 값 생성
# print(randint(1, 45)) #1~45이하의 임의의 값 생성
# print(randint(1, 45)) #1~45이하의 임의의 값 생성
# print(randint(1, 45)) #1~45이하의 임의의 값 생성
# print(randint(1, 45)) #1~45이하의 임의의 값 생성
# print(randint(1, 45)) #1~45이하의 임의의 값 생성

# # Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# # 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# # 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# #조건1 : 랜덤으로 날짜를 뽑아야 함
# #조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# #조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# #(출력문 예제)
# # 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.
# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 "+str(date)+"일로 선정되었습니다.")



# ########################## 문자열 ###########################
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)



# ########################## 슬라이싱 ###########################
# jihun = "901228-1802519"
# print("성별 : "+jihun[7])
# print("연 : "+jihun[0:2]) #0~2직전까지 (0,1)
# print("월 : "+jihun[2:4])
# print("일 : "+jihun[4:6])

# print("생년월일 : "+jihun[:6]) # 처음부터 6직전까지
# print("뒤 7자리 : "+jihun[7:]) # 7부터 끝까지
# print("뒤 7자리 (뒤에서부터)"+jihun[-7:]) #맨 뒤에서 7번째부터 끝까지



# ########################## 문자열 처리 ###########################
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python","Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("n"))
# print(python.find("Java")) #포함되어 있지 않으면 '-1'로 출력
# # print(python.index("java")) #포함되어 있지 않으면 '오류'로 처리

# print(python.count("n")) #문자열 내, "n" 갯수 출력



########################## 문자열 포맷 ###########################
# print("a"+"b")
# print("a","b")

# # 방법 1
# print("나는 %d살입니다." %20) # %d : 정수
# print("나는 %s을 좋아해요." %"파이썬") # %s : 문자열
# print("Apple은 %c로 시작해요" %"A") # %c : 한 글자만

# # %s
# print("나는 %s살입니다." %20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간"))

# # 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age=20))

# # 방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")



########################## 탈출 문자 ###########################
# # \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")

# # \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다.
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.


# # \\ : 문장 내에서 '\' 표현
# print("C:\\Users\\남지훈\\Desktop\\PythonWorkspace>")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")


# # Quiz) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# # 예) http://naver.com
# # 규칙1 : http:// 부분은 제외 => naver.com
# # 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# # 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
# #                       (nav)       (5)              (1)        (1)
# # 예) 생성된 비밀번호 nav51!

# ## 내가 한거
# site1 = "http://daum.com"
# site2 = site1[7:]
# site3 = site2.index(".")
# site4 = site2[:site3]
# pw = site4[:3]
# cnt = len(site4)
# ecnt = site4.count("e")
# print("생성된 비밀번호 : "+pw+str(cnt)+str(ecnt)+"!")


# ## 정답
# url = "http://naver.com"
# my_str = url.replace("http://","") # 규칙1
# # print(my_str)
# my_str = my_str[:my_str.index(".")] # 규칙2
#  # my_str[0:5] -> 0~5 직전까지 (0,1,2,3,4)
# # print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))+"!"
# print("{0}의 비밀번호는 {1}입니다.".format(url, password))



########################## 리스트 ###########################

# # 지하철 칸별로 10명, 20명 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10,20,30]
# print(subway)

# subway = ["유재석","조세호","박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# # 정형돈씨를 유재석 / 조세호 사이에 태봄
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

# print(subway.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호",20,True]
# # print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)



########################## 사전 ###########################
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5])
# print(cabinet.get(5)) # []의 값x->error, get의 값x->None
# print(cabinet.get(5, "사용 가능"))
# print("hi")


# print(3 in cabinet) #True
# print(5 in cabinet) #False


# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key들만 출력
# print(cabinet.keys())

# # value들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)



########################## 튜플 ###########################
# # 속도가 list보다 빠름, 변경 불가하고 값을 고정할때 사용
# menu = ("돈까스","치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name,age,hobby)



########################## 세트 ###########################
# # 집합 (set)
# # 중복 안됨, 순서 없음
# my_set = {1,3,2,3,3}
# print(my_set)

# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])

# # 교집합 (java와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java도 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 (java 할 수 있지만 python 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)



########################## 자료구조의 변경 ###########################
# # 커피숍
# menu = {"커피","우유","주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))


# # Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# #      참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# #      댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# #      추첨 프로그램을 작성하시오

# # 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# # 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# # 조건3 : random 모듈의 shuffle과 sample을 활용

# # (출력 예제)
# # -- 당첨자 발표 --
# # 치킨 당첨자 : 1
# # 커피 당첨자 : [2, 3, 4]
# # -- 축하합니다 --

# # (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1)) #리스트 값중 무작위 1개 출력

# # 정답
# from random import *
# users = range(1, 21) #1~20까지 숫자 생성
# # print(type(users))
# users = list(users)
# # print(type(users))
# shuffle(users)
# print(users)

# winners = sample(users, 4) # 4명 중에서 1명 치킨, 3명 커피

# print(" -- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")



##########################      if      ###########################
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추우니깐 나가지 마세요")



##########################      for      ###########################
# print("대기 번호 : 1")
# print("대기 번호 : 2")
# print("대기 번호 : 3")
# print("대기 번호 : 4")

# randrange()
# for waiting_no in range(5): # 0,1,2,3,4
# for waiting_no in range(1,6): # 1,2,3,4,5
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨","토르","아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다".format(customer))



##########################      while      ###########################
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피가 폐기처분되었습니다")

# customer = "아이언맨"
# index = 1
# while True: # Ctrl + c 누르면 종료됨
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer,index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")



##########################    continue와 break    ###########################
# absent = [2,5] # 결석
# no_book = [7] # 책을 안가져옴
# for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어줘".format(student))



##########################    continue와 break    ###########################
# # 출석번호가 1 2 3 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# student = [1,2,3,4,5]
# print(student)
# students = [i+100 for i in student]
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# # 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)


# # Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
# #      50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# # 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# # 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# # (출력문 예제)
# # [O] 1번째 손님 (소요시간 : 15분)
# # [ ] 2번째 손님 (소요시간 : 50분)
# # [O] 3번째 손님 (소요시간 : 5분)
# # ...
# # [ ] 50번째 손님 (소요시간 : 16분)
# # 총 탑승 승객 : 2 분

# # 내가 한거
# list =[]
# cnt = 0
# for customer in range(0,51):
#     time = randint(5,50)
#     list.append(time)
#     if 5<=list[customer]<=15:
#         print("[O] {0}번째 손님(소요시간 : {1}분)".format(customer,time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님(소요시간 : {1}분)".format(customer,time))
# print("총 탑승 승객 : {}".format(cnt))

# # 정답
# cnt = 0 # 총 탑승 승객 수 
# for i in range(1,51): # 1~50
#     time = randrange(5,51) # 5~50분 사이
#     if 5<=time<=15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("총 탑승 승객 : {}".format(cnt))



##########################    함수    ###########################
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money):    # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
#     return balance+money

# def withdraw(balance, money):   # 출금
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100 # 수수료
#     return commission, balance-money-commission


# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# print(balance)



##########################    함수의 기본값    ###########################
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name,age,main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# # 같은 학교 같은 학년 같은 반 같은 수업.
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name,age,main_lang))

# profile("유재석")
# profile("김태호")



##########################    키워드값    ###########################
# def profile(name, age, main_lang):
#     print(name,age,main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")



##########################    가변인자    ###########################
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift")



##########################  지역변수와 전역변수  ###########################
# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun  # 전역 공간에 있는 gun 사용, 함수 내 전역변수를 무분별하게 사용하면 안좋음
#     gun = gun - soldiers
#     print("[함수내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계근무 나감

# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# # # Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# # * 표준 체중 : 각 개인의 키에 적당한 체중

# # (성별에 따른 공식)
# # 남자 : 키(m) x 키(m) x 22
# # 여자 : 키(m) x 키(m) x 21

# # 조건1 : 표준 체중은 별도의 함수 내에서 계산
# #         * 함수명 :std_weight
# #         * 전달값 : 키(height), 성별(gender) 
# # 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# # (출력 예제)
# # 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# def std_weight(height, gender):
#     if gender == "남자":
#         weight = round(height*height*22*0.0001,2)
#         print("키 {0}cm 남자의 표준 체중은 {1}kg입니다.".format(height,weight))
#     elif gender == "여자":
#         weight = round(height*height*21*0.0001,2)
#         print("키 {0}cm 여자의 표준 체중은 {1}kg입니다.".format(height,weight))
# std_weight(178,"남자")
# std_weight(160,"여자")



##########################  표준 입출력  ###########################
# print("Python", "Java", "JavaScript", sep=" vs ")
# print("Python", "Java", "JavaScript", sep=",", end="? ")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# answer = 10
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")



##########################  다양한 출력 포맷  ###########################
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리마다 콤마를 찍어주기
# print("{0:,}".format(10000000000))
# # 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(10000000000))
# # 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니깐 빈 자리는 ^로 채워주기
# print("{0:^<+30,},".format(1000000000000000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자릿수 까지만 표시 (소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))



##########################  파일 입출력  ###########################
# score_file = open("score.txt","w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")   # 줄바꿈 x
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# # 한 줄 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# # 읽을 파일 내용 줄을 알 수 없을때
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# # 리스트를 사용하여 출력
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()



##########################  pickle  ###########################
# # 사용하고 있는 데이터를 파일 형태로 저장하는 키워드

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()



##########################  with (파일 입출력시 이걸로 ㅊㅊ)  ###########################
# # 위 내용보다 편한 방식, 매번 close 함수를 사용하지 않아 편리

# with open("profile.pickle", "rb") as profile_file: # 파일의 내용을 profile_file 변수에 저장
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


# # Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# #       보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# # - x주차 주간보고 -
# # 부서 :
# # 이름 : 
# # 업무 요약 :

# # 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# # 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

# for i in range(1,51):
#     with open(str(i)+"주차.txt", "w", encoding="utf8") as study_file:
#         study_file.write("- " + str(i) + " 주차 주간보고 -")
#         study_file.write("\n부서 :")
#         study_file.write("\n이름 :")
#         study_file.write("\n업무 요약 :")



##########################  클래스(class)  ###########################
# # 마린 : 공격 유닛, 군인, 총 사용
# name = "마린"
# hp = 40
# damage = 5
# print("{} 유닛이 생성되었습니다".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크 , 포 사용, 일반모드/시저모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{} 유닛이 생성되었습니다".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
# print("{} 유닛이 생성되었습니다".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name,location,damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# # 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# # 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))


# # 마인드 컨트롤 : 상대방 유닛을 내 것을 만드는 것
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


# # 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 반향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# # 메딕 :의무병
# # 파이어뱃
# firebat1 = AttackUnit("파이어뱃", 50 ,16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# # 드랍십 : 공중 유닛, 공격x
# # 날 수 있는 기능 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):   # 재정의
        print("[공중 유닛 이동")
        self.fly(self.name, location)

# # 발키리 : 공중 공격 유닛
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# # 벌쳐 : 지상 유닛
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # Unit.__init__ 차이 : super()와 self 안들어감 
        self.location = location

# # 서플라이 디폿 : 건물, 1개 = 8유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass  # 완성하진 않았지만 일단 아무것도 안하고 그냥 넘어감

# game_start()
# game_over()



# # practice_class.py로