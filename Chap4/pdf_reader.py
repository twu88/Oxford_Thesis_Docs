#!/usr/bin/env python
import PyPDF2

import re
import glob
import os


#your full path of directory
# mypath = "dir"
# for file in os.listdir(os.curdir):
#     print(file)
#     if file.endswith('.pdf'):
#         fileReader = PyPDF2.PdfFileReader(open(file, "rb"))
#         count = 0
#         count = fileReader.numPages
#         while count >= 0:
#             count -= 1
#             pageObj = fileReader.getPage(count)
#             text = pageObj.extractText()
#             print(text)
#         num = re.findall(r'tools', text)
#         print(num)
#
#     else:
#         print("not in format")


# file = '1907.01427.pdf'
# fileReader = PyPDF2.PdfFileReader(open(file, "rb"))
# search_word = "tool"
# search_word_count = 0
# for pageNum in range(1, fileReader.numPages):
#     pageObj = fileReader.getPage(pageNum)
#     text = pageObj.extractText().encode('utf-8')
#     search_text = text.lower().split()
#     for word in search_text:
#         if search_word in word.decode("utf-8"):
#             search_word_count += 1
#
#
# print("The word {} was found {} times".format(search_word, search_word_count))


#pdfFileObj = open(r'C:\Users\Craig\RomeoAndJuliet.pdf', mode='rb')



# pages_text = []
# words_start_pos = {}
# words = {}
#
# searchwords = ['tool']
#
# for filename in glob.glob('*.pdf'):
#     pdfFileObj = open(filename, mode='rb')
#     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#     number_of_pages = pdfReader.numPages
#     with open((filename.rsplit(".", 1)[0]) + ".csv", 'w') as f:
#         f.write('{0},{1}\n'.format("Sheet Number", "Search Word"))
#         for word in searchwords:
#             for page in range(number_of_pages):
#                 print(page)
#                 pages_text.append(pdfReader.getPage(page).extractText())
#                 words_start_pos[page] = [dwg.start() for dwg in re.finditer(word, pages_text[page].lower())]
#                 words[page] = [pages_text[page][value:value + len(word)] for value in words_start_pos[page]]
#         for page in words:
#             for i in range(0, len(words[page])):
#                 if str(words[page][i]) != 'nan':
#                     print(filename)
#                     f.write('{0},{1}\n'.format(page + 1, words[page][i]))
#                     print(page, words[page][i])


from PyPDF2 import PdfFileReader, PdfFileWriter

#
# # find pages
# def findText(f, slist):
#     file = open(f, 'rb')
#     pdfDoc = PdfFileReader(file)
#     pages = []
#     for i in range(pdfDoc.getNumPages()):
#         content = pdfDoc.getPage(i).extractText().lower()
#         for s in slist:
#             if re.search(s.lower(), content) is not None:
#                 if i not in pages:
#                     pages.append(i)
#     return pages
#
# #extract pages
# def extractPage(f, fOut, pages):
#     file = open(f, 'rb')
#     output = PdfFileWriter()
#     pdfOne = PdfFileReader(file)
#     for i in pages:
#         output.addPage(pdfOne.getPage(i))
#     outputStream = open(fOut, "wb")
#     output.write(outputStream)
#     outputStream.close()
#     return
#
#
# for pdfFile in glob.glob("*.pdf"):
#     print(pdfFile)
# #    outPdfFile = pdfFile.replace(".pdf","_searched_extracted.pdf")
#     stringList = ["string1", "string2"]


#    extractPage(pdfFile, outPdfFile, findText(pdfFile, stringList))


# def fnPDF_FindText(xFile, xString):
#     # xfile : the PDF file in which to look
#     # xString : the string to look for
#     import pyPdf, re
#     PageFound = -1
#     pdfDoc = pyPdf.PdfFileReader(file(xFile, "rb"))
#     for i in range(0, pdfDoc.getNumPages()):
#         content = ""
#         content += pdfDoc.getPage(i).extractText() + "\n"
#         content1 = content.encode('ascii', 'ignore').lower()
#         ResSearch = re.search(xString, content1)
#         if ResSearch is not None:
#            PageFound = i
#            break
#            return PageFound
#
# for pdfFile in glob.glob("*.pdf"):
#     print(pdfFile)
#     String = ["tool", "Tool"]
#     findText(pdfFile, String)




# Open the pdf file
#object = PyPDF2.PdfFileReader(r"C:\TEST.pdf")

# Get number of pages
#NumPages = object.getNumPages()

# Enter code here
#String = "Enter_the_text_to_Search_here"

# Extract text and do the search
def pdf_textfinder(xFile,xString):
    pdfDoc = PyPDF2.PdfFileReader(xFile, "rb")
    f = open("hello.txt", 'w')
    for i in range(0, pdfDoc.getNumPages()):
        PageObj = pdfDoc.getPage(i)
        Text = PageObj.extractText()
        if re.search(xString, Text) is not None:
            #print(pdfFile)
            f.write(pdfFile + "Pattern Found on Page: " + str(i))
            #print("Pattern Found on Page: " + str(i))
        else:
            break

for pdfFile in glob.glob("*.pdf"):
    print(pdfFile)
    #String = ['tool', 'people']
    pdf_textfinder(pdfFile, 'r')


# Open the pdf file
# object = PyPDF2.PdfFileReader(r"1803.10147.pdf")
#
# # Get number of pages
# NumPages = object.getNumPages()
#
# # Enter code here
# String = "r"
#
# # Extract text and do the search
# for i in range(0, NumPages):
#     PageObj = object.getPage(i)
#     Text = PageObj.extractText()
#     if re.search(String, Text):
#         print("Pattern Found on Page: " + str(i))
#     else:
#         break

