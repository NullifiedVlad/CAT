"""
Join to our telegram channel https://t.me/CAT_discord_dev
Jo to our telegram group https://t.me/catchatdev
Made by NullifiedVlad 2020
"""

from bs4 import BeautifulSoup
import requests


def ip():
    heads = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}
    r = requests.get('https://2ip.ru/', headers=heads)
    soup = BeautifulSoup(r.text, 'html.parser')
    block = soup.find('div', {'class': 'ip', 'style': 'width:250px'})
    ip_address = block.find('big', {'id': 'd_clip_button'})

    return ip_address.text
