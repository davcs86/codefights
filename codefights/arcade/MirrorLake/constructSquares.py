from collections import Counter
from itertools import permutations

def constructSquares(s):
    a = {1:[],4:[],5:[],6:[],9:[],0:[0]}
    d = {k: False for k in Counter(s).iterkeys()}
    p = permutations(s, len(s))
    print d
    for i in p:
        print list(reversed(i))
        for j in reversed(i):
            print j
        print "-*-"
    return 0
    contLen = len(containers)
    limit = int("1"*contLen, 2)
    for i in range(1, limit+1):
        combination = ("{0:0"+str(contLen)+"b}").format(i)
        combList = [containers[j] for j, k in enumerate(combination) if k == "1"]
        if sum(combList) >= total:
            return len(combList)
    return -1

constructSquares('aab')