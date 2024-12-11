import setuptools

#with open("README.md", 'r', encoding="utf-8") as f:
 #   long_description = f.read()

#__version__ ="0.0.0"

#REPO_NAME ="chicken-diseases-classification"
#AUTHOR_USER_NAME ="CSEAryan"
#SRC_REPO = "chicken_diseases_classification"
#AUTHOR_EMAIL = "dipuaryan1111@gmail.com"

#setuptools.setup(
#    name =SRC_REPO,
#    version=__version__,
#    author=AUTHOR_USER_NAME,
#    author_email=AUTHOR_EMAIL,
#    description="A small python package for CNN app",
#    long_description=long_description,
#    long_description_content="text/markdown",
#    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
#    project_urls ={
#        "Bug Tracker" :f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
#    },
#    package_dir={"": "src"},
#    packages=setuptools.find_packages(where="src")
#)
from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT ='-e .'

#defining a function
def get_requirements(file_path:str)->List[str]:
    '''
    this function will retirn the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='chicken_diseases_classification',
    version='0.0.1',
    author='Aryan',
    author_email ='dipuaryan1111@gmail.com',
    # yesle init.py ka xa vanerw khojera import garxa
    packages=find_packages(), 
    install_requires =get_requirements('requirements.txt')
)