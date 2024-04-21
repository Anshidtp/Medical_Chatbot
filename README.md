# Medical_Chatbot -MediChat

### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone


## STEPS TO RUN :

### STEP 01- Clone the Repository

```bash
Project repo: https://github.com/
```

### STEP 02- Create a conda environment after opening the repository

```bash
conda create -n <env_name> python=3.8 -y
```

```bash
conda activate <env_name>
```

### STEP 03- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### STEP 04- Run the following Commands
```bash
python store_index.py
```

```bash
python app.py
```

Now,
```bash
open up localhost:
```


