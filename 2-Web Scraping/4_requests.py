## requets : 웹페이지 정보를 가져오기 위해 설치해야 함 pip install requests
import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()
# 밑 if문 말고 위 코딩으로 요약해서 사용하면 됨

# print("응답코드 : "+str(res.status_code))    # 200 이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
    # print("문제가 생겼습니다. [에러코드 :", res.status_code,"]")

print(len(res.text))
print(res.text)

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)


