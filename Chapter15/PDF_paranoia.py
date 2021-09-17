#! python3

import PyPDF2
import os
import re
import sys

password = sys.argv[1]

os.chdir(r"C:\Users\Ozgur2\Desktop\pdfs_to_encrypt")
path = os.getcwd()

for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith((".pdf", ".PDF")):
            print(f"Encrypting {file}...")
            pdf = open(os.path.join(folder, file), "rb")
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.encrypt(sys.argv[1])

            for page_num in range(pdf_reader.numPages):
                page_obj = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page_obj)

            file = re.sub(".pdf", "", file)
            new_pdf = open(os.path.join(folder, file + "_encrypted.pdf"), "wb")
            pdf_writer.write(new_pdf)
            pdf.close()
            new_pdf.close()

for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith("encrypted.pdf"):
            pdf = open(os.path.join(folder, file), "rb")
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            try:
                page_obj = pdf_reader.getPage(0)
            except PyPDF2.utils.PdfReadError:
                file = re.sub("_encrypted.pdf", "", file)
                print("Deleting %s..." % (os.path.join(folder, file)))
                os.remove(os.path.join(folder, file + ".pdf"))

print("Finished.")
