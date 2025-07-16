import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


pygame.mixer.init()


def choose_file():
    global filename
    filename = filedialog.askopenfilename(
        title="select a music file",
        filetypes=[("mp3 files", "*.mp3 *.wav *.ogg"), ("all files", "*.*")]
    )
    if filename:
        status_var.set(f"Selected:{filename.split('/')[-1]}")


def play_music():
    if filename:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def pause_music():
    pygame.mixer.music.pause()


def unpause_music():
    pygame.mixer.music.unpause()


root = tk.Tk()
root.title("music player")
root.geometry("500x300")
root.configure(bg="#978")

status_var = tk.StringVar()
status_var.set('no file selected')

# وضعیت فایل انتخاب شده
status_label = ttk.Label(root, textvariable=status_var, font=('Helvetica', 10))
status_label.pack(side=tk.TOP, pady=90)


# فریم کنترل در پایین صفحه با فاصله مناسب
control_frame = ttk.Frame(root)
control_frame.pack(side=tk.BOTTOM, pady=20)  # فاصله پایین 20 پیکسلی

# دکمه انتخاب فایل
choose_btn = ttk.Button(control_frame, text='Choose File', command=choose_file)
choose_btn.pack(side=tk.LEFT, padx=5)


# دکمه‌های کنترل درون فریم
play_btn = ttk.Button(control_frame, text="▶️ Play", command=play_music)
play_btn.pack(side=tk.LEFT, padx=5)

stop_btn = ttk.Button(control_frame, text="⏹️ Stop", command=stop_music)
stop_btn.pack(side=tk.LEFT, padx=5)

pause_btn = ttk.Button(control_frame, text="⏸️ Pause", command=pause_music)
pause_btn.pack(side=tk.LEFT, padx=5)

resume_btn = ttk.Button(control_frame, text="⏯️ resume", command=unpause_music)
resume_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()
