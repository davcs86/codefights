def integerToStringOfFixedWidth(n, w):
    a = w-len(n)
    if a>0:
        n = ('0'*a)+n
    elif a < 0:
        n = n[w:]
    return n

print integerToStringOfFixedWidth('1234',2)
print integerToStringOfFixedWidth('1234',4)
print integerToStringOfFixedWidth('1234',6)