import csv
import re
import PyPDF2

csv_file = open("find_the_link.csv", encoding="utf-8")
csv_data = csv.reader(csv_file)
csv_lines = list(csv_data)
url = ""
for i,row in enumerate(csv_lines):
    url += row[i]
csv_file.close()
print("url is: {}".format(url))

pdf_file = open("Find_the_Phone_Number.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)
pdf_text = []
for p in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[p]
    pdf_text.append(page.extract_text())

for text in pdf_text:
    clean_text = str(text).replace("-", "").replace(" ", "").replace(".", "")
    my_re = re.search(r'\d{10}', clean_text)
    if my_re:
        the_phone = my_re.group()
        print("the phone is: {}".format(the_phone))

pdf_file.close()
