from urllib import request
from urllib.parse import unquote,quote
from bs4 import BeautifulSoup
import os
import io
import re
import string
import datetime
import time
from time import strptime


def get_response_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


    req = request.Request(url=url,headers=headers)
    
    html = request.urlopen(req).read()
    main_soup = BeautifulSoup(html, 'lxml')
    
    return main_soup 
    

def get_top10_book_of_each_tag(list):
    booklist =[]
    for url in list:
        main_soup = get_response_html(url)
        total_books= main_soup('h2')
        for bookinfo in BeautifulSoup(str(total_books),'lxml').find_all('a'):
            book_url = bookinfo['href']
            booklist.append(book_url)
        
        time.sleep(1)
    return booklist


def get_all_detail_books(book_list):

    book_json_list=[]
    
    for  book in book_list:
        book_info = {}
        main_soup = get_response_html(book)
        book_cover_img = main_soup.select('a[class="nbg"]')
        
        item_key_list = BeautifulSoup(str(main_soup.select('div[id="info"]')),'lxml').text
        a = re.compile(r'&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020|\r')
        item_key_list = a.sub('', item_key_list).replace('\n','',4).replace('[','').replace(']','').replace(r'元','')
                                                #删除前面多少个换行符  
        print(item_key_list)
        print('_'*40)
        for  item in re.split('\n',item_key_list):
            if item !='':
                print(item)
                print('_'*40)
                book_info[item[0:item.index(':')]] = item[item.index(':')+1:]
            else:
                break     
        book_json_list.append(book_info)
    print(book_json_list)
    
    return book_json_list 




def insert_into_db(list):
    


def test():
     str1 = '作者:林奕含\n出版社:北京联合出版公司\n出品方:磨铁图书\n出版年:2018-2\n页数:272\n定价:45.00\n装帧:平装\nISBN:9787559614636'
     book={}
     for item in re.split('\n',str1):
        
        key1 = item[0:item.index(':')]
        value1 = item[item.index(':')+1:] 
        #print(key1)
        #print(value1)
        book[key1] =value1

     print(book)
     #print(str1)
    
if __name__ == '__main__':
    ## 根地址  https://book.douban.com/tag/?view=type&icn=index-sorttags-all
    ## 然后获取每个tag 的链接 ，新链接中获取到第一页中的数据，然后依次进入页面 获取图书信息

    # url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    # main_soup=get_response_html(url)
    # total_page= main_soup('table',class_='tagCol')


    # total_tags_url=[]
    # detail_book_url_list=[]
    # all_books=[]

    # tag_base_url='https://book.douban.com/tag/'
    # for i in BeautifulSoup(str(total_page),'lxml').find_all('a'):
    #     total_tags_url.append(tag_base_url+quote(i.text))

    # #print(total_tags_url)      
    # detail_book_url_list = get_top10_book_of_each_tag(total_tags_url)

    #test()
    detail_book_url_list=['http://book.douban.com/subject/27614904/']

    ##detail_book_url_list =['https://book.douban.com/subject/4913064/']
    all_books=get_all_detail_books(detail_book_url_list)

    insert_into_db(all_books)    