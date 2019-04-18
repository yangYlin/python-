# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 16:24:47 2018

@author: icetong
"""

import requests
from urllib.parse import quote
import time
from random import sample,choice








#随机选择一个浏览器

def select_user_agent():
    uas = [
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
        "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
        "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
        "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
        "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    ]
    user=choice(uas)
    user_dict={}
    user_dict['user-agent']=user
    return user_dict
    
    


'''headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\
           /537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
'''

#解析页面
def parse_one_page(items):
    for item in items:
        desc = item['description']
        itemId = str(item['itemId'])
        location = item['itemLocation']
        nick = item['nick']
        picUrl = item['picUrl']
        price = str(item['price']) if 'price' in item else '--'
        realPrice = str(item['realPrice'])
        saleCount = str(item['saleCount'])
        result.append([itemId, desc, nick, location, price, 
                       realPrice, saleCount, picUrl])
    
#请求页面
def requests_one_page(url,parmas):
    for p in range(1, page_num+1):
        parmas['page'] = str(p)
        r = requests.get(url, headers=select_user_agent(), params=parmas)
        data = r.json()
        items = data['result']['auction']
        parse_one_page(items)
    
    print("page: {}".format(p))
    time.sleep(2)
    
'''
result = []
for p in range(1, page_num+1):
    parmas['page'] = str(p)
    r = requests.get(url, headers=select_user_agent(), params=parmas)
    data = r.json()
    items = data['result']['auction']
    for item in items:
        desc = item['description']
        itemId = str(item['itemId'])
        location = item['itemLocation']
        nick = item['nick']
        picUrl = item['picUrl']
        price = str(item['price']) if 'price' in item else '--'
        realPrice = str(item['realPrice'])
        saleCount = str(item['saleCount'])
        result.append([itemId, desc, nick, location, price, 
                       realPrice, saleCount, picUrl])
    print("page: {}".format(p))
    time.sleep(2)
'''

#保存为csv文件
def save_as_csv():
    
    with open("{}2.csv".format(key_word), "w", encoding="gbk") as f:
        f.write(",".join(['itemId', 'desc', 'nick', 'location', 'price', 
                           'realPrice', 'saleCount', 'picUrl'])+'\n')
        content = "\n".join([",".join(l) for l in result])
        f.write(content.encode("gbk", "ignore").decode("gbk"))



page_num =90
result = []#存放结果
key_word = "羽毛球拍"

def main():
    url = "https://ai.taobao.com/search/getItem.htm"

    parmas = {'_tb_token_': '353a8b5a1b773',
          '__ajax__': '1', 
          'pid': 'mm_10011550_0_0',
          'page': '1',
          'pageSize': '60', 
          'sourceId': 'search',
          'pageNav': 'false',
          'key': quote(key_word),
          'debug': 'false',
          'maxPageSize': '200',
          'npx': '50'}

    requests_one_page(url,parmas)
    save_as_csv()

if  __name__=="__main__":
    #main()
    s=time.time()
    main()
    e=time.time()
    print("完成！！时间为：{}".format(e-s))
