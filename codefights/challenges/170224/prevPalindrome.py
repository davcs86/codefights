def prevPalindrome(x):
    a = map(int, list(str(x)))
    f = len(a) - 1
    already = False
    for i in range(0, (f+1) // 2):
        if a[i] == a[f-i] and not already:

            already = True
        print i
    print a

prevPalindrome(16)
prevPalindrome(11)