
from docx import Document
from error_handler import ErrorHandler

DEFAULT_PATH = r'.\sample\ex1.docx'


def open_docx(path):
    return Document(path)

oldStr = r"le tran anh vu"
newStr = r"tran thi ut"
def replace_docx(path, old_str, new_str):
    # open docx
    doc = open_docx(path)
    # check none
    if( not isinstance(old_str,str) or not isinstance(new_str,str)):
        e = "the parameter in replace_docx must not be None"
        return ErrorHandler(path,e)

    # replace the string
    try:
        for i, para in enumerate(doc.paragraphs):
            # para.text = para.text.replace(old_str,new_str)
            inline = para.runs
            for j in range(len(inline)):
                print(">>:", j)
                print(inline[j].text)
                print(inline[j].part)
                print("<<")
            # print(">>:", i)
            # print( para.text)
            # print(para.style.quick_style)
            # print("<<")
            # print("write Ok")
        # doc.save(DEFAULT_PATH)


    except AttributeError as e:
        errorObj = ErrorHandler(path, e)
        errorObj.showError()
        return errorObj


    # save the file


replace_docx(DEFAULT_PATH, oldStr, newStr)
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_element', '_parent', 'base_style', 'builtin', 'delete', 'element', 'font', 'hidden', 'locked', 'name', 'next_paragraph_style', 'paragraph_format', 'part', 'priority', 'quick_style', 'style_id', 'type', 'unhide_when_used']