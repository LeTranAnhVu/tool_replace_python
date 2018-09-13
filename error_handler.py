# this file is use to build the error to be for structure -> easy to handler

class ErrorHandler:
    def __init__(self,problem_location, error_discription):
        self.eDisc = error_discription
        self.where = problem_location
    def showError(self):
        print(self.where)
        print(self.eDisc)

