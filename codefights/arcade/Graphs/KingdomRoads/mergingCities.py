def printMatrix(r):
    for i in r:
        print "[" + ",".join([str(j) for j in i]) + "]"

def rmCity(m, i):
    r = []
    for k, f in enumerate(m):
        if k == i:
            continue
        t = []
        for l, c in enumerate(f):
            if l == i:
                continue
            if k == i - 1:
                if l == i - 1:
                    t.append(False)
                else:
                    t.append(c or m[k+1][l])
            else:
                if l == i - 1:
                    t.append(c or m[k][l+1])
                else:
                    t.append(c)
        r.append(t)
    return r

def mergingCities(r):
    o = 0
    for i in range(len(r)/2):
        j = i*2
        if r[j+o][j+o+1]:
            r = rmCity(r, j+o+1)
            o -= 1
    return r

roadRegister = [
  [False, True,  True,  False, False, False, True ],
  [True,  False, True,  False, True,  False, False],
  [True,  True,  False, True,  False, False, True ],
  [False, False, True,  False, False, True,  True ],
  [False, True,  False, False, False, False, False],
  [False, False, False, True,  False, False, False],
  [True,  False, True,  True,  False, False, False]
]


print mergingCities(roadRegister) == [
  [False, True,  True,  False, True ],
  [True,  False, False, True,  True ],
  [True,  False, False, False, False],
  [False, True,  False, False, False],
  [True,  True,  False, False, False]
]