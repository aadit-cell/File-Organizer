import os
import shutil

folder = input("Enter folder path: ")

files = os.listdir(folder)

categories = {
    ".py": "Python",
    ".md": "Documents",
    ".txt": "Text",
    ".csv": "CSV",
    ".json": "JSON",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".mp4": "Video",
    ".avi": "Video",
    ".mkv": "Video",
    ".zip": "Compressed",
    ".rar": "Compressed",
    ".exe": "Executables"
}

for file in files:
    extension = os.path.splitext(file)[1].lower()

    if extension in categories:
        category = categories[extension]

        category_folder = os.path.join(folder, category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        print(file, "->", category)

        shutil.move(
            os.path.join(folder, file),
            os.path.join(category_folder, file)
        )

