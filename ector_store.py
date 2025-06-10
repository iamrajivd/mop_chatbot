from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

def index_documents(text):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = [Document(page_content=chunk) for chunk in splitter.split_text(text)]
    db = FAISS.from_documents(docs, OpenAIEmbeddings())
    return db
