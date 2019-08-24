# openssl-python

This tool is a command line interface to OpenSSL, written with Python3.
It permits encrypting/decrypting files, as well as generating RSA keys, encrypting private RSA keys, signing files using an RSA key, and also verifying signatures using RSA.  
  
## Dependencies
  
Before running this tool, the following dependency must be installed, as well as being on the path:

* openssl  
  
Usually, this dependency exists by default in most of the supported platforms(see below). In case it doesn't, try consulting the official [OpenSSL documentation](https://www.openssl.org/docs/); or consult your operating system' documentation on how to install new software. 
  
## Usage

### Using the source code
* To launch openssl-python tool, just clone the source code from [Github Repository](https://github.com/the11/openssl-python):
    ```
    git clone git@github.com:the11/openssl-python.git
    ```
* Go to the source code directory and proceed in one of the two following ways:
    * run the following command:  
    ```
    python3 openssl-python.py
    ```
    * Or alternatively, if python is in the path, run the following commands:
    ```
    chmod +x openssl-python.py
    ./openssl-python.py
    ```
### Using pip
* Download the package by using the pip tool:
    ```
    pip install openssl-python
    ```
* Launch your Python interpreter and start using the package
    ```
    python3
    >>> import openssl_python
    ```


## Platform support

This tool was initially developed and tested on Linux systems, so it does also support Unix-like systems: BSDs, Mac OS...  
Windows support though is not guaranteed.
