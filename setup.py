# from distutils.core import setup
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='openssl-python',
    version='0.1',
    packages=['pyopenssl'],
    url='https://github.com/the11/openssl-python',
    license='GNU GPLv3',
    author='Youssef Seddik',
    author_email='yseddik94@gmail.com',
    description='Command line interface to OpenSSL with Python3',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.4',
   ],
    keywords='crypto encryption RSA-keys signature signature-verification',
)

