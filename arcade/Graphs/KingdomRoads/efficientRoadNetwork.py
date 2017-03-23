class Node:
    def __init__(self, id):
        self.__id = id
        self.__adjacencyList = set([])
        self.__2ndAdjacencyList = set([])

    def getId(self):
        return self.__id

    def addCity(self, city):
        if city != self.__id:
            self.__adjacencyList |= {city}

    def add2ndCity(self, city):
        if city != self.__id:
            self.__2ndAdjacencyList |= {city}

    def add2ndCities(self, cities):
        for c in cities:
            self.add2ndCity(c)

    def getCities(self):
        return self.__adjacencyList

    def getFullCities(self):
        return self.__2ndAdjacencyList | self.__adjacencyList

    def getCitiesCount(self):
        return len(self.getFullCities())

    def isValid(self, n):
        return self.getCitiesCount() == (n - 1)


def efficientRoadNetwork(n, roads):
    cities = [Node(i) for i in range(n)]
    for r in roads:
        cities[r[0]].addCity(r[1])
        cities[r[1]].addCity(r[0])

    for c in cities:
        for cc in c.getCities():
            c.add2ndCities(cities[cc].getCities())
        if not c.isValid(n):
            return False
    return True

###################
n = 6
roads = [[3, 0], [0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
print efficientRoadNetwork(n, roads)

n = 6
roads = [[0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
print efficientRoadNetwork(n, roads)

n = 7
roads = [[1,0],
 [0,2],
 [2,4],
 [3,0],
 [5,6],
 [5,4],
 [5,0],
 [0,4],
 [5,2]]
print efficientRoadNetwork(n, roads)
