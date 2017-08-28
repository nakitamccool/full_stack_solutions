#!/usr/bin/env python

import os
from bs4 import BeautifulSoup  # BeautifulSoup4 package
import urllib.request

# Grab the HTML from a web page just like we did
# in the first example
my_address = "http://www.irishtimes.com/"

# Open my_address, read page and decode from bytes to text
with urllib.request.urlopen(my_address) as html_page:
    html_text = html_page.read().decode("utf-8")

# Pass the HTML to the BeautifulSoup constructor.
# The second argument tells beautiful soup which parser to use
soup = BeautifulSoup(html_text, "html.parser")

# Store the images in a list
images = soup.find_all("img")

# Iterate over 'images' list and
# print the 'src' of each image
for img in images:
    print(img['src'])
