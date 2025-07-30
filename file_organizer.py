import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Archives': ['.zip', '.rar'],
    'Music': ['.mp3', '.wav']
}


def organize_files(folder, output_widget):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in file_types.items():
                if ext in extensions:
                    target_dir = os.path.join(folder, category)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_dir, filename))
                    output_widget.insert(tk.END, f"✅ Moved: {filename} → {category}\n")
                    moved = True
                    break
            if not moved:
                output_widget.insert(tk.END, f"⚠️ Skipped: {filename} (no match)\n")


def open_gui():
    def choose_folder():
        path = filedialog.askdirectory()
        if path:
            folder_path.set(path)

    def run_organizer():
        folder = folder_path.get()
        if not folder or not os.path.isdir(folder):
            messagebox.showerror("خطا", "لطفاً یک پوشه‌ی معتبر انتخاب کنید.")
            return
        output_box.delete('1.0', tk.END)  # پاک‌کردن خروجی قبلی
        organize_files(folder, output_box)

    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("500x400")

    folder_path = tk.StringVar()

    tk.Label(root, text="مسیر پوشه:").pack(pady=5)
    tk.Entry(root, textvariable=folder_path, width=50).pack(pady=5)
    tk.Button(root, text="📁 انتخاب پوشه", command=choose_folder).pack(pady=5)
    tk.Button(root, text="🚀 مرتب‌سازی فایل‌ها", command=run_organizer).pack(pady=10)

    output_box = scrolledtext.ScrolledText(root, width=60, height=15)
    output_box.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    open_gui()
