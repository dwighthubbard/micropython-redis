#!/bin/bash

ls -1d redis redis.*| while read package
do
    cd "$package"
    micropython setup.py sdist
    mv dist/* ../dist
    cd ..
done
