import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_map(url):

#url="https://www.cna.com.tw/list/aipl.aspx"
    r=requests.get(url)
    express=r"https.*aspx"
    regex=re.compile(express)
    map=[]

    if r.status_code == 200:
        web_content=r.text
        soup=BeautifulSoup(web_content,'lxml')
        list_=soup.find(id="myMainList")
        for child in list_.children:
            str_=str(child)
            text=regex.findall(str_)[0]
            map.append(text)
    return map