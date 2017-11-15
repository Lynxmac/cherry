"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cherry',
    version='0.1.8',
    description='classify data set',
    long_description=long_description,
    url='https://github.com/Sunkist-Cherry/cherry',
    author='Windson Yang',
    author_email='wiwindson@outlook.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='data classify content filter',
    install_requires=[
        'jieba>=0.39',
        'numpy>=1.13.3', 
        ],
    packages=['filter'],
    package_data={
        'filter': ['cache/*', 'data/large/*.dat', 'data/small/*.dat'],
    },
)
