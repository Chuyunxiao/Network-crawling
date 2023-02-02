import requests
from lxml import html
import pandas as pd
from matplotlib import pyplot as plt
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}
all_movie = []
counts = {}
for i in range(0, 226, 25):
    url = "https://movie.douban.com/top250?start=%d&filter="%(i)
    print(url)
    response = requests.get(url, headers=headers)
    print(response.status_code)  # ok 200
    data = response.text
    selector = html.fromstring(data)
    # 获取标签内容
    # // 代表任意路径
    # //标签1[@属性=属性值]/ 标签2[@属性=属性值] /text()
    movie_list = selector.xpath('//div[@id="content"]//ol/li')
    print(len(movie_list))
    for movie in movie_list:
        movie_name = movie.xpath('div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/span[1]/text()')[0]
        print(movie_name)

        movie_score = \
        movie.xpath('div[@class="item"]/div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
        print(movie_score)

        movie_eval = \
        movie.xpath('div[@class="item"]/div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()')[0]
        print(movie_eval)

        img_src = movie.xpath('div[@class="item"]/div[@class="pic"]/a/img/@src')[0]
        resp = requests.get(img_src, headers=headers)
        if resp.status_code == 200:
            # bytes 类型响应  wb 写二进制
            with open('./imgs/%s.jpg' % (movie_name), mode='wb') as f:
                f.write(resp.content)
        print(img_src)
        counts[movie_score] = counts.get(movie_score,0) + 1
        all_movie.append({
            "movie_name": movie_name,
            "movie_score": movie_score,
            "movie_eval": movie_eval,
            "img_src": img_src
        })
df = pd.DataFrame(all_movie)
df.to_csv('douban.csv', index=False)
values = list(counts.values())
labels = list(counts.keys())  # [9.6, 9.7]
plt.pie(values, labels=labels,autopct="%0.1f%%")
plt.show()
