import requests
from lxml import html
import shutil

url = "http://markmolnar.com/project-dune/"

page = requests.get(url)

page = html.fromstring(page.content)

pics = page.xpath('//img[@src]/@src')


for picurl in pics:
    pic = requests.get(picurl, stream=True)
    path = '/home/samueltwallace/Pictures/Wallpapers/'+ picurl.split('/')[-1]
    if pic.status_code == 200:
        pic.raw.decode_content = True
        with open(path, 'wb') as picfile:
            shutil.copyfileobj(pic.raw,picfile)
