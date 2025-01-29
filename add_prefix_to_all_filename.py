from pathlib import Path

root_dir = Path('files')

files = root_dir.iterdir()

for file in files:
    #setting new name to the file
    new_file_name ='new-' + file.stem + file.suffix
    #making a new file path object
    new_file_path = Path(new_file_name)
    #renaming the  files 
    file.rename(new_file_path)



