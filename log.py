# import os
import json

# seed


# data = {
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# }
# data = {
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# }
# data ={
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# }

# end seed
DEFAULT_PATH = './log.txt'


class Log:
    def __init__(self):
        self.logDicts = {
            "input": []
        }


def updateLog(path, dataDict, field):
    # check the path
    if not path:
        path = DEFAULT_PATH
    # get current log
    logDicts = getLog(path)
    # add new log to current
    if (logDicts == None or (not logDicts)):
        logDicts = Log().logDicts

    logDicts[field].insert(0, dataDict)
    # save grand new mass log to txt
    writeLog(path, logDicts)


def writeLog(path, dataDict):
    try:
        with open(path, 'w', encoding="utf-8") as f:
            if dataDict != None:
                # convert dict tp json
                dataJson = json.dumps(dataDict)
                f.write(dataJson)
                print("write ok")
    except IOError as e:
        print("[ERROR]Cannot read this file: ", path, "error description: ", e)
        return None


def getLog(path):
    # check the path
    if not path:
        path = DEFAULT_PATH
    contentJson = ""
    try:
        with open(path, 'r', encoding="utf-8") as f:
            contentJson += f.read()
            # decoding json to dictionary
            if not contentJson:
                logDicts = Log().logDicts
            else:
                logDicts = json.loads(contentJson)
        return logDicts
    except IOError as e:
        print("[ERROR]Cannot read this file: ", path, "error description: ", e)
        return None


def getParticularLog(path, field):
    logDicts = getLog(path)
    # check whether read processing is ok
    if not logDicts:
        # reading fail
        return None

    try:
        return logDicts[field]
    except KeyError as e:
        print('Cannot find the key: ', e)
        return None


def getCurrentLog(path, field):
    try:
        logDict = getParticularLog(path, field)
        return logDict[0]
    except:
        print("Cannot get the currentLog, Please check the key in Log.txt again")
        return None
    # logDict is the array of dictionary

# print(isinstance(data,dict))
# writeLog("./log.txt",data)
# getLog("./log.txt")
# updateLog('./log.txt',data)


# print(getParticularLog(DEFAULT_PATH, 'input'))
# print(getCurrentLog(DEFAULT_PATH, 'input'))
