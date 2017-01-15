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
        elif url == "http://top.contributors/velak.html":
            return ('<a href="http://top.contributors/jesyspa.html">'
        '<a href="http://top.contributors/forbiddenvoid.html">')
        elif url == "http://top.contributors/jesyspa.html":
            return  ('<a href="http://top.contributors/elssar.html">'
        '<a href="http://top.contributors/kilaws.html">')
        elif url == "http://top.contributors/forbiddenvoid.html":
            return ('<a href="http://top.contributors/charlzz.html">'
        '<a href="http://top.contributors/johang.html">'
        '<a href="http://top.contributors/graemeblake.html">')
        elif url == "http://top.contributors/kilaws.html":
            return ('<a href="http://top.contributors/tomvandenbosch.html">'
        '<a href="http://top.contributors/mathprof.html">')
        elif url == "http://top.contributors/graemeblake.html":
            return ('<a href="http://top.contributors/dreyescat.html">'
        '<a href="http://top.contributors/angel.html">')
        elif url == "A1":
            return  '<a href="B1"> <a href="C1">  '
        elif url == "B1":
            return  '<a href="E1">'
        elif url == "C1":
            return '<a href="D1">'
        elif url == "D1":
            return '<a href="E1"> '
        elif url == "E1":
            return '<a href="F1"> '
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
            if (element not in list1):
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
            
            if (page_to_crawl not in urls_crawled):
                content_page = get_page(page_to_crawl)
                add_page_to_index(index, page_to_crawl, content_page)
                union_lists(urls_next_depth, get_all_urls(content))
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
            if (keyword == entry[0]):
                if (url not in entry[1]):
                    entry[1].append(url)
                    return
                
        index.append([keyword,[url]])

    except Exception as e:
        print ( "Error in add_to_index: %s" % str(e) )

def index_lookup(index, keyword):
    """This function looks for the keyword in the index and return the entry or a empty list"""

    try:

        for entry in index:
            if (keyword == entry[0]):
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





