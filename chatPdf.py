import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pine import generate_embeddings,store
from pdf import download_pdf,read_pdf

def pdf_to_text(pdf):
    download_pdf(pdf,'./fake1.pdf')
    data=read_pdf("./fake1.pdf")
    return data

def get_text_chunks(text,cs=350,co=30):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=cs, chunk_overlap=co)
    chunks = text_splitter.split_text(text)
    return chunks

def make_an_store(pdf,c):
    text = pdf_to_text(pdf)
    data = get_text_chunks(text)
    print(len(data))
    store(data,str(c),{})

# make_an_store('https://www.umamaheshdev.com/Resume.pdf')











