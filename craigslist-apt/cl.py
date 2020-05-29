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


def collectall():
        links = cl.collectEntries()
        info = []
        numlinks = len(links)
        for i in range(numlinks):
        print("Searching url " + str(i) + " of " +str(numlinks))
        info.append(cl.collectInfo(links[i]))
        print("Writing info to JSON...")
        open('cl.json','w',encoding='UTF-8').write(json.dumps(info,indent=4))
        print("Done!")
