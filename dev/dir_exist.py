from os import listdir
from pathlib import Path

def dir_exist():
    # Get current directory path.
    dir_path = Path.cwd()

    # list of files.
    dir_file_list = listdir(dir_path)

    # return the list of files. 
    return dir_file_list
