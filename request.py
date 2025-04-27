import requests
import json
from bs4 import BeautifulSoup

base_url = 'https://ssr1.scrape.center/detail/'
headers = {}

movies = []
movie_id = 1

while True:
    url = base_url + str(movie_id)
    movie = {}
    movie['id'] = movie_id

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        break
    soup = BeautifulSoup(res.text, 'html.parser')

    name = soup.find('h2', class_='m-b-sm').text.split('-')
    movie['cn_name'] = name[0]
    movie['en_name'] = name[1]

    tags = soup.find('div', class_='categories').find_all('button')
    movie['tags'] = []
    for tag in tags:
        movie['tags'].append(tag.text.strip())
    
    try:
        spans = soup.find_all('div', class_='m-v-sm info')
        movie['region'] = spans[0].find_all('span')[0].text.strip()
        movie['duration'] = spans[0].find_all('span')[2].text.strip()
        movie['release_time'] = spans[1].find('span').text.strip()
    except:
        movie['release_time'] = 'unknown'

    description = soup.find('div', class_='drama').find('p').text.strip()
    movie['description'] = description

    img_src = soup.find('img', class_='cover')['src']
    with open(f'./public/images/{movie_id}.jpg', 'wb') as file:
        img_res = requests.get(img_src)
        file.write(img_res.content)
    movie['img'] = f'../../public/images/{movie_id}.jpg'
    movies.append(movie)
    movie_id += 1


with open('./src/assets/movies.json', 'w') as file:
    json.dump(movies, file, ensure_ascii=False, indent=4)

print("Parsing completed.")