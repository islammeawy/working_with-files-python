from pathlib import Path
root_dir = Path('files')
for file in root_dir.glob('*.txt'):
    if file.is_file():
        new_file = file.with_suffix('.csv')
        file.rename(new_file)