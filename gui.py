from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("Replace Tool")


# event handlers
def btnReplace_Click():
    searchStr = txtSearch.get()
    replaceStr = txtReplace.get()
    print("searchStr: ", searchStr)
    print("replaceStr: ", replaceStr)


# create form
lblSearch = Label(window, text="Search for")
lblReplace = Label(window, text="Replaced by")
txtSearch = Entry(window, width=30)
txtReplace = Entry(window, width=30)

# layout form
lblSearch.grid(row=0, column=0, sticky='w')
lblReplace.grid(row=1, column=0, sticky='w')
txtSearch.grid(row=0, column=1)
txtReplace.grid(row=1, column=1)

btnReplace = Button(window, text="Replace", command=btnReplace_Click).grid(row=2, column=1)

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
