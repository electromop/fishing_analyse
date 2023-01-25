import requests
from bs4 import BeautifulSoup
from collections import Counter
import json

def del_symbols(ssilka):
    red_ssilka = list(ssilka)
    for i in ssilka:
        if ((ord(i) < 65) or (ord(i) > 122)) or ((ord(i) > 91) and (ord(i) < 97)):
            red_ssilka.remove(i)
    return ''.join(red_ssilka)

def html_create(vgm_url):
    html_text = requests.get(vgm_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup


vgm_url = str(input())
rez = Counter(str(html_create(vgm_url)))
rez[vgm_url] = 0
otred_ssilka = del_symbols(vgm_url)

text_file = open('orig_sites/' + otred_ssilka + '.json', "w", encoding='utf-8')
text_file.write(json.dumps(rez))
