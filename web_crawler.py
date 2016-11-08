# constants
const_html_tag = '<a href='

def get_next_url(page):

    start_html_tag = page.find(const_html_tag)

    start_url = page.find('"', start_html_tag)

    end_url = page.find('"', start_url+1)

    url = page[start_url+1:end_url]

    return url, end_url

# Select a url for a website
# Request
# Handle the response --> result page

page = ('<div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a>')

url, end_url = get_next_url(page)

# logging
print (url)
print (end_url)

page = page[end_url:]






