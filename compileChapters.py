import extractText
import os

file = 'report2.pdf'
rawText =  extractText.pdfToText(file).replace('\n \n \n','\n').replace('\n \n',' ').replace('�','')

print(rawText)

