def Chemicals(t, u):
    z = []
    for i in range(len(u)):
        v = t * 1
        y = 0
        if u[i] > 0:
            y = v / u[i]
            v %= u[i]
            if v > 0:
                for j in range(i-1, -1, -1):
                    if u[j] > 0:
                        x = v / u[j]
                        y += x
                        v %= u[j]
                        if v == 0:
                            break
        print v, y
        if v == 0:
            z.append(y)
    print z
    return min(z) if len(z) else -1


    # contLen = len(containers)
    # limit = int("1"*contLen, 2)
    # for i in range(1, limit+1):
    #     combination = ("{0:0"+str(contLen)+"b}").format(i)
    #     combList = [containers[j] for j, k in enumerate(combination) if k == "1"]
    #     if sum(combList) >= total:
    #         return len(combList)
    # return -1

print Chemicals(18, [1, 2, 5, 10])
print Chemicals(9, [1, 4, 6])
print Chemicals(10, [8])
print Chemicals(0, [8])
print Chemicals(39883, [383, 440, 449])