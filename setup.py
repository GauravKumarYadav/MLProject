from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(path : str) ->List[str]:
    '''
        This function will read the requirements.txt file and return a list of packages for installation
    '''
    requirements = []
    with open(path) as f:
        requirements =  f.readlines()
        requirements = [req.replace("\n"," ") for req in requirements if req != HYPEN_E_DOT]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='gaurav',
    author_email='gauravy60@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)