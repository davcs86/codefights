def printMatrix(r):
    for i in r:
        print "[" + ",".join([str(j) for j in i]) + "]"

def livingOnTheRoads(r):
    # create links
    links = []
    for i in range(len(r)):
        for j in range(i+1, len(r)):
            if r[i][j]:
                links.append({i, j})
    # check for the intersections
    results = [[False for i in range(len(links))] for j in range(len(links))]
    for i in range(len(links)):
        for j in range(i+1, len(links)):
            if len(links[i] | links[j]) < 4:
                results[i][j] = True
                results[j][i] = True
    return results

roadRegister = [
  [False, True,  True,  False, False, False],
  [True,  False, False, True,  False, False],
  [True,  False, False, False, False, False],
  [False, True,  False, False, False, False],
  [False, False, False, False, False, True ],
  [False, False, False, False, True,  False]
]


print livingOnTheRoads(roadRegister) == [
  [False, True,  True,  False],
  [True,  False, False, False],
  [True,  False, False, False],
  [False, False, False, False]
]