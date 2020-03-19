import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='med-coursework-parser',
    version='0.0.1',
    packages=setuptools.find_packages(),
    url='https://github.com/hearts-thaw/med-coursework-parser',
    license='',
    author='hearts-thaw',
    author_email='pavel.sviststetsky@gmail.com',
    description='DOCX parser for medical students\' coursework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7', install_requires=['python-docx', 'psycopg2']
)
