import json
import TeXWriter as TW

class storageUnit:
    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        try:
            self.cmds = json.loads(open('files/cmds.json','r',encoding='UTF-8').read())
        except:
            self.cmds = {}
        try:
            self.envs = json.loads(open('files/envs.json','r',encoding='UTF-8').read())
        except:
            self.envs = {}
        self.newCmdsEnvs = TW.collectCmdsEnvs()
    def addTeXCmds(self):
        newCmds = self.newCmdsEnvs[0]
        existingCmdNames = self.cmds.keys()
        newCmdNames = newCmds.keys()
        for cmd in newCmds:
            if cmd not in existingCmdNames:
                self.cmds[cmd] = newCmds[cmd]

    def addCmdCode(self,cmd,code):
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
        open('files/cmds.json','w',encoding='UTF-8').write(json.dumps(self.cmds))

    def addTeXEnvs(self):
        newEnvs = self.newCmdsEnvs[1]
        existingEnvNames = self.envs.keys()
        newEnvNames = newEnvs.keys()
        for env in newEnvs:
            if env not in existingEnvNames:
                self.envs[env]=newEnvs[env]

    def addEnvCode(self,env,beginCode,endCode):
        self.envs[env]['begincode'] = beginCode
        self.envs[env]['endcode']=endCode

    def writeEnvs(self):
        open('files/envs.json','w',encoding='UTF-8').write(json.dumps(self.envs))

    def returnCmds(self):
        return self.cmds

    def returnEnvs(self):
        return self.envs

class feedManager:
    def __init__(self):
        try:
            self.feeds = json.loads(open('files/blogs.json','r',encoding='UTF-8').read())
        except:
            self.feeds = {}

    def addFeed(self, name,link):
        """TODO: Docstring for addFeed.

        :name: TODO
        :link: TODO
        :returns: TODO

        """
        self.feeds[name]=link

    def removeFeed(self, name):
        """TODO: Docstring for removeFeed.

        :name: TODO
        :returns: TODO

        """
        del(self.feeds[name])

    def returnFeeds(self):
        """TODO: Docstring for returnFeeds.
        :returns: TODO

        """
        return self.feeds

    def writeFeeds(self):
        """TODO: Docstring for writeFeeds.
        :returns: TODO

        """
        open('files/blogs.json','w',encoding='UTF-8').write(json.dumps(self.feeds))
