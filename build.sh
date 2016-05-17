#!/bin/bash

ls -1d redis redis.*| while read package
do
    cd "$package"
    python3 setup.py sdist upload
    mv dist/* ../dist
    cd ..
done
