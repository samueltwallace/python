import storage
from PyInquirer import prompt

def displayCmdInterface():
    s = storage.storageUnit()
    s.addTeXCmds()
    cmds = s.returnCmds()
    questions = [{
                "type":"input",
                "name":cmd,
                "message":"What code do you want for the command " + cmd + "? It takes " + cmds[cmd]['nargs'] + " arguments: "
                } for cmd in cmds.keys()
            ]
    codes = prompt(questions)
    for cmd in codes.keys():
        if codes[cmd]!='':
            s.addTeXCmds(cmd,codes[cmd])
    envs = s.returnEnvs()
    questions = [{
                "type":"input",
                "name":env+"Begin",
                "message":"What code do you want for the begin code of environment  " + env + "?"
                },{
                    "type":"input",
                    "name":env+"End",
                    "message":"What code do you want for the end code of environment " + env + "?"
                    }for env in envs.keys()
            ]
    codes = prompt(questions)
    for env in codes.keys():
        if codes[env]!='':
            s.addEnvCode(env,codes[env][0],codes[env][1])

###################################
##         TODO: CHECK THIS!     ##
###################################


def buildFeedManagerInterface():
    f = feedManger()

