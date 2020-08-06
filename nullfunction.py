"""
Join to our telegram channel https://t.me/CAT_discord_dev
Jo to our telegram group https://t.me/catchatdev
Made by NullifiedVlad 2020
"""

from bs4 import BeautifulSoup
import requests


def ip():  # get ip
    heads = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}
    r = requests.get('https://2ip.ru/', headers=heads)
    soup = BeautifulSoup(r.text, 'html.parser')
    ip_address = soup.find('div', {'class': 'ip', 'id': 'd_clip_button'})
    return ip_address.text[1:]


def img_get(url):
    heads = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}
    r = requests.get(str(url), headers=heads)
    data = r.content
    return data
