import re
import feedparser
from html.parser import HTMLParser

class parser(HTMLParser):
    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self)
        self.output = ''

    def handle_starttag(self,tag, attrs):
        string = '\\' + tag
        for attr in attrs:
            string += '{' + attr[1] + '}'
        string += '{'
        self.output += string
    def handle_endtag(self,tag):
        self.output +=  '}'
    def handle_data(self,data):
        self.output +=  data
    def parsed(self):
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
