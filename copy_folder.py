from shutil import copytree, rmtree
from os import path, getcwd
from error_handler import  PrintException
from app import TESTMODE
import errno

SRC = r'./sample'
DEST = r'./sample-copy'


def pathfactory(root, name):
    dir = path.join(root, name)
    return dir


def copy_folder(root, name, *copiedName):
    src = pathfactory(root, name)
    # check whether copiedName para is passed in function or not
    if not copiedName or not isinstance(copiedName[0], str):
        copiedName = name + "-copy"
    else:
        # keep the copiedName
        pass

    dest = pathfactory(root, copiedName)

    # try to make a copy
    try:
        copytree(src, dest)
    except FileExistsError:
        rmtree(dest)
        copytree(src, dest)
    except FileNotFoundError:
        # show this error in log
        PrintException(testmode=TESTMODE)
    print("copy OK")


root = getcwd()


copy_folder(root, 'sample')
