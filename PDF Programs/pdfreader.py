from pyPDF2 import PdfReader

reader = PdfReader("")  # Enter PDF File you want to read
page = reader.pages[0]
print(page.extract_text())
