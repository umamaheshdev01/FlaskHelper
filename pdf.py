import os
import requests
from PyPDF2 import PdfReader
from winow import similarity_score

def download_pdf(url, local_path):
    response = requests.get(url)
    with open(local_path, 'wb') as file:
        file.write(response.content)

def read_pdf(path):
    text = ''
    pdf_reader = PdfReader(path)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def compare(pdf1,pdf2):
    download_pdf(pdf1,"./fake1.pdf")
    download_pdf(pdf2,"./fake2.pdf")

    data1=read_pdf("./fake1.pdf")
    data2=read_pdf("./fake2.pdf")

    return similarity_score(data1,data2)





