import storage

def buildCmdInterface():
    s = storage.storageUnit()
    s.addTeXCmds()
    cmds = json.loads(open('files/rss.cmds','r',encoding='UTF-8').read())
    questions = [{
                "type":"input",
                "name":cmd,
                "message":"What code do you want for the command " + cmd + "? It takes " + cmds[cmd]['nargs'] + " arguments: "
                } for cmd in cmds.keys()
            ]
       return questions 


def buildFeedManagerInterface():
