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


def updateLog(path, dataDict, field):
    # check the path
    if not path:
        path = DEFAULT_PATH
    # get current log
    currentDicts = getLog(path, field)
    print('hello: ', currentDicts)
    # add new log to current
    if (currentDicts == None or (not currentDicts)):
        currentDicts = {}
        currentDict['input'] = []

    currentDict['input'].insert(0, dataDict)
    # save grand new mass log to txt
    writeLog(path, currentDict)

    # # test
    # for log in getLog(DEFAULT_PATH)['input']:
    #     print('log')
    #     print(log)


def writeLog(path, dataDict):
    try:
        with open(path, 'w', encoding="utf-8") as f:
            if dataDict != None:
                dataJson = json.dumps(dataDict)
                f.write(dataJson + "\n")
                print("write ok")
    except IOError as e:
        print(e)


def getLog(path):
    # check the path
    if not path:
        path = DEFAULT_PATH
    content = ""
    logDict = {}
    contentJson = ""
    try:
        with open(path, 'r', encoding="utf-8") as f:
            contentJson += f.read()
            print('logDict', type(logDict))
            # decoding json to dictionary
            logDict = json.loads(contentJson)
            return logDict
    except IOError as e:
        return e


def getCurrentLog()

# print(isinstance(data,dict))
# writeLog("./log.txt",data)
# getLog("./log.txt")
# updateLog('./log.txt',data)
