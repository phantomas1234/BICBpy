import string

asci = string.ascii_lowercase
len_asci = len(asci)
rules = list()
for i in range(len_asci):
    if i <= len_asci - 3:
        rules.append((asci[i], asci[i+2]))
    else:
        rules.append((asci[i], asci[abs(i - len_asci) - abs(i - len_asci)]))
print rules
rules = dict(rules)
rules['z'] = 'b'
print rules

# s = list("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
s = list("http://www.pythonchallenge.com/pc/def/map.html")
s2 = list()
for c in s:
    if rules.has_key(c):
        c = rules[c]
    s2.append(c)
print ''.join(s2)