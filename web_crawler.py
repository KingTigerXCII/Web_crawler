# constants
const_html_tag = '<a href='

def get_next_url(page):
    """This function returns a url and the end point of the url"""

    try:

        start_html_tag = page.find(const_html_tag)

        # Link in the website not found
        if (start_html_tag == -1):
            return None, 0

        start_url = page.find('"', start_html_tag)
        end_url = page.find('"', start_url+1)   
        url = page[start_url+1:end_url]

        return url, end_url

    except:
        print ("Function get_next_url raises an error.")


def get_all_urls(page):
    """This function returns all urls of the website"""

    try:
        while True:       
            url, end_url = get_next_url(page)
            
            if url:
                print ("url: ", url) 
                page = page[end_url:]
            
            else:
                break
    except:
        print ("Function get_all_urls raises an error.")

# Select a url for a website
# Request
# Handle the response --> result page

page = ('<div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a><div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a><div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a><div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a><div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a>')

get_all_urls(page)







