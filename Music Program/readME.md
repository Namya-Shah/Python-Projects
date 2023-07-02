# Music Player

This code provides a simple music player application using the Tkinter library in Python. It allows you to play random music files from a specified directory.

## Prerequisites

- Python 3.x installed on your system
- Tkinter library installed (usually included with Python installations)
- Music files stored in a directory

## Getting Started

1. Ensure that you have the necessary prerequisites installed.
2. Download the code and save it to a Python file, e.g., `music_player.py`.
3. Modify the `path` variable in the code to the directory where your music files are stored.
4. Run the code using the command `python music_player.py`.

## Usage

1. Upon running the code, a graphical window will appear with the title "Music Program".
2. Below the title, you will see the secondary title instructing you to click the button to start playing music.
3. Click the "Play Music!" button to randomly select a music file from the specified directory and play it.
4. The selected music file's full path will be printed in the console.

## Customization

- You can modify the code to change the appearance of the user interface by modifying the colors, fonts, and sizes in the `styles.py` file.
- If you want to change the default path to your music directory, update the `path` variable in the code to the desired directory.

## Dependencies

The code relies on the following libraries:

- `tkinter`: The standard Python interface to the Tk GUI toolkit.
- `os`: Provides functions for interacting with the operating system.
- `subprocess`: Enables the creation of new processes and the execution of external commands.
- `random`: Used for randomly selecting a music file from the directory.

## Note

- This code is a simple implementation and may not support all types of music files or handle certain exceptions.
