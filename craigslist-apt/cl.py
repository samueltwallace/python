import feedparser as fp
import requests
from lxml import html
import json


def collectInfo():
    infoList = []
    url = "https://chicago.craigslist.org/search/apa?format=rss"
    fields = ["mapaddress", "shared-line-bubble", "attrgroup"]

    listings = fp.parse(url).entries

    for entry in listings:
        info = {}
        info['title'] = entry.title
        page = requests.get(entry.link)
        pageTree = html.fromstring(page.content)
        for field in fields:
            info[field]= pageTree.xpath('//*[@class="' + field + '"]//*/text()')
        infoList.append(info)
    return infoList

