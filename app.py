import json
import re
import sys
import requests
from bs4 import BeautifulSoup

def api(lat,lon):
    # アクセスするURL
    url = "https://weathernews.jp/onebox/" + str(lat) + "/" + str(lon) + "/"

    # URLにアクセスする htmlが帰ってくる
    html = requests.get(url)

    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html.text, "html.parser")
    # 天気取得
    table = soup.find_all("table",class_="fcst-table-weekly")

    #天気格納前処理
    arr = []
    M = str(table)
    L = re.split('"',M)

    j = 0
    for i in range(175):
        line = str(L[i])
        if ('title=' in line ):
            txt = str(L[i+1])
            if("Rain" in txt):arr.append("雨")
            elif("Fine" in txt):arr.append("晴")
            else:arr.append("曇")    
            j = j + 1

    return arr