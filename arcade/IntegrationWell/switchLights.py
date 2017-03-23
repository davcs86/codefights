def switchLights(a):
    b = len([i for i in a if i])
    print b
    for k, v in enumerate(a):
        a[k] = (v, (v + 1) % 2)[b % 2]
        if v:
            b-=1
    return a

print switchLights([1,1,1,1,1])
print switchLights([0,0])

# Input:
# a: [1, 0, 0, 1, 0, 1, 0, 1]
# Output:
# [1, 0, 0, 0, 0, 0, 0, 0]
# Expected Output:
# [1, 1, 1, 0, 0, 1, 1, 0]

print switchLights([1, 0, 0, 1, 0, 1, 0, 1])

# a: [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1]
# Output:
# [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1]
# Expected Output:
# [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0]

print switchLights([1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1])