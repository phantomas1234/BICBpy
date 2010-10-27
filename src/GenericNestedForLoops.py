#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Nikolaus Sonnenschein on 2010-10-25.
Copyright (c) 2010 Jacobs University of Bremen. All rights reserved.
"""

import sys
import os


def tuples(bunch, k):
    """Returns a generator of all k tuple combinations of elements in bunch"""
    exec 'gen = (' + str(indices) + " " + " ".join(tuple(["for "+str(e)+" in b" for e in indices]))+ ')'
    return gen

if __name__ == '__main__':
    b = ['a', 'b', 'c', 'd']
    slots = 3 # tuple length
    indices = tuple(['e'+str(i) for i in range(slots)])
    
    print indices
    
    print " ".join(tuple(["for "+str(e)+" in b" for e in indices]))
    hack = 'gen = (' + str(indices) + " " + " ".join(tuple(["for "+str(e)+" in b" for e in indices]))+ ')'
    exec hack
    print list(gen)
    
    print tuples