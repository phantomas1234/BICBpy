#!/usr/bin/env python
# encoding: utf-8
"""
NeatFacebookExample.py

Performs a breadth-first-search traversal of the public facebook network

Created by Nikolaus Sonnenschein on 2010-10-26.
Copyright (c) 2010 . All rights reserved.
"""

import re
import time
import random
import urllib2
import networkx as nx

stack = ['nikolaus.sonnenschein']
url_dict = dict()
network = set([])
depth = 2
regex = re.compile('<a class="title" href="(.*?)" rel="friend" title="(.*?)">')

for level in range(depth):
    for person in stack:
        print person
        person = stack[0]
        url = 'http://www.facebook.com/' + person
        siteOpener = urllib2.urlopen(url)
        siteContent = siteOpener.read()
        for match in regex.findall(siteContent):
            friend = ".".join(match[1].lower().split())
            url_dict[friend] = match[0]
            stack.append
            network.add((person, friend))
        
        # time.sleep(random.random()+1)

        print network
        print url_dict
