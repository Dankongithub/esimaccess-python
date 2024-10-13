from setuptools import setup, find_packages

setup(
    name="esimaccess-python",
    version="0.1.0",
    description="Python SDK for the Esimaccess API",
    author="Corbin Li",
    packages=find_packages(),
    install_requires=[
        "httpx"
    ]
)
