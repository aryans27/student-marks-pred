from setuptools import find_packages, setup     # setuptools used for packaging Python projects
from typing import List

HYP_E_DOT = '-e .'

def get_requirements(filePath: str) -> List[str]:
    '''
    Gets the requirements for this project and returns a list of them.
    '''
    with open(filePath, 'r') as file:       
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]      # Strips the newline characters from each line.
        if HYP_E_DOT in requirements:
            requirements.remove(HYP_E_DOT)
    return requirements

setup(          # meta-data for the project 
    name='ML-ETE-Project',
    version='0.1.2',
    author='Sakshit',
    author_email='sakshitaryan@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
