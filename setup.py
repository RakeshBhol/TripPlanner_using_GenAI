"""
Description: It will create a python installer like .exe or .tar file.

setup.py naming is required, so that it can picked up by setuptools module.

For local test run command "pip install .", it will create a module
"""
from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_list: List[str] = []

    try:
        # Open and read the requirements.txt
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                # strip white space and newline characters
                requirements = line.strip()
                # ignore empty lines and -e .
                if requirements and requirements != '-e .':
                    requirement_list.append(requirements)
    except FileNotFoundError:
        print('requirements.txt file not found.')
    
    return requirement_list

print(get_requirements())

'''Meta deta needed for setup()'''
setup(
    name = 'GENAI-TRAVEL-PLANNER',
    description='It ',
    version = '0.0.1',
    author = 'Rakesh Bhol',
    author_email ='rkbhol1101@gmail.com',
    packages = find_packages(),  # It will bundle all self created files and packages
    install_requires = get_requirements()  # dependency need to include from requirements.txt
)