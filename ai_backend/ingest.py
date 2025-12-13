from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

DATA_DIR = "data/library"
DB_DIR = "chroma_db"

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

docs = []
for f in os.listdir(DATA_DIR):
    docs += TextLoader(os.path.join(DATA_DIR, f)).load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)

Chroma.from_documents(chunks, embeddings, persist_directory=DB_DIR)
print("✅ E-Library indexed successfully")
