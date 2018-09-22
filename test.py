import zipfile

# import xml.etree.ElementTree as ET
CURRENT_PATH = r"./sample/ex11.docx"
ROOT_PATH = r"./sample/"


def readHeader(path):
    with zipfile.ZipFile(path) as doc:
        for xml in doc.filelist:
            if "header" in xml.filename:
                header = doc.read(xml).decode()
                print('>>')
                print(xml)
                print('<<')
                # doc.extract(xml.filename, path=ROOT_PATH, pwd=None)
                return header


def xmlfile(path):
    with zipfile.ZipFile(path) as doc:
        print('>>', doc.filelist)
        for xml in doc.filelist:
            print('>>')
            print(xml.filename)


def writeHeader(path, newHeader):
    with zipfile.ZipFile(path, mode='a') as doc:
        for xml in doc.filelist:
            # print("ten")
            if "header" in xml.filename:
                doc.writestr("./sample/" + xml.filename, newHeader)
                print(">>>>>")
                # print(readHeader(path))


# doc.writestr("./sample/"+xml.filename,header)
# ['NameToInfo', '_RealGetContents', '__class__', '__del__', '__delattr__',
#  '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__',
#  '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
#  '_allowZip64', '_comment', '_didModify', '_extract_member', '_filePassed', '_fileRefCnt',
#  '_fpclose', '_lock', '_open_to_write', '_sanitize_windows_name', '_seekable',
#  '_windows_illegal_name_trans_table', '_write_end_record', '_writecheck', '_writing', 'close',
#  'comment', 'compression', 'compresslevel', 'debug', 'extract', 'extractall', 'filelist', 'filename',
#  'fp', 'getinfo', 'infolist', 'mode', 'namelist', 'open', 'printdir', 'pwd', 'read', 'setpassword',
#  'start_dir', 'testzip', 'write', 'writestr']


#
# header = readHeader(CURRENT_PATH)
# writeHeader(CURRENT_PATH,header)
# xmlfile(CURRENT_PATH)


# tree = ET.parse(ROOT_PATH+'word/header1.xml')
# root = tree.getroot()
# # print(root)
# for child in root.findall("w:hdr"):
#     # print(child)
#     print(root)

zip = None
xml = ""
import zipfile

try:
    zip = zipfile.ZipFile('./sample/ex2.docx')
    for file in zip.filelist:
        if "header" in file.filename:
            xml = zip.extract(file, './sample')
except FileNotFoundError as e:
    print(e)
finally:
    zip.close()

# xml = './sample/header1.xml'
# read write new content
with open(xml, 'r')as file:
    text = file.read()
    if "Lara" in text:
        text = text.replace("Lara", "python that la vai leo")

with open(xml, 'w')as file:
    file.write(text)

print("xml: |" + xml)
# end write
#
# # update to docx
# try:
#     zip = zipfile.ZipFile('./sample/ex2.docx', 'a')
#     for file in zip.filelist:
#         if "header" in file.filename:
#             # zip.write(xml,arcname='word/header1.xml', compress_type=None, compresslevel=None)
#             zip.writestr('./word/header1.xml', text, compress_type=None, compresslevel=None)
# except FileNotFoundError as e:
#     print(e)
# finally:
#     zip.close()


import tempfile
import shutil
import os


def remove_from_zip(zipfname, filenames):
    tempdir = tempfile.mkdtemp()
    print('tempdir|' + tempdir)
    try:
        tempname = os.path.join(tempdir, 'new.zip')
        with zipfile.ZipFile(zipfname, 'r') as zipread:
            with zipfile.ZipFile(tempname, 'w') as zipwrite:
                for item in zipread.infolist():
                    if item.filename not in filenames:
                        data = zipread.read(item.filename)
                        zipwrite.writestr(item, data)
        shutil.move(tempname, zipfname)
    finally:
        shutil.rmtree(tempdir)


#
remove_from_zip('./sample/ex2.docx', 'word/header1.xml')
with zipfile.ZipFile('./sample/ex2.docx', 'a') as z:
    z.write(xml, arcname='word/header1.xml')

# GOOD
# import xmltodict
#
# with open(xml) as fd:
#     doc = xmltodict.parse(fd.read())
#     print(doc)
#     doc["w:hdr"]["w:p"]["w:r"]["w:t"] = "cai lon me may"
#     out = xmltodict.unparse(doc, pretty=True)
#
# with open(xml, 'w') as file:
#     file.write(out)
#

# my own
# with open(xml,'r')as file:
#     text = file.read()
#     if "cai lon me may" in text:
#         text = text.replace("somthing", "python that la vai leo")
#
# with open(xml,'w')as file:
#     file.write(text)
