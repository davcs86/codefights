class City:
    def __init__(self):
        self.__edges = {}
        self.__days = 0
        self.__conquered = False
    def addEdge(self, edge):
        self.__edges[edge] = 1
    def removeEdge(self, edge):
        if edge in self.__edges:
            del self.__edges[edge]
    def getEdges(self):
        return self.__edges
    def conquer(self):
        self.__conquered = True
    def isConquerable(self):
        return len(self.__edges) < 2
    def isConquered(self):
        return self.__conquered
    def addDay(self):
        self.__days += 1
    def getDays(self):
        return self.__days if self.isConquered() else -1

def citiesConquering(n, roads):
    cities = {k: City() for k in range(n)}
    for r in roads:
        cities[r[0]].addEdge(r[1])
        cities[r[1]].addEdge(r[0])
    toVisit = [i for i in range(n)]
    while toVisit:
        toConquer = []
        nVisit = []
        for k in toVisit:
            if cities[k].isConquerable() and not cities[k].isConquered():
                cities[k].addDay()
                toConquer.append(k)
            elif not cities[k].isConquered():
                cities[k].addDay()
                nVisit.append(k)
        if len(toConquer)==0:
            break
        for i in toConquer:
            cities[i].conquer()
            for d in cities[i].getEdges():
                cities[d].removeEdge(i)
        toVisit = nVisit

    return [c.getDays() for k, c in cities.iteritems()]


n = 10
roads = [[1, 0], [1, 2], [8, 5], [9, 7],
         [5, 6], [5, 4], [4, 6], [6, 7]]

print citiesConquering(n, roads) == [1, 2, 1, 1, -1, -1, -1, 2, 1, 1]