
magicSquare = lambda s, t, n: [[s + (y * t) for y in x] for x in [[],[[1,6,5],[8,4,0],[3,2,7]],[[0,1,14,15],[11,13,2,4],[12,6,9,3],[7,10,5,8]],[[0]]][n-2]]

def printMatrix(r):
    print "["+"\n".join(["[" + ",".join([str(j) for j in i]) + "]" for i in r])+"]\n"


printMatrix(magicSquare(2017,7,1))
printMatrix(magicSquare(2017,7,2))
printMatrix(magicSquare(2017,7,3))
printMatrix(magicSquare(2017,7,4))
