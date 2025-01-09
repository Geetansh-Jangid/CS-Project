import os
import shutil

def file_organizer():
    print("\n=== File Organizer ===")
    directory = input("Enter the directory to organize: ")

    if not os.path.exists(directory):
        print("Directory not found.")
        return

    file_types = {
        "Audio": [".mp3", ".wav", ".m4a", ".aac"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mkv", ".flv", ".avi"],
        "Documents": [".pdf", ".docx", ".xlsx", ".txt"],
        "Archives": [".zip", ".rar", ".7z"],
    }

    for folder, extensions in file_types.items():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in os.listdir(directory):
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(os.path.join(directory, file), folder_path)

    print("Files organized successfully.")
