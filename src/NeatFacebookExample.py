#!/usr/bin/env python
# encoding: utf-8
"""
NeatFacebookExample.py

Created by Nikolaus Sonnenschein on 2010-10-26.
Copyright (c) 2010 . All rights reserved.
"""

from urllib2 import urlopen
import json

def get_sg(seed_url):
    """Create Internet socket for some seed URL"""
    sgapi_url="http://socialgraph.apis.google.com/lookup?q="+seed_url+"&edo=1&edi=1&fme=1&pretty=0"
    try:
        furl=urlopen(sgapi_url)
        fr=furl.read()
        furl.close()
        return fr
    except IOError:
        print "Could not connect to website"
        print sgapi_url
        return {}

seed="imichaeldotorg"
seed_url="http://"+seed+".livejournal.com"
print get_sg(seed_url)

"http://socialgraph.apis.google.com/<method_name>?<parameter 1>&<parameter 2>&<parameter n>"
print urlopen("http://socialgraph.apis.google.com/lookup?q=niko.sonnenschein@gmail.com")

# url_handle = urllib2.urlopen('https://graph.facebook.com/nikolaus.sonnenschein')
# url_handle = urllib2.urlopen('https://graph.facebook.com/friends')
# print json.load(url_handle)

# content = urllib2.urlopen('http://www.facebook.com/nikolaus.sonnenschein').read()
# content = urllib2.urlopen('http://www.facebook.com').info()
# content = urllib2.Request('http://www.facebook.com').info()
# print content