#building application as a package
from setuptools import find_packages,setup
from typing import List
hy_e='-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hy_e in requirements:
            requirements.remove(hy_e)
    return requirements

setup(
name="SaiMLprojects",
version='0.0.1',
author="Sai Jagadeesh",
author_email="ysaijagadeeshuh@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)