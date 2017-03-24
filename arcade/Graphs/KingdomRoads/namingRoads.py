class City:
    def __init__(self):
        self.__edges = []
    def addEdge(self, edge):
        self.__edges.append(edge)
    def getEdges(self):
        return self.__edges
    def isValid(self):
        edges = self.__edges = sorted(self.__edges)
        sz = len(edges)
        if sz > 1:
            pItem = edges[0]
            for i in range(1, sz):
                nItem = edges[i]
                if nItem - pItem == 1:
                    return False
                pItem = nItem
        return True

def namingRoads(roads):
    cities = {}
    for r in roads:
        city = cities.get(r[0], City())
        city.addEdge(r[2])
        cities[r[0]] = city
        city = cities.get(r[1], City())
        city.addEdge(r[2])
        cities[r[1]] = city
    for k, c in cities.iteritems():
        if not c.isValid():
            return False
    return True


roads = [[0, 1, 0],
         [4, 1, 2],
         [4, 3, 4],
         [2, 3, 1],
         [2, 0, 3]]
print namingRoads(roads) == True

roads = [[2, 3, 1],
         [3, 0, 0],
         [2, 0, 2]]
print namingRoads(roads) == False