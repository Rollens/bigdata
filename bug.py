from find import get_map
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re

"""
Read README and get the list of classification
"""

def bug(classification):
    goto='https://www.cna.com.tw/list/'+classification+'.aspx'
    url_list=get_map(goto)
    express=r"<\s*p[^>]*>(.*?)<\s*/\s*p>"
    regex=re.compile(express)
    news_list=[]
    for url in url_list:
        r=requests.get(url)
        o_text=""
        if r.status_code == 200:
            print(r.status_code,"visit:",url)
            web_content=r.text
            soup=BeautifulSoup(web_content,'lxml')
            title=soup.find('h1').text
            index = soup.find('div', class_='paragraph')
            str_=str(index)
            text=regex.findall(str_)
            updatetime_str=soup.find('div',class_='updatetime').contents[1].contents[0]#'yyyy/mm/dd hh:mm'in string
            updatetime=datetime.strptime(updatetime_str,'%Y/%m/%d %H:%M')
            for i in text:
                o_text=o_text+i+"\n"
            dict_news={'title':title,'content':o_text,'post_time':updatetime,'url':url}
            news_list.append(dict_news)
        dict_news.clear()
    return news_list
"""
with open('output.txt','w',encoding='utf-8') as f:
    for i in news_list:
        f.write(i)
"""