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
        self.inTag = False
        self.reg1 = re.compile(r'\%')
        self.reg2 = re.compile(r'\$')

    def escape(self,string):
        string = self.reg1.sub(r'\%',string)
        string = self.reg2.sub(r'\\$', string)
        return string

    def handle_starttag(self,tag, attrs):
        tag = self.escape(tag)
        string = '\\' + tag
        self.tags.append(tag)
        for attr in attrs:
            string += '{' + self.escape(attr[1]) + '}'
        self.output += string
        self.inTag = True
    def handle_endtag(self,tag):
        self.inTag = False
    def handle_data(self,data):
        data = self.escape(data)
        if self.inTag:
            self.output +=  '{' + data + '}'
        else:
            self.output += data
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
            p = parser()
            p.feed(page[key])
            bigString += '\\xml' + prefix +  cleanKey(key) + '{' + p.parsed() + '}'
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
    cmdnames = [cmd[0] for cmd in cmds]
    cmdnames = list(set(cmdnames))
    nargs = {"" : ""}
    for cmdname in cmdnames:
        for cmd in cmds:
            if cmdname == cmd[0]:
                nargs[cmdname] = int(len(cmd) - 1)


    for cmd in nargs.keys():
        if cmd == 'begin':
            pass
        elif cmd == 'end':
            pass
        else:
            finalString += '\\newcommand{\\' + cmd + '}[' + str(nargs[cmd]) + ']{\\ignorespaces}\n\n'

    envs = re.findall(r'\\begin\{(?P<env>\w+)\}',wholeTeX)
    envs = list(set(envs))
    for env in envs:
        finalString += '\\newenvironment{' + env  +'}{}{}\n\n'
    return finalString
