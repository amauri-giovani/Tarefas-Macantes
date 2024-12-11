# -*- coding: utf-8 -*-

import sys
import PyPDF2

def convertPdf2String(path):
    content = ""
    # load PDF file
    pdf = PyPDF2.PdfFileReader(path, "rb")
    # iterate pages
    for i in range(0, pdf.getNumPages()):
        # extract the text from each page
        content += pdf.getPage(i).extractText() + " \n"
    # collapse whitespaces
    content = u" ".join(content.replace(u"\xa0", u" ").strip().split())
    return content

# convert contents of a PDF file and store retult to TXT file
f = open('a.txt','w+')
f.write(convertPdf2String(sys.argv[1]))
f.close()

# or print contents to the standard out stream