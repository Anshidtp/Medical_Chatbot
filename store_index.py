from src.helper import load_pdf, chunk_split, Download_embedding_model 
import pinecone
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv
load_dotenv() # initializing all packages
import os


PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')



extracted_data = load_pdf("Dataset/")
text_chunks = chunk_split(extracted_data)
embedding_model = Download_embedding_model()

# Initializing the Pinecone
pinecone.init(api_key=PINECONE_API_KEY,
              environment=PINECONE_API_ENV)
index_name = "medical-chatbot"

#Creating embedding for each of text_chunks & storing
docsearch = Pinecone.from_texts([t.page_content for t in text_chunks], 
                                embedding=embedding_model,
                                index_name=index_name)