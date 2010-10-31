#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Nikolaus Sonnenschein on 2010-02-13.
Copyright (c) 2010 . All rights reserved.
"""

import sys
import os
import re
import urllib2
import pickle

if os.path.exists('./banner.p'):
    pass
else:
    stuff = pickle.load(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
    print stuff
    pickle.dump(stuff, open('banner.p', 'w'))

stuff = pickle.load(open('banner.p', 'r'))
for sub in stuff:
    print ''.join([i*j for i, j in sub])
print 'Yup! Thats it!'