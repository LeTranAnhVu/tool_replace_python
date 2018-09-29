import sys , os
from cx_Freeze import setup, Executable


os.environ['TCL_LIBRARY'] = r"C:\Users\fuckyoubitch\AppData\Local\Programs\Python\Python36\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\fuckyoubitch\AppData\Local\Programs\Python\Python36\tcl\tk8.6"

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "json", "openpyxl" , "docx"] , "include_files" : [r"C:\Users\fuckyoubitch\AppData\Local\Programs\Python\Python36\DLLs\tcl86t.dll" , r"C:\Users\fuckyoubitch\AppData\Local\Programs\Python\Python36\DLLs\tk86t.dll"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Replace Name",
      version="1.0",
      description="Replaceeeee!",
      options={"build_exe": build_exe_options},
      executables=[Executable("gui.py", base=base)])
