import storage
from PyInquirer import prompt

def displayCmdInterface():
    s = storage.storageUnit()
    s.addTeXCmds()
    cmds = s.returnCmds()
    questions = [{
                "type":"input",
                "name":cmd,
                "message":"What code do you want for the command " + cmd + "? It takes " + str(cmds[cmd]['nargs']) + " arguments (leave blank for no action): "
                } for cmd in cmds.keys()
            ]
    codes = prompt(questions)
    for cmd in codes.keys():
        if codes[cmd]!='':
            s.addCmdCode(cmd,codes[cmd])
    envs = s.returnEnvs()
    s.addTeXEnvs()
    questions = []
    for env in envs.keys():
        questions.append({'type':'input','name':env + 'BeginCode','message':'What code do you want for the begin code of the environment ' + env + '? '})
        questions.append({'type':'input', 'name': env + 'EndCode','message':'What code do you want for the end code of the environment ' + env + '? '})
    codes = prompt(questions)
    for env in codes.keys():
        if codes[env]!='':
            s.addEnvCode(env,codes[env]['beginCode'],codes[env]['endCode'])

    s.writeCmds()
    s.writeEnvs()

###################################
##         TODO: CHECK THIS!     ##
###################################


def feedManagerInterface():
    f = storage.feedManager()
    adding = prompt([{"type": 'confirm', 'name':'adding','message':'Would you like to add a blog feed? '}])['adding']
    while adding:
        newFeed = prompt([{'type':'input','name':'feedName','message':'What is the name of the feed? '},{'type':'input','name':'feedLink','message': 'What\'s the link to the RSS feed for this blog?'}])
        f.addFeed(newFeed['feedName'],newFeed['feedLink'])
        adding = prompt([{"type": 'confirm', 'name':'adding','message':'Would you like to add another feed? '}])['adding']

    removeing = prompt([{"type": 'confirm', 'name':'removeing','message':'Would you like to remove a blog feed? '}])['removeing']
    while removeing:
        newFeed = prompt([{'type':'input','name':'feedName','message':'What is the name of the feed? '}])
        f.removeFeed(newFeed['feedName'])
        removeing = prompt([{"type": 'confirm', 'name':'removeing','message':'Would you like to remove another feed? '}])['removeing']

    f.writeFeeds()



