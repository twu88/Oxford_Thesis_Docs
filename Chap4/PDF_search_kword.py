#!/usr/bin/env python
import PyPDF2
import re
import glob

# Extract text and do the search writes to text file and prints the name of file and page number keyword is found
def pdf_textfinder(xFile,xString):
    pdfDoc = PyPDF2.PdfFileReader(xFile, "rb")
    f = open("results.txt", 'a')
    for i in range(0, pdfDoc.getNumPages()):
        PageObj = pdfDoc.getPage(i)
        Text = PageObj.extractText()
        if re.search(xString, Text) is not None:
            f.write('pdfFile \n' + "Pattern Found on Page: " + '\n' + str(i) + '\n')
            print("Pattern Found on Page: " + str(i))
        else:
            break

for pdfFile in glob.glob("*.pdf"):
    print(pdfFile)
   #String = ['tool', 'people']
    pdf_textfinder(pdfFile, 'tool')
