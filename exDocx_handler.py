from docx import Document
from error_handler import ErrorHandler

DEFAULT_PATH = r'.\sample\ex1.docx'


class MatchedRunObj:
    def __init__(self, paragraph, matchedIndex, oldStr, newStr):
        self.p = paragraph
        self.matchedIndex = matchedIndex
        self.oldStr = oldStr
        self.newStr = newStr
        self.listOfIndexOfRun = []
        # indexOfFirstMatchedChar is the position of the first character-in oldStr in the first Run obj in Run Objlist
        self.indexOfFirstMatchedChar = None

        # indexOfLastMatchedChar is the position of the last character-in oldStr in the last Run obj in Run Objlist
        self.indexOfLastMatchedChar = None

    def findRelatedRunIndex(self):
        # do something to ...
        return self.listOfIndexOfRun

    def findFirstCharMatchedIndex(self):
        # do something to ...
        return self.indexOfFirstMatchedChar

    def findLastCharMatchedIndex(self):
        # do something to ...
        return self.indexOfLastMatchedChar

    def replaceString(self):
        # do something to ...
        return True


def findMatchedIndices(str, offset, pattern):
    itemList = []
    i = str.find(pattern, offset)
    length = len(str)
    patternLen = len(pattern)
    while 0 <= i <= length:
        itemList.append(i)
        i = str.find(pattern, i + patternLen)
    return itemList


def open_docx(path):
    return Document(path)


def replace_docx(path, old_str, new_str):
    doc = open_docx(path)
    # check none
    if not isinstance(old_str, str) or not isinstance(new_str, str):
        e = "the parameter in replace_docx must not be None"
        return ErrorHandler(path, e)
    # replace the string
    try:
        for i, para in enumerate(doc.paragraphs):
            # each para call  matchIndexs
            if old_str in para.text:
                matchedIndices = findMatchedIndices(para.text, 0, old_str)
                for matchIndex in matchedIndices:
                    # make the instance of matchedRunObj
                    matchedObj = MatchedRunObj(para, matchIndex, old_str, new_str)
                    matchedObj.findRelatedRunIndex()
                    matchedObj.findFirstCharMatchedIndex()
                    matchedObj.findLastCharMatchedIndex()
                    matchedObj.replaceString()
        # save file in here
    except AttributeError as e:
        errorObj = ErrorHandler(path, e)
        errorObj.showError()
        return errorObj
