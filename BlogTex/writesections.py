import feedparser
import sqlite3
import sys
import re
from  TeXWriter import *

# Short function to make easy names from urls
def createShortName(urlString):
    return re.match('^[htps]+://w*\.*(\w+)\.com',urlString).group(1)

#open database
data = sqlite3.connect('files/blogs.db')
d = data.cursor()

#Select all urls for blogs
d.execute('SELECT url FROM urls;')
links = d.fetchall()

pages = []
# collect page objects
for link in links:
    pages.append(feedparser.parse(link[0]))

for page in pages:
    currentTeX = open("files/" + createShortName(page.feed.link) + ".tex", "w", encoding="utf-8")
    currentTeX.write(WriteTeX(page,''))
    currentTeX.close()

