import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

pdf_files = "data/"
documents = []

for filename in os.listdir(pdf_files):
    if filename.lower().endswith(".pdf"):
        file_path = os.path.join(pdf_files, filename)
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        documents.extend(docs)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
split_docs = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = FAISS.from_documents(split_docs, embeddings)
vectorstore.save_local("faiss_index")

print(f"done index. total chunks : {len(split_docs)}")