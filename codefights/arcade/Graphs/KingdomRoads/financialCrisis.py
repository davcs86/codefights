def rmCity(m, i):
    r = []
    for k, f in enumerate(m):
        if k == i:
            continue
        t = []
        for l, c in enumerate(f):
            if l == i:
                continue
            t.append(c)
        r.append(t)
    return r

def financialCrisis(r):
    p = []
    for k in range(len(r)):
        p.append(rmCity(r, k))
    return p

roadRegister = [[False, True,  True,  False],
                [True,  False, True,  False],
                [True,  True,  False, True ],
                [False, False, True,  False]]


print financialCrisis(roadRegister)