from bs4 import BeautifulSoup

import requests
import random


def has_class_preview(tag):
    return tag.has_attr('class') and tag['class'][0] == 'preview'

def get_image_page_url():
    html = requests.get("https://wallhaven.cc/search?categories=110&purity=100&sorting=random&order=desc&ai_art_filter=1").content

    soup = BeautifulSoup(html, 'html.parser')
    previews = soup.find_all(has_class_preview)
    random_index = random.randrange(0, len(previews)) 
    image_url = previews[random_index]['href']

    return image_url

def get_image(image_page_url):
    html = requests.get(image_page_url).content

    soup = BeautifulSoup(html, 'html.parser')
    image_element = soup.find_all('img', id="wallpaper")[0]
    image_url = image_element['src']

    return image_url

def download_and_save_image(image_url):
    response = requests.get(image_url)
    file_name = image_url.split('/')[-1]

    with open(file_name, 'wb') as file:
        file.write(response.content)

page_url = get_image_page_url()
img_url = get_image(page_url)
download_and_save_image(img_url)
