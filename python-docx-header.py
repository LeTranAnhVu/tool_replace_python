
import xmltodict

with open(xml) as fd:
    doc = xmltodict.parse(fd.read())
    print(doc)
    doc["w:hdr"]["w:p"]["w:r"]["w:t"] = "cai lon me may"
    out = xmltodict.unparse(doc, pretty=True)

with open(xml, 'w') as file:
    file.write(out)


# input xml path

# make header

# return obj name header have the struture like the mockup


# class Docx_Header:
