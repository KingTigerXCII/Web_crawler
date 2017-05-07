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
    """This function returns a url and the end point of the url in the"""
    """html structure"""

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
    """This function unions two lists"""
    
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
    """This function gets a url as parameter and searches for urls in a"""
    """given depth"""

    try:
        urls_to_crawl = [start_url]
        urls_crawled = []
        urls_next_depth = []
        depth = 0
        index = {}
        graph = {}

        while urls_to_crawl and depth <= max_crawl_depth:
            page_to_crawl = urls_to_crawl.pop()
            
            if page_to_crawl not in urls_crawled:
                content_page = get_page(page_to_crawl)
                add_page_to_index(index, page_to_crawl, content_page)
                outlinks = get_all_urls(content_page)
                graph[page_to_crawl] = outlinks
                union_lists(urls_next_depth, outlinks)
                urls_crawled.append(page_to_crawl)

            if not urls_to_crawl:
                urls_to_crawl = urls_next_depth
                urls_next_depth = []
                depth = depth + 1

        return index, graph
                

    except Exception as e:
        print ( "Error in crawl_web: %s" % str(e) )

def add_to_index(index, keyword, url):
    """This function build the index of the searchengine"""

    try:
        if keyword in index:
            index[keyword].append(url)
        else:
            index[keyword] = [url]

    except Exception as e:
        print ( "Error in add_to_index: %s" % str(e) )

def index_lookup(index, keyword):
    """This function looks for the keyword in the index and return the"""
    """entry or a empty list"""

    try:
        if keyword in index:
            return index[keyword]
        else:
            return None

    except Exception as e:
        print ( "Error in lookup: %s" % str(e) )

def add_page_to_index(index, url, content):

    try:
        keywords = content.split()
        for keyword in keywords:
            add_to_index(index, keyword, url)

    except Exception as e:
        print ( "Error in add_page_to_index: %s" % str(e) )

def compute_ranks(graph):
    """Rank the pages by incoming links of popular pages. If the side which """
    """invoke the page is high popular, it will get a good rank"""
    try:
        d = 0.8 # damping factor
        numloops = 10
        ranks = {}
        npages = len(graph)
        
        for page in graph:
            ranks[page] = 1.0 / npages
            
        for i in range(0, numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d) / npages
                for node in graph:
                    if page in graph[node]:
                        newrank = newrank + d *(ranks[node] / len(graph[node]))
                newranks[page] = newrank			    
            ranks = newranks
                                                
        return ranks
                                                
    except Exception as e:
        print ( "Error in compute_ranks: %s" % str(e) )
                                                
#def record_user_click(index, keyword, url):
#    """This function increases the count of website clicks for a specific keyword"""
#
#    try:       
#        result_of_urls = index_lookup(index, keyword)
#        if result_of_urls:
#            for entry in result_of_urls:
#                if entry[0] == url:
#                    entry[1] = entry[1]+1
#                        
#    except Exception as e:
#        print ( "Error in record_user_click: %s" % str(e) )

index = []

index, graph = crawl_web('https://www.udacity.com/cs101x/urank/index.html', 10)
print (index_lookup(index, 'Hummus'))
print ('---------------------------')
print (graph)
ranks = compute_ranks(graph)
print (ranks)






