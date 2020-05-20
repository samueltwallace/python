import requests
from lxml import html
import json

def collectInfo(entryUrl):
    fields = [{"tag":"a", "attr":"target","val":"_blank","target":"/@href", "name":"google maps link"},
            {"tag":"p","attr":"class", "val":"attrgroup","target":"//*/text()", "name":"basic info"}]
    info = {'url':entryUrl}
    page = requests.get(entryUrl)
    pageTree = html.fromstring(page.content)
    for field in fields:
        entryInfo = pageTree.xpath('//' + field["tag"] + '[@' + field["attr"] + '="' + field['val'] + '"]'+field['target'])
        info[field["name"]] = entryInfo
    return info

def findUrls(url):
    pageTree = html.fromstring(requests.get(url).content)
    return pageTree.xpath('//a[@class="result-title hdrlnk"]/@href')

def collectEntries():
    infoList = []
    url = "https://chicago.craigslist.org/search/apa"

    urls = []
    print("Collecting URLs from Craigslist search...")
    urls += findUrls(url)
    for i in range(1,25):
       urls += findUrls(url + "?s=" + str(120*i)) 
    print("Done!")
    return urls
