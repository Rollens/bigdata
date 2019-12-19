import sys
from bug import bug
import json
import requests
from datetime import datetime

def bug_date(target_date):
    url_list=[]
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
    for pages in range(1,5):
        url="https://www.cna.com.tw/cna2018api/api/simplelist/categorycode/aall/pageidx/"+str(pages)+"/"
        json_in=requests.get(url,headers=headers)
        if json_in.status_code == 200:
            res=json_in.json()
            for news in res['result']['SimpleItems']:
                news_datetime=datetime.strptime(news['CreateTime'],'%Y/%m/%d %H:%M')
                if target_date.date()==news_datetime.date():
                    url_list.append(news['PageUrl'])
    return bug(url_list)

if __name__=='__main__':
    target_date_argv=sys.argv[1]
    target_date=datetime.strptime(target_date_argv,'%Y-%m-%d')
    print(bug_date(target_date))