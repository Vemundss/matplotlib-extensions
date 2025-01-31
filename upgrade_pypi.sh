#!/bin/bash

# -----
# REMEMBER! To upgrade version number in setup.py
# -----

rm -rf build/ dist/ *.egg-info
#python -m pip install --upgrade setuptools wheel twine
python setup.py sdist bdist_wheel
python -m twine upload dist/*
