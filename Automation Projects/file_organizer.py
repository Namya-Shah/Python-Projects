import os
import shutil

videos_folder = "Videos" # Enter path where you want to save video files
excel_folder = "Excels" # Enter path where you want to save excel files
pdf_folder = "PDFs" # Enter path where you want to save pdf files
apps_folder = "Apps" # Enter path where you want to save apps files
images_folder = "Images" # Enter path where you want to save images files
zip_folder = "Zips" # Enter path where you want to save zip files
ppt_folder = "PPTs" # Enter path where you want to save ppt files
word_folder = "Words" # Enter path where you want to save word files

os.chdir("") # Enter the directory which you want to organize
dir = os.listdir()
print(dir)

if os.path.exists(videos_folder):
    print("Folder exists.") # Comment this code if you don't want "Folder exists." to print in the terminal
else:   
    os.mkdir("Videos")

if os.path.exists(excel_folder):    
    print("Folder exists.") # Comment this code if you don't want "Folder exists." to print in the terminal
else:   
    os.mkdir("Excels")

if os.path.exists(pdf_folder):  
    print("Folder exists.") # Comment this code if you don't want "Folder exists." to print in the terminal
else:   
    os.mkdir("PDFs")

if os.path.exists(apps_folder): 
    print("Folder exists.") # Comment this code if you don't want "Folder exists." to print in the terminal
else:   
    os.mkdir("Apps")

if os.path.exists(images_folder):   
     print("Folder exists.") # Comment this code if you don't want "Folder exists." to print in the terminal
else:   
    os.mkdir("Images")

if os.path.exists(zip_folder):  
    print("Folder exists.") # Comment this code if you don't want "Folder exists." to print in the terminal
else:
    os.mkdir("Zips")

if os.path.exists(ppt_folder):
    print("Folder exists.") # Comment this code if you don't want "Folder exists." to print in the terminal
else:
    os.mkdir("PPTs")

if os.path.exists(word_folder):
    print("Folder exists.") # Comment this code if you don't want "Folder exists." to print in the terminal
else:
    os.mkdir("Words")
for file in dir:
    if file.endswith(".xlsx") or file.endswith(".csv"):
        shutil.move(f"{file}", "") # Enter the destination path
    elif file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".gif") or file.endswith(".webm"):
        shutil.move(f"{file}", "") # Enter the destination path
    elif file.endswith(".pdf"):
        shutil.move(f"{file}", "") # Enter the destination path
    elif file.endswith(".dmg"):
        shutil.move(f"{file}", "") # Enter the destination path
    elif file.endswith(".zip"):
        shutil.move(f"{file}", "") # Enter the destination path
    elif file.endswith(".ppt") or file.endswith(".pptx"):
        shutil.move(f"{file}", "") # Enter the destination path
    elif file.endswith(".docx") or file.endswith(".doc"):
        shutil.move(f"{file}", "") # Enter the destination path
    elif file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".webp"):
        shutil.move(f"{file}", "") # Enter the destination path

print("Program executed...")