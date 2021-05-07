#!/usr/bin/python

import sys

for line in sys.stdin:
    lineList = line.split()
    for word in line:
        word = word.lower()
        print word, 1