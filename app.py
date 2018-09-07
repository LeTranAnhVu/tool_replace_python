import os
import excel_handler
import text_handler

open_text_and_replace = text_handler.open_text_and_replace
open_excel_and_replace = excel_handler.open_excel_and_replace


# new_str = "ti"
# old_str = "teo"
# base_path = r".\sample"
list_handlers = {
    # "docx" : open_text_and_replace,
    "txt": open_text_and_replace,
    "xls": open_excel_and_replace,
    "xlsx": open_excel_and_replace
}


def replace_name(root, name, old_str, new_str):
    new_name = name.replace(old_str, new_str)
    try:
        os.renames(os.path.join(root, name), os.path.join(root, new_name))
    except FileExistsError:
        os.renames(os.path.join(root, name), os.path.join(root, new_name + "_"))
    return new_name


def walkthrough(base_path, old_str, new_str):
    for root, folders, files in os.walk(base_path):
        for folder in folders:
            if (folder.find(old_str) != -1):
                new_folder = replace_name(root, folder, old_str, new_str)
                # update new fd name
                folders[folders.index(folder)] = new_folder
        for file in files:
            # do something
            file_path = os.path.join(root, file)
            extension = file.split(".")[-1]
            try:
                list_handlers[extension](file_path, old_str, new_str)
            except KeyError:
                print("key not found")
            new_file = replace_name(root, file, old_str, new_str)
            print("new file: ", new_file)
            # update new fd name
            files[files.index(file)] = new_file

# walkthrough(base_path,old_str,new_str)
