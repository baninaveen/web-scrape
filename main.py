from bs4 import BeautifulSoup as bfs 
import requests

url = "https://www.flipkart.com/search?q=pixel&marketplace=FLIPKART&otracker=start&as-show=on&as=off"

page_html = requests.get(url)

#page_html.close()
page_soup = bfs(page_html, "html.parser")

container = page_soup.find_all("div", {"class": "_3O0U0u"})
print(container)

