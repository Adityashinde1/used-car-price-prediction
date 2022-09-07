from setuptools import setup, find_packages
from typing import List


def get_requirements_list() -> List[str]:

    """
    Description: This function is going to return list of requirements
    mentioned in the requirements.txt file

    return this function is going to return a list which containes name 
    of libraries mentioned in requirements.txt file
    """
    with open("requirements.txt") as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name = "used-car-price-prediction",
version = "0.2",
author = "Aditya Shinde",
description = "With this project you can predict the used car prices",
packages = find_packages(),
install_requires = get_requirements_list()

)


