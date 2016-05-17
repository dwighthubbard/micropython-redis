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

#### Step 1. Create a lib directory to hold the python code for the platform

If you don't already have a library directory on the local system to hold the micropython packages, create one.

    $ mkdir lib

#### Step 2. Set the MICROPATH environment variable to the full path of the lib directory.

Set the MICROPATH environment variable to point to the library directory.  If you created the directory in the
current directory as shown in *Step 1* you could run:

    $ export MICROPATH="`pwd`/lib"

#### Step 3. Run pip-micropython to install micropython-redis into the lib directory.

Use the *pip-micropython* tool to install the *micropython-redis* package.

    $ pip-micropython install micropython-redis

#### Step 4. Copy the lib directory to the embedded device.  

Finally copy the lib directory you created to the root of the device filesystem.  This varies depending on the method
being used to put files on the device.
