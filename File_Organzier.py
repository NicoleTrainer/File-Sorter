import os
import shutil
from pathlib import Path

File_types = ["Images", "Documents", "Videos", "Other"]

Images = [".jpg", ".jpeg", ".png", ".gif"]
Documents = [".pdf", ".docx", ".txt"]
Videos = [".mp4", ".mov", ".avi"]


folder = Path(input("Enter Path: "))

for new_folder in File_types:
    new_dir = folder / new_folder
    new_dir.mkdir(exist_ok=True)

for file in folder.iterdir():
    if file.is_file():
        ext = file.suffix.lower()
        if ext in Images:
            shutil.move(str(file), str(folder / "Images"))
        elif ext in Documents:
            shutil.move(str(file), str(folder / "Documents"))
        elif ext in Videos:
            shutil.move(str(file), str(folder / "Videos"))
        else:
            shutil.move(str(file), str(folder / "Other"))