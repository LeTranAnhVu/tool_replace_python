
import os



new_str = "Pham thi thu trang"
old_str = "le tran anh vu"
base_path = r"C:\Users\letrananhvu\Desktop\sample"

def replace_folder(root,folder,old_str,new_str):
    new_folder = folder.replace(old_str, new_str)
    os.renames(os.path.join(root, folder), os.path.join(root, new_folder))
    return new_folder

def walkthrough(base_path,old_str,new_str):
    for root , folders , files in os.walk(base_path):
        for folder in folders:
            if(folder.find(old_str)!= -1):
                new_folder = replace_folder(root, folder, old_str, new_str)
                # update new fd name
                folders[folders.index(folder)]= new_folder
        for file in files :
            if(file == "hehe.xlsx"):
                #do something
                print("go here")
                file_path = os.path.join(root, file)
                new_content = ""
                try :
                    with open(file_path,'r') as f:
                        new_content += (f.read()).replace(old_str,new_str)
                        print(new_content)
                except IOError as e:
                    print(e)
                try:
                    with open(file_path,'w') as f:
                        if(new_content != ""):
                            f.write(new_content)
                            print("write ok")
                except IOError as e:
                    print(e)
                    # f.write("new string")
                    # for line  in f.readlines() :
                    #     print("line--> " , line)
                    #     line = line


walkthrough(base_path,old_str,new_str)
