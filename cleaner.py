from os import *
import shutil
import functools
import time
from colorama import Fore


Extensions = ["pdf", "jpg", "docx", "jpeg", "mp3", "mp4", "c", "py", "txt"]

@functools.lru_cache
def cleaner(extension, folderPath):
    if path.exists(folderPath) and path.isdir(folderPath):
        current_directory = getcwd()
        all = listdir(current_directory)
        for files in all:
            if path.isfile(files) and files.endswith(extension):
                print(Fore.LIGHTGREEN_EX + "Processing...............")
                time.sleep(2)
                shutil.move(files, folderPath)
                print(Fore.LIGHTGREEN_EX + f"{files} is moved to {folderPath}...............")
    else:
        print("Oops!! Something went wrong...............")
    time.sleep(3)
     
if __name__ == "__main__":
    ext = input(Fore.CYAN + "Which type of files do you want move :  ")
    pathh = input(Fore.CYAN + "Enter the path :  ")

    cleaner(ext, pathh)

