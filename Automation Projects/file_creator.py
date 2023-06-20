import os

path = "/Users/namyashah/Codes/Python-Codes/Break the Ice/"


for file in range(10, 104):
    file_name = f"{file}.py"
    file_path = os.path.join(path, file_name)


print("Program executed...")
