# Select a website
# Start request
# Handle the response

# constants
const_link_search = '<a href='

page = ('<div id="top_bin"> <div id="top_content" class="width960"> <div class="udacity float-left"> <a href="http://udacity.com">Hello world</a>')

# find the position for the first link (<a href=)
start_link = page.find(const_link_search)

# logging
print ('start_link: ', start_link)

start_url = page.find('"', start_link)

# logging
print ('start_url: ', start_url)

end_url = page.find('"', start_url+1)

# logging
print ('end_url: ', end_url)

url = page[start_url+1:end_url]

# logging
print (url)




