from urllib import request
from bs4 import BeautifulSoup
import os
import io
import re
import string
import datetime
import time
from time import strptime

if __name__ == '__main__':
    ## 根地址  https://book.douban.com/tag/?view=type&icn=index-sorttags-all
    ## 然后获取每个tag 的链接 ，新链接中获取到第一页中的数据，然后依次进入页面 获取图书信息

    all_tags={}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'

    req = request.Request(url=url,headers=headers)
    
    html = request.urlopen(req).read()
    main_soup = BeautifulSoup(html, 'lxml')
    total_page= main_soup('table',class_='tagCol')
    page = BeautifulSoup(str(total_page),'lxml').text
    print(page)
    #main_soup = BeautifulSoup(html, 'lxml')
