import PyPDF2

text = open("dictionary.txt")
text = text.read()
text = text.split("\n")

pdf = open("beginners_python_cheat_sheet_pcc_all_decrypted.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf)
pdf_writer = PyPDF2.PdfFileWriter()

for word in text:
    print(f"Trying to break in with {word}...")
    try:
        if pdf_reader.decrypt(word) == 1:
            print(f"Congratulations! The password was {word}!")
            break
        elif pdf_reader.decrypt(word.lower()) == 1:
            print(f"Congratulations! The password was {word}!")
            break
    except:
        print("Could not determine the password.")

for num_page in range(pdf_reader.numPages):
    page_obj = pdf_reader.getPage(num_page)
    pdf_writer.addPage(page_obj)

new_pdf = open("password_broken.pdf", "wb")
pdf_writer.write(new_pdf)
new_pdf.close()
pdf.close()
