import os
import codecs

from setuptools import setup, find_packages

from digiformatter import version as versionnum

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as f:
        return f.read()

setup(
    name="digiformatter",
    version=versionnum,
    description="Make your terminals look spicy.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    keywords="",
    author="DigiDuncan",
    author_email="digiduncan@gmail.com",
    url="https://github.com/DigiDuncan/DigiFormatter",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "colored"
    ],
    python_requires=">=3",
    classifiers=[
    ]
)
