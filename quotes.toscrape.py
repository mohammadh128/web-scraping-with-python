# import libraries

import requests
import bs4

page_still_valid = True
authors = set()
page = 1

page_still_valid = True
authors = set()
page = 1
url = 'http://quotes.toscrape.com/page/'

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url+str(page)

    # Obtain Request
    res = requests.get(page_url)

    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break

    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

    # Go to Next Page
    page += 1

print(authors)
