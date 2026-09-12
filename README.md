# File Organizer

A simple Python program that organizes files into different folders based on their file extensions.

## Features

* Organizes files automatically
* Creates folders when needed
* Supports different file types
* Handles file extensions without worrying about uppercase/lowercase
* Uses a dictionary to map file extensions to folders

## File Categories

* `.py` → Python
* `.md` → Documents
* `.txt` → Text
* `.csv` → CSV
* `.json` → JSON
* `.jpg`, `.jpeg`, `.png` → Images
* `.mp3`, `.wav` → Audio
* `.mp4`, `.avi`, `.mkv` → Video
* `.zip`, `.rar` → Compressed
* `.exe` → Executables

## How to Run

Make sure Python is installed.

Run the program:

```bash
python file_organizer.py
```

Enter the path of the folder you want to organize when asked.

## Example

Before:

```text
MyFolder/
├── photo.jpg
├── song.mp3
├── notes.txt
└── program.py
```

After:

```text
MyFolder/
├── Images/
│   └── photo.jpg
├── Audio/
│   └── song.mp3
├── Text/
│   └── notes.txt
└── Python/
    └── program.py
```

## What I Learned

* Working with files and folders using `os`
* Moving files using `shutil`
* Getting file extensions
* Using dictionaries to organize data
* Creating folders with Python
* Using loops and conditions
* Writing cleaner code instead of repeating the same logic

## Built With

* Python
* os
* shutil

