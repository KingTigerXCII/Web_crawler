# constants
HTML_TAG_URL = '<a href='

def get_page(url):
    """This function is just a mock function for testing the script"""
    
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
    except:
        return ""
    return ""

def get_next_url(page):
    """This function returns a url and the end point of the url"""

    try:

        start_html_tag = page.find(HTML_TAG_URL)

        # Link in the website not found
        if (start_html_tag == -1):
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

def crawl_web(start_url, max_crawl_pages):
    """This function get all links within a website and crawl each of them"""

    try:
        urls_to_crawl = [start_url]
        urls_crawled = []

        while urls_to_crawl and len(urls_crawled) < max_crawl_pages:
            page_to_crawl = urls_to_crawl.pop()
            
            if (page_to_crawl not in urls_crawled):
                union_lists(urls_to_crawl, get_all_urls(get_page(page_to_crawl)))
                urls_crawled.append(page_to_crawl)

        return urls_crawled
                

    except Exception as e:
        print ( "Error in crawl_web: %s" % str(e) )

# Select a url for a website
# Request
# Handle the response --> result page

print (crawl_web("http://www.udacity.com/cs101x/index.html",1))
print (crawl_web("http://www.udacity.com/cs101x/index.html",3))
print (crawl_web("http://www.udacity.com/cs101x/index.html",500))







