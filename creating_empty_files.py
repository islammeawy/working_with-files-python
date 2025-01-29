from pathlib import Path

root_dir = Path('files')
for i in range(10 , 21) :
    new_file =f'{i}.txt'
    file_path = root_dir / Path(new_file)
    file_path.touch()