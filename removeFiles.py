import time
import shutil
import os

def main():
    deleted_folders_count = 0
    deleted_files_count = 0
    path = 'Path to delete'
    days = 10
    seconds = time.time()-(days*24*60*60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            remove_folder(root_folder)
            deleted_folders_count+=1
    



def remove_folder():
    #removing the folder
    shutil.rmtree(path)
 
def remove_files():
    os.remove(path)
main()