import feedparser
import json
from  TeXWriter import *
import storage

def makeSections():
    f = storage.feedManager()
    links = f.returnFeeds()
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
    cmds = collectCmdsEnvs()
    for cmd in cmds[0].keys():
        if cmds[cmd]['nargs'] != 0:
            f.write('\n\\newcommand{\\'+cmd+'}[' + cmds[0][cmd]['nargs'] + ']{'+ cmds[cmd]['code'] + '}')
        else:
            f.write('\n\\newcommand{\\'+cmd+'}{'+ cmds[0][cmd]['code'] + '}')

    for env in cmds[1].keys():
        f.write('\n\\newenvironment{\\'+cmds[1][env]+'}' + '{' + cmds[1][env]['begincode'] + '}' + '{' + cmds[1][env]['endcode'] + '}')

    f.close()
