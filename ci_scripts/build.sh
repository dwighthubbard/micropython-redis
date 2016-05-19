#!/bin/bash

ls -1d uredis redis.*| while read package
do
    cd "$package"
    python3 setup.py sdist
    mv dist/* ../dist
    cd ..
done
