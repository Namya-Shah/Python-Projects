import os
import shutil
from path import path

videos_folder = "Videos"  # Enter path where you want to save video files
excel_folder = "Excels"  # Enter path where you want to save excel files
pdf_folder = "PDFs"  # Enter path where you want to save pdf files
apps_folder = "Apps"  # Enter path where you want to save apps files
images_folder = "Images"  # Enter path where you want to save images files
zip_folder = "Zips"  # Enter path where you want to save zip files
ppt_folder = "PPTs"  # Enter path where you want to save ppt files
word_folder = "Words"  # Enter path where you want to save word files
code_folder = "Codes" # Path where codes will be saved
python_folder = "Python"  # Enter path where you want to save python files
javascript_folder = "JavaScript" # Enter path where you want to save javascript files
java_folder = "Java"  # Enter path where you want to save java files
sql_folder = "SQL" # Path where SQL files will be saved

# Enter the directory which you want to organize
os.chdir(path)
dir = os.listdir()
print(dir)

if os.path.exists(videos_folder):
    # Comment this code if you don't want "Folder exists." to print in the terminal
    #print("Folder exists.")
    pass
else:
    os.mkdir("Videos")

if os.path.exists(excel_folder):
    # Comment this code if you don't want "Folder exists." to print in the terminal
    #print("Folder exists.")
    pass
else:
    os.mkdir("Excels")

if os.path.exists(pdf_folder):
    # Comment this code if you don't want "Folder exists." to print in the terminal
    #print("Folder exists.")
    pass
else:
    os.mkdir("PDFs")

if os.path.exists(apps_folder):
    # Comment this code if you don't want "Folder exists." to print in the terminal
    #print("Folder exists.")
    pass
else:
    os.mkdir("Apps")

if os.path.exists(images_folder):
    # Comment this code if you don't want "Folder exists." to print in the terminal
    #print("Folder exists.")
    pass
else:
    os.mkdir("Images")

if os.path.exists(zip_folder):
    # Comment this code if you don't want "Folder exists." to print in the terminal
    #print("Folder exists.")
    pass
else:
    os.mkdir("Zips")

if os.path.exists(ppt_folder):
    # Comment this code if you don't want "Folder exists." to print in the terminal
    #print("Folder exists.")
    pass
else:
    os.mkdir("PPTs")

if os.path.exists(word_folder):
    # Comment this code if you don't want "Folder exists." to print in the terminal
    #print("Folder exists.")
    pass
else:
    os.mkdir("Words")

if os.path.exists(code_folder):
    #print("Folder exists.")
    pass
else:
    os.mkdir("Codes")
    os.chdir(path+"Codes")
    if os.path.exists(python_folder):
        #print("Folder exists.")
        pass
    else:
        os.mkdir("Python")
    if os.path.exists(java_folder):
        #print("Folder exists.")
        pass
    else:
        os.mkdir("Java")
    if os.path.exists(javascript_folder):
        #print("Folder exists.")
        pass
    else:
        os.mkdir("JavaScript")
    if os.path.exists(sql_folder):
        #print("Folder exists.")
        pass
    else:
        os.mkdir("SQL")

for file in dir:
    if file.endswith(".xlsx") or file.endswith(".csv"):
        shutil.move(
            file, path+"Excels/"
        )  # Enter the destination path
    elif (
        file.endswith(".mp4")
        or file.endswith(".mkv")
        or file.endswith(".gif")
        or file.endswith(".webm")
    ):
        shutil.move(
            file, path+"Videos/"
        )  # Enter the destination path
    elif file.endswith(".pdf"):
        shutil.move(
            file, path+"PDFs/"
        )  # Enter the destination path
    elif file.endswith(".dmg"):
        shutil.move(
            file, path+"Apps/"
        )  # Enter the destination path
    elif file.endswith(".zip"):
        shutil.move(
            file, path+"Zips/"
        )  # Enter the destination path
    elif file.endswith(".ppt") or file.endswith(".pptx"):
        shutil.move(
            file, path+"PPTs/"
        )  # Enter the destination path
    elif file.endswith(".docx") or file.endswith(".doc"):
        shutil.move(
            file, path+"Words/"
        )  # Enter the destination path
    elif (
        file.endswith(".jpg")
        or file.endswith(".png")
        or file.endswith(".jpeg")
        or file.endswith(".webp")
    ):
        shutil.move(
            file, path+"Images/"
        )  # Enter the destination path
    elif file.endswith(".py"):
        shutil.move(file, path+"Codes/Python")
    elif file.endswith(".java"):
        shutil.move(file, path+"Codes/Java")
    elif file.endswith(".js"):
        shutil.move(file, path+"Codes/JavaScript")
    elif file.endswith(".sql"):
        shutil.move(file, path+"Codes/SQL")

print("Program executed...")
