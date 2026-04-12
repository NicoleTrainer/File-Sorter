# File Sorter

A Python script that automatically sorts files in a given directory into categorized subfolders based on file extension.

## Features

- Sorts files into Images, Documents, Audio, and Other folders
- Creates destination folders automatically if they don't exist
- Easy to extend with new file types

## How to Run

1. Clone the repository
2. Edit the `path` variable in `File_Organizer.py` to point to the folder you want to sort
3. Run the script:

```bash
python File_Organizer.py
```

## Supported File Types

| Category  | Extensions                        |
|-----------|-----------------------------------|
| Images    | .jpg, .jpeg, .png, .gif, .bmp     |
| Documents | .pdf, .docx, .txt, .xlsx, .pptx   |
| Audio     | .mp3, .wav, .flac, .aac           |
| Other     | anything not listed above         |
