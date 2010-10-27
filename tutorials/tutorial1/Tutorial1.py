#!/usr/bin/env python
# encoding: utf-8
"""
Tutorial1.py

Created by Nikolaus Sonnenschein on 2010-10-26.
Copyright (c) 2010 . All rights reserved.
"""

# ===========
# = Python? =
# ===========

# The Zen of Python, by Tim Peters
# 
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# TODO:
# try/except/else/finally

# =================
# = Ipython Shell =
# =================

# Show normal Python shell
# Show Ipython Shell

# ================
# = Neat example =
# ================

# urllib2?
# shutil/ os
# gzip/bzip2
# glob
# random
# re
# pickle

# ================
# = Getting Help =
# ================

help(dict)
# or
dict?

# =======================
# = Indentation matters =
# =======================

# Wrong!

def hello_world():
print "Hello World!"

# Correct!
def hello_world():
    print "Hello World!"
    
# 1. Indentation has to be consistent
# 2. Four spaces (not tabs!) are the standard

# ===============
# = Assignments =
# ===============

var = 1

a, b, c = (1, 2, 3) # Multiple assignments

# =======================
# = Built-in Data types =
# =======================

#### Integers, Floats, Complex numbers, Operators ###

int_var = 1
float_var = 1.3
complex_var = 1.3+3.j # or complex(1.3, 3.)

int_var - float_var # Subtraction
# -> -0.30000000000000004

int_var + float_var # Addition
# -> 2.2999999999999998

int_var * float_var # Multiplication
# -> 1.3

int_var / float_var # Division
# -> 0.76923076923076916

int_var ** float_var # int_var to the power of float_var
# -> 1.0

int_var % float_var # Modulo
# -> 1.0

# Strings

string_var = 'Hello World!'

string_var[0] # Indexing (starts with 0)
# -> 'H'

string_var[0:-1] # Slicing
# -> 'Hello World'

string_var[0] = 'A' # Does not work though because python strings are immutable
# -> TypeError: 'str' object does not support item assignment

string_var.replace('World', 'Kitty')
# -> 'Hello Kitty!'

# Introspection: Everything is an object!
dir(string_var)
# -> [...
# 'capitalize',
#  'center',
#  'count',
#  'decode',
#  'encode',
#  'endswith',
# ...
#  'swapcase',
#  'title',
#  'translate',
#  'upper',
#  'zfill']


# Lists

list_var = ['1', 1, 1.] # Lists can contain elements of different types

list_var[0] # Indexing
# -> '1'

list_var[0:-1] # Slicing
# -> ['1', 1]

list_var[0] = 'Changed' # Works because python lists are mutable
list_var
# -> ['Changed', 1, 1.0]

# Tuples (are immutable lists)

tuple_var = ('1', 1, 1.)

tuple_var[0] # Indexing
# -> '1'

tuple_var[0:-1] # Slicing
# -> ['1', 1]

tuple_var[0] = 'Changed' # Works because python lists are mutable
list_var
# -> ['Changed', 1, 1.0]










 
