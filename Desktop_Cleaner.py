import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Define file extensions
file_types = {
    "Audio": ['.mp3', '.wav', '.flac', '.aac', '.wma', '.m4a'],
    "Video": ['.mp4', '.avi', '.mov', '.mkv'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.raw', '.heic'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv', '.doc', '.ppt', '.odt'],
    "Others": []  # New category for uncategorized files
}

# Get Desktop path based on the operating system
def get_desktop_path():
    if os.name == 'nt':  # Windows
        return os.path.join(os.environ['USERPROFILE'], 'Desktop')
    else:  # macOS/Linux
        return os.path.join(os.path.expanduser('~'), 'Desktop')

desktop_path = get_desktop_path()

# Create target folders
def create_folders():
    for category in file_types:
        folder_path = os.path.join(desktop_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Move file safely
def move_file(file_path, destination_folder):
    try:
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(destination_folder, file_name)

        # Handle name collisions
        base, ext = os.path.splitext(file_name)
        counter = 1
        while os.path.exists(dest_path):
            dest_path = os.path.join(destination_folder, f"{base}_{counter}{ext}")
            counter += 1

        shutil.move(file_path, dest_path)
        return f"Moved: {file_name}"
    except Exception as e:
        return f"Error: {file_name} - {e}"

# Organize files in selected directory
def organize_files(source_dir, log_output):
    if not os.path.isdir(source_dir):
        messagebox.showerror("Error", "Invalid folder selected.")
        return

    create_folders()

    for file_name in os.listdir(source_dir):
        full_path = os.path.join(source_dir, file_name)

        if os.path.isdir(full_path):
            continue

        ext = os.path.splitext(file_name)[1].lower()
        moved = False
        for category, extensions in file_types.items():
            if ext in extensions:
                folder = os.path.join(desktop_path, category)
                result = move_file(full_path, folder)
                log_output.insert(tk.END, result + '\n')
                log_output.see(tk.END)
                moved = True
                break

        if not moved:
            # Move to "Others"
            folder = os.path.join(desktop_path, "Others")
            result = move_file(full_path, folder)
            log_output.insert(tk.END, result + ' (moved to Others)\n')
            log_output.see(tk.END)

# GUI
def start_gui():
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("600x500")

    def select_folder():
        folder = filedialog.askdirectory()
        if folder:
            folder_path.set(folder)

    def run_organizer():
        log_output.delete(1.0, tk.END)
        organize_files(folder_path.get(), log_output)

    folder_path = tk.StringVar()

    tk.Label(root, text="Select a folder to organize:").pack(pady=10)
    tk.Entry(root, textvariable=folder_path, width=50).pack()
    tk.Button(root, text="Browse", command=select_folder).pack(pady=5)
    tk.Button(root, text="Organize Files", command=run_organizer).pack(pady=10)

    log_output = scrolledtext.ScrolledText(root, width=60, height=15)
    log_output.pack(padx=10, pady=10)

    # Author & Created Information 
    author_info = "Created by: Tekzenit\n© 2025 Ethan Tran. All Rights Reserved."
    author_label = tk.Label(root, text=author_info, anchor="e")
    author_label.pack(side="bottom", fill="x", padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    start_gui()
