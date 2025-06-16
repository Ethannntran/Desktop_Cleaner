# Desktop_Cleaner_App

Python Project - Desktop Cleaner

Wanted to share a script I’ve put together to help organizing files from any folder locally on your system. Here's where to download it.
 
🗂 What it Does:
- This Python script provides a simple desktop GUI that lets you select any folder and automatically sorts its files into categorized folders — Audio, Video, Images, Documents, and Others — all created on your desktop.
 
🔍 How it Works:
- After selecting a folder via the interface, the script goes through the files and organizes them based on their file extensions.
- It creates the necessary folders on your desktop, then sorts the files into these newly created folders
- If a file doesn’t match any predefined category, it gets moved to a catch-all “Others” folder.
- It also prevents file name collisions by renaming duplicates automatically.

🧰 Tech Stack:
- Built using Python’s standard libraries: os, shutil, and tkinter (no external dependencies).
- Cross-platform compatible (works on both Windows and macOS/Linux).
- If you download it for MacOs or Linux, unzip "Desktop_Cleaner.zip" from the provided link, and follow these steps: 
   - Go to System Settings < Privacy and Security < Allow the .app to run
- if you download for Windows, "Desktop_cleaner.exe", simply just run it. 

📋 Extras:
- There’s a live activity log in the app window showing which files were moved and where.
- It's a lightweight tool ideal for cleaning up messy folders like Downloads.
- I’ve provided the full source code along with the script. Feel free to review it before running — it's all plain Python, no external dependencies, and easy to follow
