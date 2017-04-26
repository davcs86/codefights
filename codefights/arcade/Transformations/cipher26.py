def cipher26(m):
    n = m[0]
    a = ord(m[0]) - 97
    #print a
    for c in range(1, len(m)):
        b = 26 - a + ord(m[c]) - 97
        while b < 0:
            b += 26
        a += b
        #print b
        n += chr(b+97)
    return n

print cipher26('taiaiaertkixquxjnfxxdh')