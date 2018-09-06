from tkinter import *

window = Tk()
window.geometry("500x250")
window.title("Replace Tool")


# event handlers
def btnReplace_Click():
    searchStr = txtSearch.get()
    replaceStr = txtReplace.get()
    print("searchStr: ", searchStr)
    print("replaceStr: ", replaceStr)


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
# txtLog.insert(END,"Just a text Widget\nin two lines\nfjhsdjhfasdf\ndjfhksjhfksd\n")
# layout form
lblPath.grid(row=0, column=0, sticky='w')
lblSearch.grid(row=1, column=0, sticky='w')
lblReplace.grid(row=2, column=0, sticky='w')
lblLog.grid(row=4,column=0, sticky='w')
txtPath.grid(row=0, column=1, sticky='w')
txtSearch.grid(row=1, column=1, sticky='w')
txtReplace.grid(row=2, column=1, sticky='w')
txtLog.grid(row=5, column=1, columnspan=2, sticky='w')
btnReplace.grid(row=3, column=1, sticky='w')

window.mainloop()

# class MainForm:
#     count = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         MainForm.count += 1
#
#
# form1 = MainForm("le tran anh vu", 23)
# form2 = MainForm(None,None)
#
# print(form1.name, form1.age)
# print(MainForm.__bases__)
