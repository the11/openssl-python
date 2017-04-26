# from distutils.core import setup
from setuptools import setup

setup(
    name='openssl-python',
    version='0.1',
    packages=['pyopenssl'],
    url='',
    license='GNU GPLv3',
    author='Youssef Seddik',
    author_email='yseddik94@gmail.com',
    description='Command line interface to OpenSSL with Python3',
    long_description='This tool is a command line interface to OpenSSL, '
                     'written with Python3.'
                     'It permits encrypting/decrypting files, '
                     'as well as generating  RSA keys, encrypting the private '
                     'RSA key, signing a file using an RSA key, and also '
                     'verifying signatures using RSA',
   classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: All',
        'License :: OSI Approved :: GNU GPLv3',
        'Programming Language :: Python :: 3.4',
   ],
    keywords='crypto encryption RSA-keys signature signature-verification',
)

