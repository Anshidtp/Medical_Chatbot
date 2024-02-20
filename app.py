from flask import Flask,render_template, request,jsonify
from src.helper import Download_embedding_model
from langchain.vectorstores import Pinecone
import pinecone
from langchain.llms import CTransformers
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
import os
from src.prompt import *
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

embedding_model = Download_embedding_model()

# Initializing the Pinecone
pinecone.init(api_key=PINECONE_API_KEY,
              environment=PINECONE_API_ENV)
index_name = "medical-chatbot"

#loading the index
docsearch = Pinecone.from_existing_index(index_name=index_name,
                                         embedding=embedding_model)

Prompt = PromptTemplate(template=template,
                        input_variables=["context","question"])
chain_type_kwargs = {"prompt": Prompt}

# Model llama2 Loading 
llm = CTransformers(model="model\llama-2-7b-chat.ggmlv3.q4_0.bin",
                    model_type="llama",
                    config={'max_new_tokens':512,
                            'temperature':0.8})

QnA = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever = docsearch.as_retriever(search_kwargs={'k':2}),
    return_source_documents = True,
    chain_type_kwargs=chain_type_kwargs
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['GET','POST'])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result = QnA({"query":input})
    print("Response:", result['result'])
    return str(result['result'])


if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=8080 , debug=True)


