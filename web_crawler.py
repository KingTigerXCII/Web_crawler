# constants
const_html_tag = '<a href='

def get_next_url(page):

    print (page)

    start_html_tag = page.find(const_html_tag)

    # Link in the website not found
    if (start_html_tag == -1):
        return None, 0

    start_url = page.find('"', start_html_tag)
    print ('start_url: ', start_url)
    end_url = page.find('"', start_url+1)
    print ('end_url: ', end_url)    
    url = page[start_url+1:end_url]

    return url, end_url

def get_all_urls(page):

    while True:       
        url, end_url = get_next_url(page)

        print ('url', url)
        
        if url:
            page = page[end_url:]
        
        else:
            break

# Select a url for a website
# Request
# Handle the response --> result page

page = ('<div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a><div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a><div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a><div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a><div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a>')

get_all_urls(page)








