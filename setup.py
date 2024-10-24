from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name="esimaccess-python",
    version="0.1.1",
    description="Python SDK for the Esimaccess API",
    author="Corbin Li",
    packages=find_packages(),
    install_requires=[
        "httpx"
    ],
    long_description = long_description,
    long_description_content_type = 'text/markdown'
)
