#!/usr/bin/env python
"""
Installation script for the project
"""
import os
from setuptools import setup


def get_long_description():
    """
    Returns the long description of the project; either read from the README
    or a default description, if that doesn't exist.
    """
    readme_file_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_file_path):
        description = open(readme_file_path).read()
    else:
        description = """Offers an alternative to the standard way of generating
Fabric tasks. Instead
of random functions or Task declarations, instead create Commands classes that
use a simple configuration flow and allow for dependency injection to share
functionality between Tasks.

Additionally, some simple tasks are auto-generated and act as examples of how
to write Commands."""
    return description

setup(
    name='fabpowertasks',
    version='0.0.1',
    author='Shane Breatnach',
    author_email='shane.breatnach@gmail.com',
    description='',
    license='MIT',
    keywords='fabric tool',
    url='http://pythonhosted.org/fabpowertasks',
    packages=['fabpowertasks'],
    install_requires=[
        "fabric>=1.7.0", 'fabtools>=0.17.0'
    ],
    long_description=get_long_description(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ]
)
