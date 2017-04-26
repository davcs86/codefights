from itertools import combinations
def roadsBuilding(cities, roads):
    roads = [sorted(i) for i in roads]
    return [[a, b] for a, b in combinations(range(cities), 2) if [a, b] not in roads]

print roadsBuilding(4, [[0, 1], [1, 2], [2, 0]])