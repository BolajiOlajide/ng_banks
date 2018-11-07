"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup

from os import path

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ng_banks',
    packages=['ng_banks'],
    version='1.0.1',
    long_description=long_description,

    description='Python Implementation for Lightweight Zero dependency npm \
    package to get list of banks in Nigeria (Recognized by CBN)',

    author='Bolaji Olajide',
    author_email='cooproton@gmail.com',
    url='https://github.com/BolajiOlajide/ng_banks',
    download_url='',
    long_description_content_type="text/markdown",
    keywords=['banks', 'nigeria', 'nigerian', 'cbn'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
