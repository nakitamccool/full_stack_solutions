#!/usr/bin/env python

import os
from bs4 import BeautifulSoup  # BeautifulSoup4 package
import urllib.request

# Grab the HTML from a web page just like we did
# in the first example
my_address = "https://docs.python.org/3.4/whatsnew/3.4.html"

# Open my_address, read page and decode from bytes to text
with urllib.request.urlopen(my_address) as html_page:
    html_text = html_page.read().decode("utf-8")

# Pass the HTML to the BeautifulSoup constructor.
# The second argument tells beautiful soup which parser to use
soup = BeautifulSoup(html_text, "lxml")

result = soup.get_text()
text = os.linesep.join([s for s in result.splitlines() if s])
print(text)
