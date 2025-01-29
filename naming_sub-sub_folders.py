from pathlib import Path
root_dir = Path('files')
files = root_dir.glob('**/*')
for file in files:
    grandparent = file.parts[-2]
    parent = file.parts[-1]
    new_file = parent + '-' + file.name

    new_file_path = file.with_name(new_file)

    
    file.rename(new_file_path)