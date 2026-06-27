# 📂 Smart File Organizer

A simple and user-friendly desktop application built with **Python** and **Tkinter** that automatically organizes files into categorized folders based on their file extensions. The application helps keep directories clean by sorting documents, images, videos, music, archives, and other file types into their respective folders.

---

## 📖 Overview

Managing a folder filled with different file types can be time-consuming. Smart File Organizer simplifies this process by automatically moving files into categorized folders with just a few clicks.

The application provides a graphical interface where users can select a folder, organize its contents, and receive confirmation once the process is complete.

---

## ✨ Features

- Simple and intuitive GUI
- Browse and select any folder
- Automatically create category folders
- Organize files by extension
- Supports multiple file categories
- Fast and lightweight
- Beginner-friendly interface
- No internet connection required
- Cross-platform (Windows, Linux, macOS)

---
=======
# Automatic File Organizer – Python Utility Tool

This is a Python-based file management utility that automatically organizes all files inside a selected folder into categorized sub-folders such as **Images**, **Documents**, **Videos**, **Music**, **Programs**, **Scripts**, **Compressed**, and **Others**.


## 📁 File Categories


The organizer sorts files into folders such as:

- 📄 Documents
- 🖼️ Images
- 🎥 Videos
- 🎵 Audio
- 📦 Archives
- 💻 Programs
- 📂 Others

> Files with unsupported extensions remain in the "Others" folder or their original location depending on the implementation.

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- os
- shutil
- pathlib (if used)

---

## 📂 Project Structure

```
SmartFileOrganizer/
│
├── file_organizer.py
├── file_organizer_gui.py
├── file_organizer_select_folder.py
├── app_icon.ico
├── SmartFileOrganizer.spec
├── build/
├── dist/
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/SmartFileOrganizer.git
```

### 2. Navigate to the project

```bash
cd SmartFileOrganizer
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### GUI Version (Recommended)

```bash
python file_organizer_gui.py
```

---

### Folder Selection Version

```bash
python file_organizer_select_folder.py
```

---

### Basic Version

```bash
python file_organizer.py
```

---

## 🚀 How to Use

1. Launch the application.
2. Click **Browse**.
3. Select the folder you want to organize.
4. Click **Organize Files**.
5. The application automatically creates folders for each category.
6. Files are moved into their respective folders.
7. A success message is displayed after completion.

---

## 📌 Supported File Types

### Documents

- PDF
- DOC
- DOCX
- TXT
- PPT
- PPTX
- XLS
- XLSX

### Images

- JPG
- JPEG
- PNG
- GIF
- BMP
- WEBP

### Videos

- MP4
- AVI
- MKV
- MOV
- WMV

### Audio

- MP3
- WAV
- AAC
- FLAC

### Archives

- ZIP
- RAR
- 7Z
- TAR
- GZ

### Programs

- EXE
- MSI
- BAT

---

## 🖥️ Example

### Before Organizing

```
Downloads/
│
├── image.jpg
├── report.pdf
├── song.mp3
├── movie.mp4
├── setup.exe
```

### After Organizing

```
Downloads/
│
├── Images/
│   └── image.jpg
│
├── Documents/
│   └── report.pdf
│
├── Audio/
│   └── song.mp3
│
├── Videos/
│   └── movie.mp4
│
└── Programs/
    └── setup.exe
```

---

## 💡 Future Improvements

- Dark mode
- Drag-and-drop support
- Progress bar
- Duplicate file detection
- Undo operation
- Custom file categories
- Logging system
- Settings window
- Multi-threading for large folders
- Statistics dashboard

---

## 🐞 Known Limitations

- Does not detect duplicate files.
- Existing files with the same name may require manual handling.
- Limited to predefined file categories.
- Organizes only the selected folder.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

**Mohammed Nouman**

Computer Science Engineering Student

---

## ⭐ If you found this project useful, consider giving it a star!
=======
---

## 🚀 Features

* Organizes any selected folder (not limited to Downloads)
* Automatically creates category folders if missing
* Moves files based on their extensions
* Handles all common formats for documents, images, videos, scripts, etc.
* Places unidentified files in an `Others` folder
* Lightweight, fast, and very easy to use
* Fully customizable file-type categories

---

## 🖥️ How It Works

1.  Run the Python script.
2.  Enter the path of the folder you want to organize.
3.  The tool scans the folder.
4.  It automatically sorts files into proper sub-folders.
5.  Finally, it displays a summary of moved files.

---

## 📂 Example

### Folder Before

```bash
Downloads/
├── photo.jpg
├── resume.pdf
├── video.mp4
├── script.py
├── notes.txt
├── setup.exe
└── image2.png
Folder After
Bash

Downloads/
├── Images/
│   ├── photo.jpg
│   └── image2.png
├── Documents/
│   ├── resume.pdf
│   └── notes.txt
├── Videos/
│   └── video.mp4
├── Programs/
│   └── setup.exe
├── Scripts/
│   └── script.py
├── Music/
├── Compressed/
└── Others/

```
## 🔧 Technologies Used

* Python 3
* `os` module
* `shutil` module

---
```
```
## 📌 Future Enhancements

* Windows `.exe` application version
* Graphical Interface (GUI)
* Logging and reporting
* Custom category creator
* Drag-and-drop support

---
```
```
## 📜 Author

**Mohammed Nouman**
* Computer Science Engineering Student
* Organized_Files Project – 2025
```
