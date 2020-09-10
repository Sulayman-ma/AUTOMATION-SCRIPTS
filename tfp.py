#! python3


"""
TFPDL SERIES UPDATES

Gets you the links to the most recent uploads on tfpdl.com's series page.
Usage: (batch file also available)
    tfp <number of pages to check>
    default gives the first two pages
"""


# Python Imports
import re
import bs4
import requests
import sys



if len(sys.argv) == 2:
    pages = int(sys.argv[1])
else:
    pages = 2

pageNum = 1
while pageNum <= pages:
    titlePattern = re.compile(r'<a href="(.*)(" rel="bookmark.*)')
    currentPage = requests.get("https://www.tfp.is/category/tvseries/page/%s/" %
                               pageNum)
    soap = bs4.BeautifulSoup(currentPage.text, features = 'lxml')

    print("PAGE %s" % pageNum)
    for count in range(1, 9):
        rawTitle = soap.select('#main-content > div.content-wrap > div > '
                              'div.post-listing ' '> article.item-list.item_{} > h2 > '
                              'a'.format(count))

        # Filtering out just the title from the link
        filteredTitle = titlePattern.sub(r'\1', str(rawTitle[0]))
        print(str(count) + ". " + filteredTitle)

    pageNum += 1
    print('\n')

