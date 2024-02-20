from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings


# Extract data from pdf

def load_pdf(data):
    loader = DirectoryLoader(data,
                    glob="*.pdf",
                    loader_cls=PyPDFLoader)
    
    documents = loader.load()

    return documents


# Create text chunks for extracted data

def chunk_split(extracted_data):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500 , chunk_overlap = 20)
    chunks = splitter.split_documents(extracted_data)

    return chunks


# Download_embedding model

def Download_embedding_model():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding
