import cl
import json

links = cl.collectEntries()
info = []
numlinks = len(links)
for i in range(numlinks):
    print("Searching url " + str(i) + " of " +str(numlinks))
    info.append(cl.collectInfo(links[i]))
print("Writing info to JSON...")
open('cl.json','w',encoding='UTF-8').write(json.dumps(info,indent=4))
print("Done!")
