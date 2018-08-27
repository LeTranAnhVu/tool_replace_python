
import os
import re


new_str = "le tran anh vu "
old_str = "letrananhvu"
base_path = r"C:\Users\letrananhvu\Desktop\sample"
def walkthrough(base_path,old_str,new_str):
    for root , folders , files in os.walk(base_path):
        for folder in folders:
            if(folder.find(old_str)!= -1):
                print("go here")
                new_folder = folder.replace(old_str, new_str)
                print(folder)
                os.renames(os.path.join(root,folder),os.path.join(root,new_folder))
                # update new fd name
                folders[folders.index(folder)]= new_folder
print("hello")
walkthrough(base_path,old_str,new_str)
