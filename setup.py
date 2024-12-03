from setuptools import setup, find_packages

setup(
    name='mplextensions',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'IPython',
    ],
    python_requires='>=3.6',
    author='Vemund Schøyen',
    author_email='vemund@live.com',
    description='Extensions for Matplotlib plotting functions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Vemundss/matplotlib-extensions',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)