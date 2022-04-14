
# pdf = p.PdfFileReader("Ansible.pdf")

# importing required modules
import PyPDF2
 
# creating a pdf file object
pdfFileObj = open('Resume.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
print(pdfReader.numPages)
 
# # creating a page object
pageObj = pdfReader.getPage(0)
 
# # # extracting text from page
text = pageObj.extractText()
print(text)
 
# # closing the pdf file object
# pdfFileObj.close()


for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    text = pageObj.extractText()
    print(text)
    