#this is the template that can be used in each and every ml project
import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s')

project_name = "chicken-diseases-classification"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "template/index.html"
    

]

#traveling through list
for filepath in list_of_files:
    filepath = Path(filepath)
    #ssesperating file and folders since it will return filename and folder
    filedir, filename = os.path.split(filepath)
    #if filedir is not empty the create the folder
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file :{filename}")

    #checeking the file exist or not and also the file size 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file:{filepath}")

    else:
        logging.info(f"{filename} already exist")

