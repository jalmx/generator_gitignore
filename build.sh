#!/bin/sh

# pip install python-minifier # if failed install this
NAME_SCRIPT="ignore"

rm -rf bin

mkdir -p bin

pyminify ./src/ignore.py --output ./bin/$NAME_SCRIPT
sudo chmod +x bin/$NAME_SCRIPT
