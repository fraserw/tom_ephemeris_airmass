from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tom-ephemeris-airmass',
    version='0.1.0',
    description='Tom Toolkit extension module for tom_nonsidereal_airmass',
    long_description=long_description,
    long_description_content_type='text/markdown',
    #url='https://tomtoolkit.github.io',
    author='fraserw',
    author_email='westhefras@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    keywords=['tomtoolkit', 'astronomy', 'astrophysics', 'observatory', 'planetary'],
    packages=find_packages(),
    install_requires=[
        'tomtoolkit',
        'numpy',
        'json'
    ],
    include_package_data=True,
)
