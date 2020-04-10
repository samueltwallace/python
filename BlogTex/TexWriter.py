import re
import feedparser

def cleanStr(string):
    return re.sub('\s|_','',string)

def WriteTeX(page,prefix):
    bigString = ''
    for key in page.keys():
        if type(page[key]) == str:
            bigString += '\\xml' + prefix +  cleanStr(key) + '{' + page[key] + '}'
        if type(page[key]) == feedparser.FeedParserDict:
            bigString += '\n\\begin{xml' + prefix + cleanStr(key) + '}\n'
            bigString += WriteTeX(page[key],cleanStr(key))
            bigString += '\n\\end{xml' + prefix + cleanStr(key) + '}\n'
        if type(page[key]) == list:
            bigString += '\n\\begin{xml' + prefix + cleanStr(key) + '}\n'
            for elements in page[key]:
                bigString += WriteTeX(elements,cleanStr(key))
            bigString += '\n\\end{xml' + prefix + cleanStr(key) + '}\n'
    return bigString
