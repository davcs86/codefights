import re

def switchDemSigns(e):
    a = 0
    r = ''
    if e:
        s = re.search('[\+\-]', e)
        t = re.search('[^\s\+\-]', e)
        if s and t and s.span()[0] > t.span()[0]:
            e = '+ ' + e
    for i in e:
        a+=((0,-1)[i == ')' or i == '}'],1)[i == '(' or i == '{']
        r+=(((i, '+')[i == '-'],'-')[i == '+'],i)[a>0]
    return r

print switchDemSigns('a + (b + c - (p - q) + (z - x - {r})) + f')
print switchDemSigns('a + b + c - (p - q) + (z - x - {r}) + f')