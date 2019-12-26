import requests
from bs4 import BeautifulSoup

def hot_label():
    hot_label_list=[]
    url="https://tag.analysis.tw/"
    res=requests.get(url)
    if res.status_code == 200:
        web_content=res.text
        soup= BeautifulSoup(web_content,'lxml')
        trs= soup.find_all('tr', class_='trs')
        for tr in trs:
            hot_label_list.append(tr.contents[3].text)
    return hot_label_list

if __name__ == '__main__':
    print(hot_label())