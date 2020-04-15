import json
import TeXWriter as TW

class storageUnit:
    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        try:
            self.cmds = json.loads(open('files/rss.cmds','r',encoding='UTF-8').read())
        except:
            self.cmds = {}
        try:
            self.envs = json.loads(open('files/rss.envs','r',encoding='UTF-8').read())
        except:
            self.envs = {}
        self.newStuff = TW.collectCmdsEnvs()
    def addTeXCmds():
        newCmds = self.newStuff[0]
        existingCmdNames = self.cmds.keys()
        newCmdNames = newCmds.keys()
        for cmd in newCmds:
            if cmd not in existingCmdNames:
                self.cmds[cmd] = newCmds[cmd]

    def addCmdCode(cmd,code):
        """TODO: Docstring for addCmd.

        :cmd: TODO
        :returns: TODO

        """
        self.cmds[cmd]['code'] = code

    def writeCmds(self):
        """TODO: Docstring for close.

        :f: TODO
        :returns: TODO

        """
        open('files/rss.cmds','w',encoding='UTF-8').write(json.dumps(self.cmds))

    def addTeXEnvs(self):
        newEnvs = self.newStuff[1]
        existingEnvNames = self.envs.keys()
        newEnvNames = newEnvs.keys()
        for env in newEnvs:
            if env not in existingEnvNames:
                self.envs[env]=newEnvs[env]

    def addEnvCode(self,env,beginCode,endCode):
        self.envs[env]['begincode'] = beginCode
        self.envs[env]['endcode']=endCode

    def writeEnvs(self):
        open('files/rss.envs','w',encoding='UTF-8').write(json.dumps(self.envs))

    def returnCmds(self):
        return self.cmds

    def returnEnvs(self):
        return self.envs
