from pypdf import PdfWriter

import os

pdf_directory="Tomerge" # wite the folder name where all pdfs file are present 

merger = PdfWriter()

files = [os.path.join(pdf_directory, file) for file in os.listdir(pdf_directory) if file.endswith(".pdf")]
for pdf in files:
    merger.append(pdf)
output_file = "merged-pdf.pdf"
merger.write(output_file)

merger.close()