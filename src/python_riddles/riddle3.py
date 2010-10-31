import urllib2
import re
import pickle
import os

if os.path.exists('./riddle3.pcl'):
    content = pickle.load(open('riddle3.pcl'))
else:
    content = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read().split('<!--')[1]
    pickle.dump(content, open('riddle5.pcl', 'w'))
    
all = re.findall('[A-Z]{3}[a-z][A-Z]{3}', content)
print all
print re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', content)
print re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', content)
print "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', content))

# print [elem for elem in all if elem[0:3] == elem[4:]]
# smallOnes = re.findall('[A-Z]{3}([a-z])[A-Z]{3}', content)
# print ''.join(smallOnes)