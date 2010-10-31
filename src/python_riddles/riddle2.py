import urllib2
import string

content = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read().split('<!--')[2]
chars_in_content = list(set(list(content)))
result = list()
for c in chars_in_content:
    if string.count(content, c) == 1 and c is not '>':
        result.append(c)

print ''.join(result)

for c in content:
    if c in result:
        print c
