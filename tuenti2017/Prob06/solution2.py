#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from sys import maxint

"""
The Bellman-Ford algorithm
Graph API:
    iter(graph) gives all nodes
    iter(graph[u]) gives neighbours of u
    graph[u][v] gives weight of edge (u, v)
"""

# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = maxint
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d


# graph = {
#         '1': {'2': 1, '3': 3},
#         '2': {'3': 2, '4': 5, '1': 0},
#         '3': {'4': 3, '2': 0},
#         '4': {'3': 0}
#         }
#
# print bellman_ford(graph, '1')
#
# graph = {
#         '1': {'2': 1},
#         '2': {'3': 2, '1': 0},
#         '3': {'4': 3, '5': 2, '2': 0},
#         '4': {'5': 4, '8': 6, '3': 0},
#         '5': {'6': 5, '8': 20, '4': 0},
#         '6': {'7': 6, '5': 0},
#         '7': {'8': 7, '6': 0},
#         '8': {'9': 8, '7': 0},
#         '9': {'8': 0},
#         }
#
# print bellman_ford(graph, '1')

fname = "submitInput.txt"
fname2 = "submitOutput2.txt"

with open(fname, "r") as stdin:
    with open(fname2, "w", 0) as fil:

        t = int(stdin.readline().strip())

        for T in range(1, t+1):

            f, s = map(int, stdin.readline().strip().split(' '))

            g = {}
            for F in range(1, f + 1):
                k = str(F)
                g[k] = {}
                if F < f:
                    g[k][str(F + 1)] = F
                if F > 1:
                    g[k][str(F - 1)] = 0

            for S in range(s):
                a, b, c = stdin.readline().strip().split(' ')
                c = int(c)
                m = g[a].get(b, maxint)
                g[a][b] = c if c < m else m

            #print g

            x = bellman_ford(g, '1')
            fil.write("Case #{0}: {1}\n".format(T, x[str(f)]))

        fil.close()

    stdin.close()