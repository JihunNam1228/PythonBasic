## requets : 웹페이지 정보를 가져오기 위해 설치해야 함 pip install requests
import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/106.0.0.0 Safari/537.36"}    # 실제로 사람이 접속하는 걸로 전환 방법
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html","w",encoding="utf8") as f:
    f.write(res.text)

## 내 google > 'user agent string' 검색 > What is my User Agent? site 접속
## 접속하는 유형에 따라 agent 넘버가 달라짐

