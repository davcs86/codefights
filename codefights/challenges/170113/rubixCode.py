import re

def printMatrix(r):
    for i in r:
        print "[" + ",".join([str(j) for j in i]) + "]"

def r(l, n, p, s):
    f = -1 if p else 1
    return l[(f*n) % s:] + l[:(f*n) % s]

def t(c, i, j, s, r):
    #print i, j, s, r
    m = [z[j:j+s] for z in c[i:i+s]]
    #print m
    n = zip(*reversed(m)) if r else list(reversed(zip(*m)))
    #print n
    for k in range(0, s):
        for l in range(0, s):
            c[k+i][l+j] = n[k][l]
    return c

def L(c, n, i, s):
    print n, i ,s
    #print [r(j, 2*s, 1, 4*s) for j in c[s:2*s]]
    d=c[:]
    c += [r(j, 2*s, 1, 4*s) for j in c[s:2*s]]
    printMatrix(c)
    print " "
    for p in range(0, 3*s):
        d[p] = (c[p][:s+n] + [c[(p+s)%(4*s)][2*s-n]] + c[p][s+n+1:]) if i else (c[p][:s+n] + [c[(p-s)%(4*s)][s+n]] + c[p][s+n+1:])
        if p>=s and p<2*s:
            d[p][4*s-n-1] = c[(p+2*s)%(3*s)][2*s-n] if i else c[(p-2*s)%(3*s)][s+n]
    if n == 0:
        d = t(d, s, 0, s, not i)
    elif n == s-1:
        d = t(d, s, 2*s, s, i)
    return d

def B(c, n, i, s):
    #print n, i, s
    c[s+n] = r(c[s+n], 3, i, s*4)
    if n == 0:
        c = t(c, 0, s, s, not i)
    elif n == s-1:
        c = t(c, 2*s, s, s, i)
    #d = c
    #d[s+n] = (c[s+n][-1*s:] + c[s+n][:3*s]) if i else (c[s+n][3*s:] + c[s+n][:3*s])
    return c

def U(c, n, i, s):
    d = c[:]
    for p in range(s, 2*s):
        d[p][s-1-n], d[s-1-n][s*3-p-1], d[s*3-p-1][s*2+n], d[s*2+n][s*3-p-1] = [c[s-1-n][s*3-p-1], c[s*3-p-1][s*2+n], c[s*2+n][s*3-p-1], c[p][s-1-n]] if i else [c[s*2+n][s*3-p-1], c[p][s-1-n], c[s-1-n][s*3-p-1], c[s*3-p-1][s*2+n]]
    if n == 0:
        d = t(d, s, s, s, not i)
    elif n == s-1:
        d = t(d, s, 3*s, s, i)
    return d

def rubixCube(c, m):
    d = {
        "L": L,
        "B": B,
        "U": U,
        "R": lambda c, n, i, s: L(c, s-1-n, not i, s),
        "F": lambda c, n, i, s: B(c, s-1-n, not i, s),
        "D": lambda c, n, i, s: U(c, s-1-n, not i, s)
    }
    s = len(c) / 3
    m = map(lambda r: re.match("^([^\di]+)(i?)(.*)$", r).groups(), m.split())
    for f,i,n in m:
        c = d[f](c,int(n),i,s)
    return c

c = [[0,0,0,6,6,6,0,0,0,0,0,0],
 [0,0,0,6,6,6,0,0,0,0,0,0],
 [0,0,0,10,6,6,0,0,0,0,0,0],
 [5,5,5,1,1,1,2,2,2,3,3,3],
 [5,5,12,1,1,1,13,2,2,3,3,3],
 [5,5,5,1,1,1,2,2,2,3,3,3],
 [0,0,0,11,4,4,0,0,0,0,0,0],
 [0,0,0,4,4,4,0,0,0,0,0,0],
 [0,0,0,4,4,4,0,0,0,0,0,0]]

printMatrix(c[:])
print " "
printMatrix(rubixCube(list(c), "R0"))
print " "

c = [[0,0,0,6,6,6,0,0,0,0,0,0],
 [0,0,0,6,6,6,0,0,0,0,0,0],
 [0,0,0,6,2,6,0,0,0,0,0,0],
 [5,5,5,1,1,1,2,2,2,3,3,3],
 [5,5,12,1,1,1,13,2,2,3,3,3],
 [5,5,5,1,1,1,2,2,2,3,3,3],
 [0,0,0,11,4,4,0,0,0,0,0,0],
 [0,0,0,4,4,4,0,0,0,0,0,0],
 [0,0,0,4,4,4,0,0,0,0,0,0]]

#printMatrix(c[:])
#print " "
printMatrix(rubixCube(list(c), "R2"))
print " "