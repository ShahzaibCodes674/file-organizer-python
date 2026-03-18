# SMART FILE ORGANIZER with LOGGING

import os 
import shutil

Folder = input("Enter name of folder to organize files: ")

# ...... LOG FUNCTION ......
def log_action(message):
    with open("log.text", "a") as log:
        log.write(message + "\n")

# ...... CREATE FOLDERS FUNCTION ......
def create_folders(Folder):
    folders = ["PDFs", "Images", "Videos", "Documents", "Large_files", "Others"]

    for folder in folders:
        os.makedirs(os.path.join(Folder, folder), exist_ok = True)

# ...... MAIN ORGANIZER FUNCTION ......
def organize_files(Folder):
    
    files = os.listdir(Folder)
    
    count = 1
    
    for file in files:

        path = os.path.join(Folder, file)

        if os.path.isdir(path):
            continue

        # Determine_size
        size = os.path.getsize(path)
        size_mb = size / (1024*1024)

        if size_mb > 5:
            shutil.move(path, os.path.join(Folder, "Large_files"))
            continue
        log_action("Large_files")

        if file.lower().endswith(".pdf"):
            print("PDFs")
    
        # Rename_files
        name, ext = os.path.splitext(file)
        new_name = "file_" + str(count) + ext
        new_path = os.path.join(Folder, new_name)
        os.rename(path, new_path)

        path = new_path
        file = new_name
        count += 1

        # File type check
        if file.lower().endswith(".pdf"):
            print("PDfs")
            count += 1
            shutil.move(path, os.path.join(Folder, "PDFs", file))
            log_action("PDFs")

        elif file.lower().endswith((".jpg", ".jpeg", ".png")):
            print("Images")
            count += 1
            shutil.move(path, os.path.join(Folder, "Images", file))
            log_action("Images")

        elif file.lower().endswith(".mp4"):
            print("Videos")
            count += 1
            shutil.move(path, os.path.join(Folder, "Videos", file))
            log_action("Videos")

        elif file.lower().endswith((".doc", ".docx")):
            print("Documents")
            count += 1
            shutil.move(path, os.path.join(Folder, "Documents", file))
            log_action("Documents")

        else:
            print("Others")
            count += 1
            shutil.move(path, os.path.join(Folder, "Others", file))
            log_action("Others")

create_folders(Folder)
organize_files(Folder)

print("Files organized successfully!")

