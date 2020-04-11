import re
import feedparser
from html.parser import HTMLParser
from pathlib import Path

class parser(HTMLParser):
    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self)
        self.output = ''
        self.headerFile = open('files/xml.sty','a',encoding='UTF-8')
        self.tags = []

    def handle_starttag(self,tag, attrs):
        string = '\\' + tag
        self.tags.append(tag)
        for attr in attrs:
            string += '{' + attr[1] + '}'
        string += '{'
        self.output += string
    def handle_endtag(self,tag):
        self.output +=  '}'
    def handle_data(self,data):
        self.output +=  data
    def parsed(self):
        for tag in self.tags:
            self.headerFile.write('\\newcommand{\\' + tag + '}{}\n')
        return self.output

def cleanKey(string):
    return re.sub('\s|_','',string)

def WriteTeX(page,prefix):
    bigString = ''
    for key in page.keys():
        if type(page[key]) == str:
            bigString += '\\xml' + prefix +  cleanKey(key) + '{' + page[key] + '}'
        if type(page[key]) == feedparser.FeedParserDict:
            bigString += '\n\\begin{xml' + prefix + cleanKey(key) + '}\n'
            bigString += WriteTeX(page[key],cleanKey(key))
            bigString += '\n\\end{xml' + prefix + cleanKey(key) + '}\n'
        if type(page[key]) == list:
            bigString += '\n\\begin{xml' + prefix + cleanKey(key) + '}\n'
            for elements in page[key]:
                bigString += WriteTeX(elements,cleanKey(key))
            bigString += '\n\\end{xml' + prefix + cleanKey(key) + '}\n'
    return bigString

def writePackage():
    finalString = ''
    wholeTeX = ''
    for TeXFile in list(Path('./files/').glob('**/*.tex')):
        wholeTeX += open(str(TeXFile),'r',encoding='UTF-8').read()
    cmds = re.findall('\\\\(?P<cmd>\w+)(\{.*?\})+',wholeTeX)
    cmds = list(dict.fromkeys(cmds))
    nargs = []
    for cmd in cmds:
        nargs.append(len(cmd) - 1)
    for i in range(len(cmds)):
        finalString += '\\newcommand{\\' + cmds[i][0] + '}[' + str(nargs[i]) + ']{}\n\n'
    return finalString
