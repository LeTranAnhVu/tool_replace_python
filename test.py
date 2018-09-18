def findMatchedIndices(str, offset, pattern):
    itemList = []
    i = str.find(pattern, offset)
    length = len(str)
    patternLen = len(pattern)
    while 0 <= i <= length:
        itemList.append(i)
        i = str.find(pattern, i + patternLen)
    return itemList




str = "Lara had been back and forth along the river path many times in her short life. Her people had not created the path—it had always been there, like the river—but their deerskin-shod feet and the wooden wheels of their handcarts kept the path well worn. tLara’s people were salt traders, and their livelihood took them on a continual journey."

print(findMatchedIndices(str,0,"Lara"))
# [0, 253]

# 267
oStr = "Lara"
nStr = "Pham Thi Thu Trang"
print(len(nStr)- len(oStr))