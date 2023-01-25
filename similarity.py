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

time.sleep(5.0)

rez_2 = str(html_create(vgm_url))

amount_symbols_1 = Counter(list(rez))
amount_symbols_2 = Counter(list(rez_2))
total_amount_symbols = len(list(rez))

raznica = 0
for i in amount_symbols_1:
    raznica += amount_symbols_2.get(i) - amount_symbols_1.get(i)

sim_percantage = ((total_amount_symbols - int(math.fabs(raznica)))/total_amount_symbols) * 100

print(sim_percantage)
