from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Marcos Winther",
    author_email="winthermarcos@gmail.com",
    description="Projeto proposto no Bootcamp 'NTT DATA - Engenharia de Dados com Python' na plataforma da DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarcosWinther/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
)