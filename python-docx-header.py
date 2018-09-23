import xmltodict
import os
from error_handler import ErrorHandler, PrintException


# with open(xml) as fd:
#     doc = xmltodict.parse(fd.read())
#     print(doc)
#     doc["w:hdr"]["w:p"]["w:r"]["w:t"] = ""
#     out = xmltodict.unparse(doc, pretty=True)
#
# with open(xml, 'w') as file:
#     file.write(out)


# input xml path

# make header

# return obj name header have the struture like the mockup


# dict
# OrderedDict([('w:hdr', OrderedDict([('@xmlns:wpc', 'http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas'), ('@xmlns:cx', 'http://schemas.microsoft.com/office/drawing/2014/chartex'), ('@xmlns:cx1', 'http://schemas.microsoft.com/office/drawing/2015/9/8/chartex'), ('@xmlns:mc', 'http://schemas.openxmlformats.org/markup-compatibility/2006'), ('@xmlns:o', 'urn:schemas-microsoft-com:office:office'), ('@xmlns:r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'), ('@xmlns:m', 'http://schemas.openxmlformats.org/officeDocument/2006/math'), ('@xmlns:v', 'urn:schemas-microsoft-com:vml'), ('@xmlns:wp14', 'http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing'), ('@xmlns:wp', 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'), ('@xmlns:w10', 'urn:schemas-microsoft-com:office:word'), ('@xmlns:w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'), ('@xmlns:w14', 'http://schemas.microsoft.com/office/word/2010/wordml'), ('@xmlns:w15', 'http://schemas.microsoft.com/office/word/2012/wordml'), ('@xmlns:w16se', 'http://schemas.microsoft.com/office/word/2015/wordml/symex'), ('@xmlns:wpg', 'http://schemas.microsoft.com/office/word/2010/wordprocessingGroup'), ('@xmlns:wpi', 'http://schemas.microsoft.com/office/word/2010/wordprocessingInk'), ('@xmlns:wne', 'http://schemas.microsoft.com/office/word/2006/wordml'), ('@xmlns:wps', 'http://schemas.microsoft.com/office/word/2010/wordprocessingShape'), ('@mc:Ignorable', 'w14 w15 w16se wp14'), ('w:p', [OrderedDict([('@w:rsidR', '00790A97'), ('@w:rsidRDefault', '00935AAA'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')]))])), ('w:r', [OrderedDict([('w:t', OrderedDict([('@xml:space', 'preserve'), ('#text', 'python that')]))]), OrderedDict([('@w:rsidR', '00790A97'), ('w:t', 'la vai leo')])])]), OrderedDict([('@w:rsidR', '00BA469C'), ('@w:rsidRDefault', '00493F3D'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')]))])), ('w:r', OrderedDict([('w:t', 'Ten ten')]))]), OrderedDict([('@w:rsidR', '00493F3D'), ('@w:rsidRDefault', '00493F3D'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:rPr', OrderedDict([('w:b', None)]))])), ('w:r', [OrderedDict([('w:t', OrderedDict([('@xml:space', 'preserve'), ('#text', 'Hello')]))]), OrderedDict([('@w:rsidRPr', '00493F3D'), ('w:rPr', OrderedDict([('w:i', None)])), ('w:t', 'ben')]), OrderedDict([('w:t', OrderedDict([('@xml:space', 'preserve'), ('#text', 'ra minh')]))]), OrderedDict([('@w:rsidRPr', '00493F3D'), ('w:rPr', OrderedDict([('w:b', None)])), ('w:t', 'sdjfljas')])])]), OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')]))]))])]), ('w:tbl', [OrderedDict([('w:tblPr', OrderedDict([('w:tblStyle', OrderedDict([('@w:val', 'TableGrid')])), ('w:tblW', OrderedDict([('@w:w', '0'), ('@w:type', 'auto')])), ('w:tblInd', OrderedDict([('@w:w', '1134'), ('@w:type', 'dxa')])), ('w:tblLook', OrderedDict([('@w:val', '04A0'), ('@w:firstRow', '1'), ('@w:lastRow', '0'), ('@w:firstColumn', '1'), ('@w:lastColumn', '0'), ('@w:noHBand', '0'), ('@w:noVBand', '1')]))])), ('w:tblGrid', OrderedDict([('w:gridCol', [OrderedDict([('@w:w', '2116')]), OrderedDict([('@w:w', '1992')]), OrderedDict([('@w:w', '2116')]), OrderedDict([('@w:w', '1992')])])])), ('w:tr', [OrderedDict([('@w:rsidR', '00BA469C'), ('@w:rsidTr', '00BA469C'), ('w:tc', [OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00BA469C'), ('@w:rsidRDefault', '00BA469C'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))])), ('w:r', OrderedDict([('w:t', 'cell_00')]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00BA469C'), ('@w:rsidRDefault', '00BA469C'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00BA469C'), ('@w:rsidRDefault', '00BA469C'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00BA469C'), ('@w:rsidRDefault', '00BA469C'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))])])]), OrderedDict([('@w:rsidR', '00BA469C'), ('@w:rsidTr', '00BA469C'), ('w:tc', [OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00BA469C'), ('@w:rsidRDefault', '00BA469C'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00BA469C'), ('@w:rsidRDefault', '00BA469C'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00BA469C'), ('@w:rsidRDefault', '00BA469C'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))])), ('w:r', OrderedDict([('w:t', 'cell_12')]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00BA469C'), ('@w:rsidRDefault', '00BA469C'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))])])]), OrderedDict([('@w:rsidR', '00493F3D'), ('@w:rsidTr', '00BA469C'), ('w:tc', [OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00493F3D'), ('@w:rsidRDefault', '00493F3D'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))])), ('w:r', OrderedDict([('w:t', 'as')]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00493F3D'), ('@w:rsidRDefault', '00493F3D'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00493F3D'), ('@w:rsidRDefault', '00493F3D'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '00493F3D'), ('@w:rsidRDefault', '00493F3D'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))])])])])]), OrderedDict([('w:tblPr', OrderedDict([('w:tblStyle', OrderedDict([('@w:val', 'TableGrid')])), ('w:tblW', OrderedDict([('@w:w', '0'), ('@w:type', 'auto')])), ('w:tblInd', OrderedDict([('@w:w', '1134'), ('@w:type', 'dxa')])), ('w:tblLook', OrderedDict([('@w:val', '04A0'), ('@w:firstRow', '1'), ('@w:lastRow', '0'), ('@w:firstColumn', '1'), ('@w:lastColumn', '0'), ('@w:noHBand', '0'), ('@w:noVBand', '1')]))])), ('w:tblGrid', OrderedDict([('w:gridCol', [OrderedDict([('@w:w', '2083')]), OrderedDict([('@w:w', '2024')]), OrderedDict([('@w:w', '2084')]), OrderedDict([('@w:w', '2025')])])])), ('w:tr', [OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidTr', '009240D7'), ('w:tc', [OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))])), ('w:r', OrderedDict([('w:t', 'tbl2')]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))])])]), OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidTr', '009240D7'), ('w:tc', [OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))])), ('w:r', OrderedDict([('w:t', 'tbl2')]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))])])]), OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidTr', '009240D7'), ('w:tc', [OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))])), ('w:r', OrderedDict([('w:t', 'tbl2')]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2337'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))]), OrderedDict([('w:tcPr', OrderedDict([('w:tcW', OrderedDict([('@w:w', '2338'), ('@w:type', 'dxa')]))])), ('w:p', OrderedDict([('@w:rsidR', '0094415B'), ('@w:rsidRDefault', '0094415B'), ('@w:rsidP', '0094415B'), ('w:pPr', OrderedDict([('w:pStyle', OrderedDict([('@w:val', 'Header')])), ('w:ind', OrderedDict([('@w:left', '0')]))]))]))])])])])])])]))])


# json
# {"w:hdr": {"@xmlns:wpc": "http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas", "@xmlns:cx": "http://schemas.microsoft.com/office/drawing/2014/chartex", "@xmlns:cx1": "http://schemas.microsoft.com/office/drawing/2015/9/8/chartex", "@xmlns:mc": "http://schemas.openxmlformats.org/markup-compatibility/2006", "@xmlns:o": "urn:schemas-microsoft-com:office:office", "@xmlns:r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships", "@xmlns:m": "http://schemas.openxmlformats.org/officeDocument/2006/math", "@xmlns:v": "urn:schemas-microsoft-com:vml", "@xmlns:wp14": "http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing", "@xmlns:wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing", "@xmlns:w10": "urn:schemas-microsoft-com:office:word", "@xmlns:w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main", "@xmlns:w14": "http://schemas.microsoft.com/office/word/2010/wordml", "@xmlns:w15": "http://schemas.microsoft.com/office/word/2012/wordml", "@xmlns:w16se": "http://schemas.microsoft.com/office/word/2015/wordml/symex", "@xmlns:wpg": "http://schemas.microsoft.com/office/word/2010/wordprocessingGroup", "@xmlns:wpi": "http://schemas.microsoft.com/office/word/2010/wordprocessingInk", "@xmlns:wne": "http://schemas.microsoft.com/office/word/2006/wordml", "@xmlns:wps": "http://schemas.microsoft.com/office/word/2010/wordprocessingShape", "@mc:Ignorable": "w14 w15 w16se wp14", "w:p": [{"@w:rsidR": "00790A97", "@w:rsidRDefault": "00935AAA", "w:pPr": {"w:pStyle": {"@w:val": "Header"}}, "w:r": [{"w:t": {"@xml:space": "preserve", "#text": "python that"}}, {"@w:rsidR": "00790A97", "w:t": "la vai leo"}]}, {"@w:rsidR": "00BA469C", "@w:rsidRDefault": "00493F3D", "w:pPr": {"w:pStyle": {"@w:val": "Header"}}, "w:r": {"w:t": "Ten ten"}}, {"@w:rsidR": "00493F3D", "@w:rsidRDefault": "00493F3D", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:rPr": {"w:b": null}}, "w:r": [{"w:t": {"@xml:space": "preserve", "#text": "Hello"}}, {"@w:rsidRPr": "00493F3D", "w:rPr": {"w:i": null}, "w:t": "ben"}, {"w:t": {"@xml:space": "preserve", "#text": "ra minh"}}, {"@w:rsidRPr": "00493F3D", "w:rPr": {"w:b": null}, "w:t": "sdjfljas"}]}, {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}}}], "w:tbl": [{"w:tblPr": {"w:tblStyle": {"@w:val": "TableGrid"}, "w:tblW": {"@w:w": "0", "@w:type": "auto"}, "w:tblInd": {"@w:w": "1134", "@w:type": "dxa"}, "w:tblLook": {"@w:val": "04A0", "@w:firstRow": "1", "@w:lastRow": "0", "@w:firstColumn": "1", "@w:lastColumn": "0", "@w:noHBand": "0", "@w:noVBand": "1"}}, "w:tblGrid": {"w:gridCol": [{"@w:w": "2116"}, {"@w:w": "1992"}, {"@w:w": "2116"}, {"@w:w": "1992"}]}, "w:tr": [{"@w:rsidR": "00BA469C", "@w:rsidTr": "00BA469C", "w:tc": [{"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00BA469C", "@w:rsidRDefault": "00BA469C", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}, "w:r": {"w:t": "cell_00"}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00BA469C", "@w:rsidRDefault": "00BA469C", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00BA469C", "@w:rsidRDefault": "00BA469C", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00BA469C", "@w:rsidRDefault": "00BA469C", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}]}, {"@w:rsidR": "00BA469C", "@w:rsidTr": "00BA469C", "w:tc": [{"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00BA469C", "@w:rsidRDefault": "00BA469C", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00BA469C", "@w:rsidRDefault": "00BA469C", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00BA469C", "@w:rsidRDefault": "00BA469C", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}, "w:r": {"w:t": "cell_12"}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00BA469C", "@w:rsidRDefault": "00BA469C", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}]}, {"@w:rsidR": "00493F3D", "@w:rsidTr": "00BA469C", "w:tc": [{"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00493F3D", "@w:rsidRDefault": "00493F3D", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}, "w:r": {"w:t": "as"}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00493F3D", "@w:rsidRDefault": "00493F3D", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00493F3D", "@w:rsidRDefault": "00493F3D", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "00493F3D", "@w:rsidRDefault": "00493F3D", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}]}]}, {"w:tblPr": {"w:tblStyle": {"@w:val": "TableGrid"}, "w:tblW": {"@w:w": "0", "@w:type": "auto"}, "w:tblInd": {"@w:w": "1134", "@w:type": "dxa"}, "w:tblLook": {"@w:val": "04A0", "@w:firstRow": "1", "@w:lastRow": "0", "@w:firstColumn": "1", "@w:lastColumn": "0", "@w:noHBand": "0", "@w:noVBand": "1"}}, "w:tblGrid": {"w:gridCol": [{"@w:w": "2083"}, {"@w:w": "2024"}, {"@w:w": "2084"}, {"@w:w": "2025"}]}, "w:tr": [{"@w:rsidR": "0094415B", "@w:rsidTr": "009240D7", "w:tc": [{"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}, "w:r": {"w:t": "tbl2"}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}]}, {"@w:rsidR": "0094415B", "@w:rsidTr": "009240D7", "w:tc": [{"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}, "w:r": {"w:t": "tbl2"}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}]}, {"@w:rsidR": "0094415B", "@w:rsidTr": "009240D7", "w:tc": [{"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}, "w:r": {"w:t": "tbl2"}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2337", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}, {"w:tcPr": {"w:tcW": {"@w:w": "2338", "@w:type": "dxa"}}, "w:p": {"@w:rsidR": "0094415B", "@w:rsidRDefault": "0094415B", "@w:rsidP": "0094415B", "w:pPr": {"w:pStyle": {"@w:val": "Header"}, "w:ind": {"@w:left": "0"}}}}]}]}]}}


# xml is the relative path from this path of this module to the path of the xml file

class Docx_Header:
    def __init__(self, path):
        self.path = path
        self.hdrDict = self.read_xml()
        self.paragraphs = []
        try:
            plist = self.hdrDict['w:p']
            for p in plist:
                self.paragraphs.append(Paragraph(p))
        except KeyError as e:
            PrintException()
            pass

    def read_xml(self):
        path = self.path
        with open(path, 'r') as xml:
            xmldict = xmltodict.parse(xml.read())
            return xmldict["w:hdr"]
    # def parse_xml(self):


class Paragraph:
    def __init__(self, pdict):
        self.text = "Para"
        self.runs = []
        try:
            rlist = pdict["w:r"]
            print("@@@@")
            print(rlist)
            print("@@@@")
            for r in rlist:
                print("####")
                print(r)
                print("####")
                self.runs.append(Run(r))
        except KeyError as e:
            PrintException()
            pass


class Run:
    def __init__(self, rdict):
        self.text = "run...."
        try:
            print((rdict["w:t"]["#text"]))
        except KeyError as e:
            PrintException()
            pass
        except TypeError as e:
            PrintException()
            pass
        # try :
        #     textdict = rdict["w:t"]
        #     self.text = Text(textdict).text
        # except KeyError as e:
        #     PrintException()
        #     pass

class Text:
    def __init__(self, text):
        self.text = text


header = Docx_Header('./sample/word/header1.xml')
#
# for p in header.paragraphs:
#     print(p)
#     for r in p.runs:
#         print(r.text)

#
#
# <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
# <w:hdr
# 	xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas"
# 	xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex"
# 	xmlns:cx1="http://schemas.microsoft.com/office/drawing/2015/9/8/chartex"
# 	xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
# 	xmlns:o="urn:schemas-microsoft-com:office:office"
# 	xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
# 	xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"
# 	xmlns:v="urn:schemas-microsoft-com:vml"
# 	xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing"
# 	xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
# 	xmlns:w10="urn:schemas-microsoft-com:office:word"
# 	xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
# 	xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"
# 	xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml"
# 	xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex"
# 	xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup"
# 	xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk"
# 	xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml"
# 	xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 w15 w16se wp14">
# 	<w:p w:rsidR="00790A97" w:rsidRDefault="00935AAA">
# 		<w:pPr>
# 			<w:pStyle w:val="Header"/>
# 		</w:pPr>
# 		<w:r>
# 			<w:t xml:space="preserve">python that </w:t>
# 		</w:r>
# 		<w:r w:rsidR="00790A97">
# 			<w:t>la vai leo</w:t>
# 		</w:r>
# 	</w:p>
# 	<w:tbl>
# 		<w:tblPr>
# 			<w:tblStyle w:val="TableGrid"/>
# 			<w:tblW w:w="0" w:type="auto"/>
# 			<w:tblInd w:w="1134" w:type="dxa"/>
# 			<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>
# 		</w:tblPr>
# 		<w:tblGrid>
# 			<w:gridCol w:w="2116"/>
# 			<w:gridCol w:w="1992"/>
# 			<w:gridCol w:w="2116"/>
# 			<w:gridCol w:w="1992"/>
# 		</w:tblGrid>
# 		<w:tr w:rsidR="00BA469C" w:rsidTr="00BA469C">
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00BA469C" w:rsidRDefault="00BA469C">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 					<w:r>
# 						<w:t>cell_00</w:t>
# 					</w:r>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00BA469C" w:rsidRDefault="00BA469C">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00BA469C" w:rsidRDefault="00BA469C">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00BA469C" w:rsidRDefault="00BA469C">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 		</w:tr>
# 		<w:tr w:rsidR="00BA469C" w:rsidTr="00BA469C">
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00BA469C" w:rsidRDefault="00BA469C">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00BA469C" w:rsidRDefault="00BA469C">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00BA469C" w:rsidRDefault="00BA469C">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 					<w:r>
# 						<w:t>cell_12</w:t>
# 					</w:r>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00BA469C" w:rsidRDefault="00BA469C">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 		</w:tr>
# 		<w:tr w:rsidR="00493F3D" w:rsidTr="00BA469C">
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00493F3D" w:rsidRDefault="00493F3D">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 					<w:r>
# 						<w:t>as</w:t>
# 					</w:r>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00493F3D" w:rsidRDefault="00493F3D">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00493F3D" w:rsidRDefault="00493F3D">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="00493F3D" w:rsidRDefault="00493F3D">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 		</w:tr>
# 	</w:tbl>
# 	<w:p w:rsidR="00BA469C" w:rsidRDefault="00493F3D">
# 		<w:pPr>
# 			<w:pStyle w:val="Header"/>
# 		</w:pPr>
# 		<w:r>
# 			<w:t>Ten ten</w:t>
# 		</w:r>
# 	</w:p>
# 	<w:p w:rsidR="00493F3D" w:rsidRDefault="00493F3D">
# 		<w:pPr>
# 			<w:pStyle w:val="Header"/>
# 			<w:rPr>
# 				<w:b/>
# 			</w:rPr>
# 		</w:pPr>
# 		<w:r>
# 			<w:t xml:space="preserve">Hello </w:t>
# 		</w:r>
# 		<w:r w:rsidRPr="00493F3D">
# 			<w:rPr>
# 				<w:i/>
# 			</w:rPr>
# 			<w:t>ben</w:t>
# 		</w:r>
# 		<w:r>
# 			<w:t xml:space="preserve"> ra minh </w:t>
# 		</w:r>
# 		<w:r w:rsidRPr="00493F3D">
# 			<w:rPr>
# 				<w:b/>
# 			</w:rPr>
# 			<w:t>sdjfljas</w:t>
# 		</w:r>
# 	</w:p>
# 	<w:tbl>
# 		<w:tblPr>
# 			<w:tblStyle w:val="TableGrid"/>
# 			<w:tblW w:w="0" w:type="auto"/>
# 			<w:tblInd w:w="1134" w:type="dxa"/>
# 			<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>
# 		</w:tblPr>
# 		<w:tblGrid>
# 			<w:gridCol w:w="2083"/>
# 			<w:gridCol w:w="2024"/>
# 			<w:gridCol w:w="2084"/>
# 			<w:gridCol w:w="2025"/>
# 		</w:tblGrid>
# 		<w:tr w:rsidR="0094415B" w:rsidTr="009240D7">
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 					<w:r>
# 						<w:t>tbl2</w:t>
# 					</w:r>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 		</w:tr>
# 		<w:tr w:rsidR="0094415B" w:rsidTr="009240D7">
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 					<w:r>
# 						<w:t>tbl2</w:t>
# 					</w:r>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 		</w:tr>
# 		<w:tr w:rsidR="0094415B" w:rsidTr="009240D7">
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 					<w:r>
# 						<w:t>tbl2</w:t>
# 					</w:r>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2337" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 			<w:tc>
# 				<w:tcPr>
# 					<w:tcW w:w="2338" w:type="dxa"/>
# 				</w:tcPr>
# 				<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B" w:rsidP="0094415B">
# 					<w:pPr>
# 						<w:pStyle w:val="Header"/>
# 						<w:ind w:left="0"/>
# 					</w:pPr>
# 				</w:p>
# 			</w:tc>
# 		</w:tr>
# 	</w:tbl>
# 	<w:p w:rsidR="0094415B" w:rsidRDefault="0094415B">
# 		<w:pPr>
# 			<w:pStyle w:val="Header"/>
# 		</w:pPr>
# 	</w:p>
# </w:hdr>