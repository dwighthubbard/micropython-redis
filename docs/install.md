# Installation Instructions

## Installing on CPython 3

Although micropython-redis is designed to function with micropython, it is supported on most python 3 interpreters.   
Use pip to install on Python3 or PyPy3.

    $ pip install micropython-redis
    
## Installing on micropython

The installation process differs depending on the version of micropython being used.  However the *pip-micropython* 
tool is used to do the installation from the Python package repositories.

### Installing on micropython unix

Use the *pip-micropython* tool to install on micropython.  Will install pip-micropython t the default micropython
lib directory.

    $ pip-micropython install micropython-redis

### Installing on micropython embedded platforms

To install on micropython embedded platforms:

1. Create a lib directory to hold the python code for the platform

    $ mkdir lib
    
2. Set the MICROPATH environment variable to the full path of the lib directory.

    $ export MICROPATH="`pwd`/lib"
    
3 Run pip-micropython to install micropython-redis into the lib directory.

    $ pip-micropython install micropython-redis
    
4. Copy the lib directory to the embedded device.  

