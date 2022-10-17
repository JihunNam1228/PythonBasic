import requests
from bs4 import BeautifulSoup

for year in range(2015,2020):
    res = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={}+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84".format(year))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    images = soup.find_all("div", attrs={"class":"thumb"})

    for idx, image in enumerate(images):
        # print(image.a.img["src"])
        image_url = image.a.img["src"]

        if image_url.startswith("//"):
            image_url = "https:"+image_url
        print(image_url)
        
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        if idx >= 4:    # 상위 5개 이미지까지만 다운로드
            break