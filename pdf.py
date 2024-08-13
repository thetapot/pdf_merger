import PyPDF2
import sys

# adding watermark to pdf
# template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()

# for i in range(template.getNumPages()):
#     page = template.getPage(i)
#     page.mergePage(watermark.getPage(0))
#     output.addPage(page)

# output.write(open('watermarked_pd.pdf', 'wb'))


# merge all pdfs into one
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write("super.pdf")

# list = sys.argv[1:]
# pdf_combiner(list)

# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)

# Bonus Rotate super.pdf counterclock wise 90°
# reader = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# writer = PyPDF2.PdfFileWriter()
# for i in range(reader.getNumPages()):
#     page = reader.getPage(i)
#     page.rotateCounterClockwise(90)
#     writer.addPage(page)
# writer.write(open('super_90_degree.pdf', 'wb'))