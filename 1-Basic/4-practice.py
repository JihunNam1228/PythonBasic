# ##########################  예외처리  ###########################
# from multiprocessing.sharedctypes import Value


# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)



# ##########################  에러 발생시키기  ###########################
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. \n한 자리 숫자만 입력하세요.")



# ##########################  사용자 정의 예외처리  ###########################
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1,num2))
#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. \n한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:    # 예외처리가 나도 무조건 실행할 수 있게 하는 매개체
#     print("계산기를 이용해 주셔서 감사합니다.")



# # Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# # 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# # 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# # 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
# #         출력 메시지 : "잘못된 값을 입력하였습니다."
# # 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
# #         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
# #         출력 메시지 : "재고가 소진되어 더이상 주문을 받지 않습니다.
# # [코드]

# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작

# class SoldOutError(Exception):
#     pass

# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호{0}] {1}마리 주문이 완료되었습니다.".format(waiting,order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더이상 주문을 받지 않습니다.")
#         break







##########################  모듈(module)  ###########################
# # 내려갈수록 편리한 방식
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화보러 갔을 때

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)

# from theater_module import price_soldier as price
# price(4)



##########################  패키지(package)  ###########################
# # 모듈(module)의 집합체
# import travel.thailand  # 끝은 무조건 패키지나 모듈만 위치해야 됨
# trip_to = travel.thailand.TailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()



##########################  __all__  ###########################
# from travel import *    # 패키지 내 모듈 중 공개 비공개 구분할 수 있음
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()



##########################  모듈 직접 실행  ###########################
# from travel import *  
# trip_to = thailand.ThailandPackage()    # 외부적으로 실행
# trip_to.detail()



##########################  패키지, 모듈 위치  ###########################
# # 모듈을 호출하는 동일한 폴더 혹은 파이썬 내 라이브러리 모여있는 곳에서 사용 가능
# # 모듈, 패키지를 위치 파악해주는 매개체 inspect
# import inspect
# import random

# from travel import thailand

# print(inspect.getfile(random))
# print(inspect.getfile(thailand))



##########################  pip install  ###########################
# # 패키지를 설치하는 방법
# # google > pypo > 자신이 원하는 패키지 찾아 설치
# # pip list : 자신이 설치된 패키지 출력
