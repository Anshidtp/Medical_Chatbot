import os
from pathlib import Path
import logging
 

logging.basicConfig(level = logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "store_index.py",
    "Templates/index.html",
    "static/css1.css"
    ""
]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir, file_name = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory : {filedir} for the {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,'w') as f:
            pass
            logging.info(f"creating empty file : {file_path}")

    else:
        logging.info(f"{file_name} is already created")