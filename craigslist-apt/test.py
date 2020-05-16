import cl
import json

links = cl.collectEntries()
info = [cl.collectInfo(link) for link in links]
open('cl.json','w',encoding='UTF-8').write(json.dumps(info))
