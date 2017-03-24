def isButterfly(adj):
    h = [0, 0, 0, 0, 0]
    hi = -1
    v = [0, 0, 0, 0, 0]
    vj = -1
    for i, a in enumerate(adj):
        for j, b in enumerate(a):
            if b:
                h[i]+=1
                v[j]+=1
                if h[i]==4:
                    hi = i
                if v[j]==4:
                    vj = j
    center = adj[hi][vj]
    # diagonals respect center must be false
    oi = hi - 2
    oj = vj - 2
    #print h, v, oi, oj
    for i in range(5):
        if adj[i+oi][i+oj] or adj[4-i+oi][i+oj]:
            return False

    h = sorted(h)
    v = sorted(v)
    #print h, v
    return h == v and h == [2, 2, 2, 2, 4] and hi == vj and not center

adj = [[False, True, True, False, False],
       [True, False, True, False, False],
       [True, True, False, True, True],
       [False, False, True, False, True],
       [False, False, True, True, False]]

print isButterfly(adj) == True

adj = [[False,True,True,True,True], 
 [True,False,True,False,False], 
 [True,True,False,False,False], 
 [True,False,False,False,True], 
 [True,False,False,True,False]]

print isButterfly(adj) == True

adj = [[False,True,True,False,False], 
 [True,False,True,False,False], 
 [True,True,True,True,False], 
 [False,False,True,False,True], 
 [False,False,False,True,True]]

print isButterfly(adj) == False