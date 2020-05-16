import requests
from lxml import html
import json

def collectInfo(entryUrl):
    fields = ["mapaddress", "shared-line-bubble", "attrgroup"]
    info = {'url':entryUrl}
    page = requests.get(entryUrl)
    pageTree = html.fromstring(page.content)
    for field in fields:
        info[field]= pageTree.xpath('//*[@class="' + field + '"]//*/text()')
    return info

def findUrls(url):
    pageTree = html.fromstring(requests.get(url).content)
    return pageTree.xpath('//a[@class="result-title hdrlnk"]/@href')

def collectEntries():
    infoList = []
    url = "https://chicago.craigslist.org/search/apa"

    urls = []
    urls += findUrls(url)
    for i in range(1,25):
       urls += findUrls(url + "?s=" + str(120*i)) 
    return urls
