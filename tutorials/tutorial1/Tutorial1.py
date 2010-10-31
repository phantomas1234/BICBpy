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

# Why Python? Google trends -> http://bit.ly/drzVPg

import this
# ->
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

# Standing on the shoulders of giants:
# 1. Huge standard library including everthing you ever dreamed of
# 2. Biopython

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
# or dict? in ipython



# =======================
# = Indentation matters =
# =======================

# Wrong!

# def hello_world():
# print "Hello World!"

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

var += 1
# equal to
var = var + 1


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

try:
    string_var[0] = 'A' # Does not work though because python strings are immutable
    # -> TypeError: 'str' object does not support item assignment
except TypeError, msg:
    print msg

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

try:
    tuple_var[0] = 'Changed' # Does not work though because python tuples are like strings immutable
    # -> TypeError: 'tuple' object does not support item assignment
except TypeError, msg:
    print msg



# Dictionaries

dict_var = {'key':'value'} # Dictionaries are collections of key-value relationships

dict_var['key'] # Values are accessed via their corresponding keys
# -> 'value'

dict_var['key'] = 'new_key' # Values can also be replaced via their corresponding keys
dict_var['key']
# -> 'new_value'



# Sets

set_var = set([2,1,3,3,3,4]) # Sets are unordered collections of unique elements
# -> set([2, 1, 3, 4])

# We can perform operations known from set theory, e.g. intersection, complement, union etc.
set_var.intersection(set([2,1,4,99]))
# -> set([1, 2, 4])
set_var.difference(set([2,1,4,99]))
# -> set([3])
set_var.union(set([2,1,4,99]))
# -> set([1, 2, 3, 4, 99])



# Nested data structures

nested_var = {'nested1': [1, [1,2,3], {'key':'value'}], 'nested2':{'key2':'values2', 'key3':set([1,2,33,33,999])}}
nested_var['nested1'][2]['key']
# -> 'value'



# ======================
# = Control structures =
# ======================

# Conditionals

boolean = True
if boolean:
    print "boolean is True!"
elif boolean == False:
    print "boolean is False!"
else:
    print "boolean is neither True nor False!"
    
# Iteration

for animal in ["cat", "dog", "mouse"]:
    print elem
    
# Loops

counter = 0
while counter <= 10:
    print counter

# break and continue are also available

# ========================
# = Function definitions =
# ========================

def function(arg):
    # Do something with the argument and put it into a temporary variable
    tmpVar = arg + 1 
    # tmpVar is a local variable and is only defined within the function's scope
    # as you will see below
    return tmpVar # return the result

print function(1)
# -> 2
try:
    print tmpVar
    # -> NameError: name 'tmpVar' is not defined
except NameError, msg:
    print msg
    pass

# Default arguments
def function(arg=1): # Argument arg has now a default value
    tmpVar = arg + 1 
    return tmpVar

# so both ...

print function(66)
# -> 67

# and ...

print function()
# -> 2

# ... work



# =====================
# = Class definitions =
# =====================

class Animal(object):
    """Animal base class"""
    def __init__(self, name=""):
        self.name = name
        
    def sayYourName(self):
        print "My name is", self.name

class Cat(Animal):
    """Cat class that inherits from Animal base class"""
    def __init__(self, name="", fur_color="White"):
        Animal.__init__(self, name=name)
        self.fur_color = fur_color
        
    def sayYourNameAndColor(self):
        Animal.sayYourName(self)
        print "My fur is", self.fur_color



# =======================
# = Catching Exceptions =
# =======================

# What if we provide a string as an argument for function?

try:
    print function("1")
    # -> TypeError: cannot concatenate 'str' and 'int' objects
except:
    pass

# How should we handle Exceptions like these?

def function(arg=1):
    try:
        tmpVar = arg + 1 # try this statement ...
    except TypeError, msg: # msg -> 'cannot concatenate 'str' and 'int' objects'
        print msg
        print "Please provide" # ... proceed here if a TypeError exception is raised ...
    else:
        print "result is", tmpVar # ... or here if everthing is fine.
    finally:
        print "executing finally clause" # This gets executed in both cases!

# ... or even more involved ...

def function_more_involved(arg=1):
    try:
        tmpVar = arg + 1
    except TypeError, msg:
        print msg
        print "Should I try to cast the argument of type " + str(type(arg)) + "into an integer? [default:no|yes]"
        human_input = raw_input("")
        if human_input == 'yes':
            tmpVar = int(arg) + 1
            print "result (using casting) is", tmpVar
        elif human_input == '' or human_input == 'no':
            print "Ok, than I will do nothing!"
        else:
            raise AssertionError, "Please provide yes or no idiot! Aborting ..."
            sys.exit()
    else:
        print "result is", tmpVar
    finally:
        print "executing finally clause"


# =========
# = Tasks =
# =========

# 1. Write a function that generates the Fibonacci numbers
# 2. 

# 3. Try to solve as many Python riddles as you can!
# http://www.pythonchallenge.com/


