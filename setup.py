from setuptools import setup, find_packages

setup(
    name='matplotlib-extensions',
    version='0.2.0',
    packages=find_packages(),
    license='MIT',
    description='Natural extensions to Matplotlib for multidimensional plotting.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Vemund Schøyen',
    author_email='vemund@live.com',
    url='https://github.com/Vemundss/matplotlib-extensions',
    install_requires=[
        'numpy',
        'matplotlib',
        'IPython',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
