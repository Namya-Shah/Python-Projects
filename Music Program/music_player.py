from tkinter import *
from styles import *
import os
import subprocess
import random

path = "/Users/namyashah/Downloads/Music"


def get_music_files():
    files = os.listdir(path)
    return files


def run_music():
    music_files = get_music_files()
    shuffled_music = random.choice(music_files)
    shuffled_music_full_path = os.path.join(path, shuffled_music)
    subprocess.call(["open", shuffled_music_full_path])
    print(shuffled_music_full_path)


root = Tk()
root.configure(bg=blue)
root.geometry("480x320")

title = Label(root, text="Music Program",
              fg=yellow, bg=blue, font=(font_type, 36)
              )

title.pack()

secondary_title = Label(root, text="Click the button to start playing music",
                        fg=yellow, bg=blue, font=(font_type, 18)
                        )

secondary_title.pack()

run_music_button = Button(root, text="Play Music!", command=run_music, fg=yellow, bg=blue, font=(font_type, 18))

run_music_button.pack(side=BOTTOM)
root.mainloop()

