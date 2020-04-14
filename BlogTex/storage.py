import shelve
import TeXWriter

def storeTeXCmds():
    cmdDb = shelve.open('files/rss.cmds')
    cmds = TeXWriter.writePackage()
    cmdDb['cmds'] = cmds[0]
    cmdDb['envs'] = cmds[1]
    cmdDb.close()

def readTeXCmds():
    """TODO: Docstring for readTeXCmds.
    :returns: TODO

    """
    cmdDb = shelve.open('files/rss.cmds')
    cmds = cmdDb['cmds']
    envs = cmdsDb['envs']
    cmdDb.close()
    return (cmds,envs)

def addCmd(cmd):
    """TODO: Docstring for addCmd.

    :cmd: TODO
    :returns: TODO

    """
    
