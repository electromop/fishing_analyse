import requests
import json
import math
import os

from bs4 import BeautifulSoup
from collections import Counter

def html_create(vgm_url):
    html_text = requests.get(vgm_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

vgm_url = str(input())
parsed_url = str(html_create(vgm_url))
amount_symbols_2 = dict(Counter(list(parsed_url)))

bd_list = os.listdir(path='C:/Users/user/Desktop/codes/python_codes/fishing_analyse/orig_sites')
sim_percantage = {}

for x in range(len(bd_list)):
    with open('orig_sites/' + bd_list[x], 'r') as bd:
        amount_symbols_1 = json.loads(str(bd.read()))
    total_amount_symbols = sum(amount_symbols_1.values())

    raznica = 0
    for i in amount_symbols_2:
        if i in amount_symbols_1:
            raznica += amount_symbols_2.get(i) - amount_symbols_1.get(i)
        else:
            raznica -= amount_symbols_2.get(i)
    sim_percantage[bd_list[x]] = (((total_amount_symbols - int(math.fabs(raznica)))/total_amount_symbols) * 100)

print(sim_percantage)
with open('orig_sites/' + get_key(sim_percantage, max(sim_percantage.values())), 'r') as orig:
    orig_dict = json.loads(str(orig.read()))

if get_key(orig_dict, min(orig_dict.values())) == vgm_url:
    print("Не фишинг")
else:
    print("ОСТОРОЖНО!!! фишинг...")
