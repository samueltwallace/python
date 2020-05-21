import re
import json

aptinfo = json.loads(open('cl.json','r',encoding='UTF-8').read())
csvfile = open('cl.csv','w',encoding='UTF-8')

firstKeys = aptinfo[0].keys()
headers = ""
for key in firstKeys:
    headers += key + "# "
headers = headers[:-1] + '\n'
csvfile.write(headers)

for info in aptinfo:
    if info.keys() != firstKeys:
        #i = aptinfo.index(info)
        #raise Exception("Inconsistent column headers on entry " + str(i) + ". Entry: " + str(info))
        pass
    else:
        row = ""
        for key in firstKeys:
            if type(info[key]) == list:
                string = " ".join(info[key])
            else:
                string = info[key]
            string = re.sub('\\n'," ",string)
            row += string + "# "
        row = row[:-1] + '\n'
        csvfile.write(row)
csvfile.close()


