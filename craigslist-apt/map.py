import json
import requests

key = open('/home/samueltwallace/repos/mapskey.txt','r',encoding='UTF-8').read()

info = json.loads(open('cl.json','r',encoding='UTF-8').read())

MSCS = "851+S+Morgan+St,+Chicago,+IL+60607"
modes = ['walking','bicycling','transit']

for i in range(len(info)):
    home = info[i]
    print("trying entry " +str(i))
    baseUrl = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + MSCS + "&destinations=" 
    mapslink = home["google maps link"]
    try:
        coords = mapslink[0].split('/')[-1]
        baseUrl += coords
        urls = []
        for mode in modes:
            url = baseUrl + '&mode=' + mode + "&key=" + key
            mapsinfo = json.loads(requests.get(url).text)

            try:
                home[mode]=mapsinfo['rows'][0]['elements'][0]['duration']['text']
                print("Successfully pulled info!")
            except:
                home[mode]="Error Pulling Maps Info!"
                print(home[mode])
    except:
        print("Error Pulling Coords")
open('cl.json','w',encoding='UTF-8').write(json.dumps(info,indent=4))
print("done!")


