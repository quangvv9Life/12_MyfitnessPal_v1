# from PyPDF2 import PdfFileReader

# with open('VTN_FCT_2007.pdf', 'rb') as f:
#     reader = PdfFileReader(f)
#     contents = reader.getPage(1).extractText().split('\n')
#     pass


# pdf_file = open('VTN_FCT_2007.pdf', 'rb')
# read_pdf = PdfFileReader(pdf_file)
# number_of_pages = read_pdf.getNumPages()

# print(number_of_pages)

# page_content = read_pdf.getPage(1).extractText()

# print(page_content)
# print (page_content.encode('utf-8','strict'))

from camelot import read_pdf

pdf_file = 'VTN_FCT_2007.pdf'

tables = read_pdf('VTN_FCT_2007.pdf')

print(tables[20].df)