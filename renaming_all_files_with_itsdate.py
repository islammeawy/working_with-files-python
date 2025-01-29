from pathlib import Path
from datetime import datetime

# Target directory containing files
root_dir = Path('files')
files = list(root_dir.glob('**/*'))

for file in files:
    if file.is_file():  # Ensure it's a file
        # Get file creation time
        stats = file.stat()
        second_created = stats.st_ctime
        date_created = datetime.fromtimestamp(second_created)

        # Format date for file name
        created_date_str = date_created.strftime("%Y-%m-%d_%H-%M-%S")

        # Construct new file name with extension
        new_file_name = f"{created_date_str}_{file.stem}{file.suffix}"

        # Handle potential name conflicts
        new_file_path = file.with_name(new_file_name)
        counter = 1
        while new_file_path.exists():
            # Avoid overwriting by appending a counter if file exists
            new_file_name = f"{created_date_str}_{file.stem}_{counter}{file.suffix}"
            new_file_path = file.with_name(new_file_name)
            counter += 1

        # Rename the file
        file.rename(new_file_path)

print("Renaming complete.")

