import requests
from bs4 import BeautifulSoup
import time
from collections import Counter
import math

vgm_url = str(input())

def html_create(vgm_url):
    html_text = requests.get(vgm_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup

rez = str(html_create(vgm_url))

text_file = open('fishing.txt', "w", encoding='utf-8')
text_file.write(rez)
