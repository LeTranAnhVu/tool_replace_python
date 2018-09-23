# this file is use to build the error to be for structure -> easy to handler

class ErrorHandler:
    def __init__(self, problem_location, error_discription):
        self.eDisc = repr(error_discription)
        self.where = problem_location

    def showError(self):
        print("ERROR:>>>")
        print(self.eDisc)
        print("in")
        print(self.where)
        print("<<<<<<<<<")


import linecache
import sys


def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))
