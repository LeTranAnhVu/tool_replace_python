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

def updateLog(path,dataDict):
    # get current log
    currentDict = getLog(path)
    # add new log to current
    if(currentDict == None or (not currentDict)):
        currentDict = {}
        currentDict['his'] = []

    currentDict['his'].insert(0,dataDict)
    # save grand new mass log to txt
    writeLog(path,currentDict)


def writeLog(path,dataDict):
    try:
        with open(path, 'w', encoding="utf-8") as f:
            if dataDict != None:
                dataJson= json.dumps(dataDict)
                f.write(dataJson + "\n")
                print("write ok")
    except IOError as e:
        print(e)


def getLog(path):
    content = ""
    contentDict = {}
    contentJson = ""
    try:
        with open(path, 'r', encoding="utf-8") as f:
            contentJson += f.read()
            print('contentDict', type(contentDict))
            # decoding json to dictionary
            contentDict = json.loads(contentJson)
            print(contentDict)
            return contentDict
    except IOError as e:
        print(e)
# print(isinstance(data,dict))
# writeLog("./log.txt",data)
# getLog("./log.txt")
# updateLog('./log.txt',data)
for log in getLog("./log.txt")['his']:
    print('log')
    print(log)