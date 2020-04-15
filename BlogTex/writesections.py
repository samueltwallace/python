import feedparser
import json
from  TeXWriter import *

def makeSections():
    links = json.loads(open('files/rss.blogs','r',encoding='UTF-8').read())
    pages = []

    # TODO: Rewrite this function
    # collect page objects
    for link in links.keys():
        pages.append(feedparser.parse(links[link]))


    for page in pages:
        currentTeX = open("files/" + createShortName(page.feed.link) + ".sectex", "w", encoding="utf-8")
        currentTeX.write(WriteTeX(page,''))
        currentTeX.close()

def makePackage():
    f = open('files/xml.sty','w',encoding='UTF-8')
    f.write('\\NeedsTeXFormat{LaTeX2e}\n\\ProvidesPackage{xml}\n\n\\ProcessOptions\\relax')
    f.write(writePackage())
    f.close()
