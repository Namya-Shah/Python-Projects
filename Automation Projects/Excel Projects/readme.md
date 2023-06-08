# Extracting Sheets

This code is designed to extract numbers from a specific sheet of an Excel workbook and create a new workbook with the extracted numbers distributed across multiple sheets.

## Setup

Before running the code, ensure that you have the following requirements:

- Python: The code is written in Python, so make sure you have Python installed on your system.
- openpyxl: The `openpyxl` library is used to interact with Excel files. Install it using the following command: `pip install openpyxl`.

## Usage

1. Replace the empty strings in the code with the appropriate filenames:
   - In the line `workbook = openpyxl.load_workbook('')`, specify the filename of the workbook from which you want to extract sheets.
   - In the line `new_workbook.save('')`, specify the filename to which you want to save the new workbook.

2. Identify the desired sheet number:
   - In the line `sheet_number = 7`, update the `sheet_number` variable with the desired sheet number you want to extract from the workbook. Note that the sheet numbering starts from 1.

3. Running the code:
   - Execute the code, and it will perform the following steps:
     - Load the specified workbook.
     - Select the desired sheet based on the sheet number provided.
     - Extract the numbers from the selected sheet.
     - Create a new workbook using `openpyxl`.
     - Iterate over the extracted numbers and create new sheets in the new workbook.
     - Write the extracted numbers to the new sheets.
     - Save the new workbook with the specified filename.

4. Result:
   - After the code execution completes, a new workbook will be created with the extracted numbers distributed across multiple sheets. Each sheet will contain up to 20 numbers.

Feel free to customize the code based on your specific requirements. You can modify the code to extract different data or adjust the number of numbers per sheet. Enjoy working with Excel files using Python!