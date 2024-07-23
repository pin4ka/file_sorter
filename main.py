import os

# Specify the path to your folder
folder_path = "./"
folder_path.replace("\\", "/")
print(folder_path)
# Get a list of all files and directories in the folder
all_items = os.listdir(folder_path)

# Filter only the files (excluding directories)
files_only = [
    item for item in all_items if os.path.isfile(os.path.join(folder_path, item))
]

print(files_only)

for files in files_only:
    folder_types = files.rsplit(".")[1]

    if folder_types != "exe":
        try:
            os.mkdir(f"All {folder_types} files")
        except:
            pass
    pass

for files in files_only:
    folder_types = files.rsplit(".")[1]
    if folder_types != "exe" or folder_types != "ini":
        try:
            os.rename(files, f"./All {folder_types} files/{files}")
        except:
            pass
