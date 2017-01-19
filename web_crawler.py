import urllib.request

# constants
HTML_TAG_URL = '<a href='

def get_page(url):
    """This function return the html code of a website"""
    
    try:

        return urllib.request.urlopen(url).read().decode('utf-8')

    except:
        return ""

def get_next_url(page):
    """This function returns a url and the end point of the url"""

    try:

        start_html_tag = page.find(HTML_TAG_URL)
        # Link in the website not found
        if start_html_tag == -1:
            return None, 0

        start_pos_url = page.find('"', start_html_tag)
        end_pos_url = page.find('"', start_pos_url+1)   
        url = page[start_pos_url+1:end_pos_url]

        return url, end_pos_url

    except Exception as e:
        print ( "Error in get_next_url: %s" % str(e) )

def union_lists(list1, list2):
    try:
        
        for element in list2:
            if element not in list1:
                list1.append(element)

    except Exception as e:
        print ( "Error in union_lists: %s" % str(e) )

def get_all_urls(page):
    """This function returns all urls of the website"""

    try:
        
        url_list = []
            
        while True:
            url, end_pos_url = get_next_url(page)
            
            if url:
                url_list.append(url)
                page = page[end_pos_url:]
                
            else:
                break

        return url_list
            
    except Exception as e:
        print ( "Error in get_all_urls: %s" % str(e) )

def crawl_web(start_url, max_crawl_depth):
    """This function get all links within a website and crawl each of them"""

    try:
        urls_to_crawl = [start_url]
        urls_crawled = []
        urls_next_depth = []
        depth = 0
        index = []

        while urls_to_crawl and depth <= max_crawl_depth:
            page_to_crawl = urls_to_crawl.pop()
            
            if page_to_crawl not in urls_crawled:
                content_page = get_page(page_to_crawl)
                add_page_to_index(index, page_to_crawl, content_page)
                union_lists(urls_next_depth, get_all_urls(content_page))
                urls_crawled.append(page_to_crawl)

            if not urls_to_crawl:
                urls_to_crawl = urls_next_depth
                urls_next_depth = []
                depth = depth + 1

        return index
                

    except Exception as e:
        print ( "Error in crawl_web: %s" % str(e) )

def add_to_index(index, keyword, url):
    """This function build the index of the searchengine"""

    try:
    
        for entry in index:
            if entry[0] == keyword:
                for urls in entry[1]:
                    if urls[0] == url:
                        return
                entry[1].append([url, 0])
                return
                
        index.append([keyword,[[url, 0]]])

    except Exception as e:
        print ( "Error in add_to_index: %s" % str(e) )

def index_lookup(index, keyword):
    """This function looks for the keyword in the index and return the entry or a empty list"""

    try:

        for entry in index:
            if keyword == entry[0]:
                return entry[1]
        return []

    except Exception as e:
        print ( "Error in lookup: %s" % str(e) )

def add_page_to_index(index, url, content):

    try:

        keywords = content.split()
        for keyword in keywords:
            add_to_index(index, keyword, url)

    except Exception as e:
        print ( "Error in add_page_to_index: %s" % str(e) )

def record_user_click(index, keyword, url):
    """This function increases the count of website clicks for a specific keyword"""

    try:
        
        result_of_urls = index_lookup(index, keyword)
        if result_of_urls:
            for entry in result_of_urls:
                if entry[0] == url:
                    entry[1] = entry[1]+1
                        
    except Exception as e:
        print ( "Error in record_user_click: %s" % str(e) )

# Select a url for a website
# Request
# Handle the response --> result page

index = []

#print (crawl_web("http://www.udacity.com/cs101x/index.html",0))
#print (crawl_web("http://www.udacity.com/cs101x/index.html",1))
#print (crawl_web("http://www.udacity.com/cs101x/index.html",50))
#print (crawl_web("http://www.udacity.com/cs101x/index.html",2))
#add_page_to_index(index, 'fake.test', "This is a test")
#print (index)
#add_page_to_index(index, 'not.test', "This is not a test")
#print (index)
#print (get_page("https://hellobasti.github.io/"))

index = crawl_web('http://www.udacity.com/cs101x/index.html', 10)
print (index_lookup(index, 'good'))





