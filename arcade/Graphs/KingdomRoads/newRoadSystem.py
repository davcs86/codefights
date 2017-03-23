class Node:
    adjacencyList = []
    outComing = 0
    inComing = 0
    def __init__(self, adjacency):
        self.adjacencyList = [k for k,v in enumerate(adjacency) if v]
        self.outComing = sum(adjacency)
    def isValid(self):
        return self.outComing == self.inComing

def newRoadSystem(r):
    nodes = [Node(i) for i in r]
    for i in nodes:
        for j in i.adjacencyList:
            nodes[j].inComing += 1
    valid = sum([1 for i in nodes if i.isValid()])
    return valid == len(r)

roadRegister = [[False, True,  False, False],
                [False, False, True,  False],
                [True,  False, False, True ],
                [False, False, True,  False]]

print newRoadSystem(roadRegister)