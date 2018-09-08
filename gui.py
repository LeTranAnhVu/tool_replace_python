from tkinter import *
from app import walkthrough

window = Tk()
window.geometry("400x250")
window.title("Replace Tool")


def overwriteLog(logObj, content):
    # clear the log
    txtLog.delete(1.0, END)
    # insert new content to log
    txtLog.insert(END, str(content) + '\n')


def nonOverwriteLog(logObj, content):
    # insert new content to log right behind the previous content
    txtLog.insert(END, str(content) + '\n')


class inputLog:
    def __init__(self, path, searchStr, replaceStr):
        self.path = path
        self.searchStr = searchStr
        self.replaceStr = replaceStr
        self.dictFactory()
    def dictFactory(self):
        print(self)
        # make the properties to dict witht he typical key


# event handlers
def btnReplace_Click():
    overwriteLog(txtLog, "processing . . .")
    searchStr = txtSearch.get()
    replaceStr = txtReplace.get()
    print("searchStr: ", searchStr)
    print("replaceStr: ", replaceStr)

    rootPath = txtPath.get()
    searchStr = txtSearch.get()
    replaceStr = txtReplace.get()
    walkthrough(rootPath, searchStr, replaceStr)
    nonOverwriteLog(txtLog, "finished!")


# create form
lblPath = Label(window, text="Add Path")
lblSearch = Label(window, text="Search for")
lblReplace = Label(window, text="Replaced by")
lblLog = Label(window, text="Log:")
txtPath = Entry(window, width=30)
txtSearch = Entry(window, width=30)
txtReplace = Entry(window, width=30)
txtLog = Text(window, width=35, height=6)
btnReplace = Button(window, text="Replace", command=btnReplace_Click)

## layout form

# path element
lblPath.grid(row=0, column=0, sticky='w')
txtPath.grid(row=0, column=1, sticky='w')

# search form
lblSearch.grid(row=1, column=0, sticky='w')
txtSearch.grid(row=1, column=1, sticky='w')

# replace form
lblReplace.grid(row=2, column=0, sticky='w')
txtReplace.grid(row=2, column=1, sticky='w')

# log
lblLog.grid(row=4, column=0, sticky='w')
txtLog.grid(row=5, column=1, columnspan=2, sticky='w')

# button
btnReplace.grid(row=3, column=1, sticky='w')

window.mainloop()
