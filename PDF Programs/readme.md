# PDF Programs

This readme provides an overview of the three Python code files that work with PDF files.

## File 1: PDF Encryption

This code encrypts a PDF file with a password.

1. Importing Required Modules:
   - Install the `PyPDF2` library if not already installed.
   - Import the necessary modules:
     ```python
     from PyPDF2 import PdfFileWriter, PdfFileReader
     import getpass
     ```

2. File Encryption:
   - Specify the PDF file you want to encrypt by providing its filename in the line `pdf = PdfFileReader("")`.
   - Enter the password for encryption when prompted using `getpass.getpass(prompt="Enter Password: ")`.
   - The encrypted PDF will be saved as "ho.pdf" in the same directory.

## File 2: PDF Merger

This code merges multiple PDF files into a single PDF file.

1. Importing Required Modules:
   - Import the `PyPDF2` module:
     ```python
     import PyPDF2
     ```

2. File Merging:
   - Specify the filenames of the PDF files you want to merge by adding them to the `pdfiles` list.
   - The merged PDF file will be saved as "merged.pdf" in the same directory.

## File 3: PDF Text Extraction

This code extracts text from a PDF file.

1. Importing Required Modules:
   - Install the `pyPDF2` library if not already installed.
   - Import the necessary module:
     ```python
     from pyPDF2 import PdfReader
     ```

2. Text Extraction:
   - Specify the PDF file from which you want to extract text by providing its filename in the line `reader = PdfReader("")`.
   - The code extracts text from the first page of the PDF and prints it.

## Usage and Notes:
- Replace the empty strings in the code with the appropriate filenames or paths of the PDF files you want to work with.
- Ensure that the required modules (`PyPDF2`, `getpass`, `pyPDF2`) are installed before running the code.
- These code snippets demonstrate basic functionality and can be customized to suit specific requirements.
- Make sure the code files and the PDF files are in the same directory or provide the full file paths as necessary.
- Note that the code examples assume that the PDF files exist and are accessible.

Feel free to modify the code based on your specific needs and explore additional features and functionalities provided by the respective libraries. Enjoy working with PDF files in Python!