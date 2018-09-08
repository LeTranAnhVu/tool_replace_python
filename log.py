# import os
import json

# seed
data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

# end seed
def updateLog(path,dataDict):
    try:
        with open(path, 'w', encoding="utf-8") as f:
            if dataDict != None:
                dataJson= json.dumps(dataDict)
                f.write(dataJson)
                print("write ok")
    except IOError as e:
        print(e)


def readLog(path):
    content = ""
    contentDict = {}
    contentJson = ""
    try:
        with open(path, 'r', encoding="utf-8") as f:
            contentJson += f.read()
            print(contentDict)
            # decoding json to dictionary
            contentDict = json.loads(contentJson)
            print(contentDict)
    except IOError as e:
        print(e)
# print(isinstance(data,dict))
updateLog("./log.txt",data)
readLog("./log.txt")
