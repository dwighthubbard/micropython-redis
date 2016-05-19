# Installation Instructions

## Installing on CPython 3

Although micropython-redis is designed to function with micropython, it is supported on most python 3 interpreters.   
Use pip to install on Python3 or PyPy3.

    $ pip install micropython-redis
    
## Installing on micropython

The installation process differs depending on the version of micropython being used.  However the **upip** module 
is used to do the installation from the Python package repositories.

### Installing on micropython unix

Use the micropython **upip** module to install on micropython.  The following Will install the **uredis** module in the
default micropython lib directory:

    $ micropython -m upip install micropython-redis

### Installing on micropython embedded platforms

To install on micropython embedded platforms:

#### Step 1. Create a lib directory to hold the python code for the platform

If you don't already have a library directory on the local system to hold the micropython packages, create one.

    $ mkdir lib

#### Step 2. Set the MICROPATH environment variable to the full path of the lib directory.

Set the MICROPYPATH environment variable to point to the library directory.  If you created the directory in the
current directory as shown in **Step 1** you could run:

    $ export MICROPYPATH="`pwd`/lib"

#### Step 3. Use hte upip module to install micropython-redis into the lib directory.

Use the **upip** module to install the **micropython-redis** package.

    $ micropython -m upip install micropython-redis

#### Step 4. Copy the lib directory to the embedded device.  

Finally copy the lib directory you created to the root of the device filesystem.  This varies depending on the method
being used to put files on the device.
