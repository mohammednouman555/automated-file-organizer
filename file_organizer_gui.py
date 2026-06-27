import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage


# ------------------------------------
# Function to load resources in EXE
# ------------------------------------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# -------------------------------
# Function to Organize Files
# -------------------------------
def organize_files(target_folder):
    FILE_TYPES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Music": [".mp3", ".wav", ".aac"],
        "Compressed": [".zip", ".rar", ".7z"],
        "Programs": [".exe", ".msi"],
        "Scripts": [".py", ".js", ".sh", ".bat"]
    }

    for category in FILE_TYPES.keys():
        category_path = os.path.join(target_folder, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    for file_name in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file_name)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(file_name)
        extension = extension.lower()

        moved = False
        for category, extensions in FILE_TYPES.items():
            if extension in extensions:
                shutil.move(file_path, os.path.join(target_folder, category, file_name))
                moved = True
                break

        if not moved:
            other_path = os.path.join(target_folder, "Others")
            if not os.path.exists(other_path):
                os.makedirs(other_path)
            shutil.move(file_path, os.path.join(other_path, file_name))


# -------------------------------
# Browse Folder
# -------------------------------
def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_selected)


# -------------------------------
# Start Organizing
# -------------------------------
def start_organizing():
    folder = folder_path_entry.get()

    if not folder or not os.path.isdir(folder):
        messagebox.showerror("Error", "Please select a valid folder.")
        return

    organize_files(folder)
    messagebox.showinfo("Success", "Files organized successfully!")


# -------------------------------
# GUI Window Setup
# -------------------------------
root = tk.Tk()
root.title("File Organizer Tool")
root.geometry("450x180")
root.resizable(False, False)

# Load PNG icon using iconphoto
icon_path = resource_path("app_icon.png")
icon_img = PhotoImage(file=icon_path)
root.iconphoto(False, icon_img)

# Font
FONT = ("Segoe UI", 11)

tk.Label(root, text="Select Folder:", font=FONT).pack(pady=10)
folder_path_entry = tk.Entry(root, width=45, font=FONT)
folder_path_entry.pack()

browse_btn = tk.Button(root, text="Browse", width=10, command=browse_folder)
browse_btn.pack(pady=5)

organize_btn = tk.Button(root, text="Organize Files", width=15, command=start_organizing)
organize_btn.pack(pady=10)

root.mainloop()
