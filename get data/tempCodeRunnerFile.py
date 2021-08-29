url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    main_soup=get_response_html(url)
    total_page= main_soup('table',class_='tagCol')


    total_tags_url=[]
    detail_book_url_list=[]
    all_books=[]

    tag_base_url='https://book.douban.com/tag/'
    for i in BeautifulSoup(str(total_page),'lxml').find_all('a'):
        total_tags_url.append(tag_base_url+quote(i.text))

    #print(total_tags_url)      
    detail_book_url_list = get_top10_book_of_each_tag(total_tags_url)