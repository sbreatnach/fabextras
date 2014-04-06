#!/bin/sh
python2.6 setup.py sdist bdist_egg upload --sign --identity="Shane.Breatnach"
python2.7 setup.py bdist_egg upload --sign --identity="Shane.Breatnach"
