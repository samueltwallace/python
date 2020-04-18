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
    m = storage.storageUnit()
    cmds = m.returnCmds()
    envs = m.returnEnvs()
    for cmd in cmds.keys():
        if cmds[cmd]['code']=='':
            cmds[cmds]['code'] = '\\ignorespaces'
        if cmds[cmd]['nargs'] != 0:
            f.write('\n\\newcommand{\\'+cmd+'}[' + str(cmds[cmd]['nargs']) + ']{'+ cmds[cmd]['code'] + '}')
        else:
            f.write('\n\\newcommand{\\'+cmd+'}{'+ str(cmds[cmd]['code']) + '}')

    for env in envs.keys():
        f.write('\n\\newenvironment{'+env+'}' + '{' + envs[env]['beginCode'] + '}' + '{' + envs[env]['endCode'] + '}')

    f.close()
