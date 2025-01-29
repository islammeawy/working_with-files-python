'''from pathlib import Path
import zipfile

root_dir = Path('files')
archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
  for path in root_dir.rglob("*.txt"):
    zf.write(path)
    path.unlink() '''
# put the zip files in file
from pathlib import Path
import zipfile
root_dir = Path('files')
folder_path = root_dir / Path(r'C:\Users\SMSMAAA\working_with_files\files\to put')
for path in root_dir.rglob("*.zip"):
  with zipfile.ZipFile(path, 'r') as zf:
    final_path = folder_path / path.stem
    zf.extractall(path=final_path)