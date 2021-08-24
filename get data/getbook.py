import requests

if __name__ == '__main__':
    ## 根地址  https://book.douban.com/tag/?view=type&icn=index-sorttags-all
    ## 然后获取每个tag 的链接 ，新链接中获取到第一页中的数据，然后依次进入页面 获取图书信息

    all_tags={}
    content= requests.get('https://book.douban.com/tag/?view=type&icn=index-sorttags-all')
    print(content)
    