import os
import shutil

def organize_files_by_keyword(directory, keywords):
    # Create folders for each keyword
    for keyword in keywords:
        folder_path = os.path.join(directory, keyword)
        os.makedirs(folder_path, exist_ok=True)
    
    # Iterate through files and move them to the respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            for keyword in keywords:
                if keyword in filename:
                    shutil.move(file_path, os.path.join(directory, keyword, filename))
                    print(f"Moved {filename} to {keyword} folder")
                    break

directory = "C:/Users/prath/Desktop/better-gui/files/assest/light"
keywords = ['12', '24', '28', '32', '48', '20', '16']  # Your keywords
organize_files_by_keyword(directory, keywords)

print("Files sorted successfully!")
