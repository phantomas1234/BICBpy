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

numbers = list()
flag = True
# number = '1234'
number = '46059'
# number = '60077'
counter = 0
while flag:
    content = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+number).read()
    try:
        text, number = re.findall('(.+?)(\d+)', content)[0]
    except:
        print content
        sys.exit(1)
    counter = counter + 1
    if not number or counter > 1500:
        flag = False
    print text, number
    numbers.append(number)
    
pickle.dump(numbers, open('riddle4.pcl', 'w'))