#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

graph = {
    'a': {'b': 5, 'c': 2},
    'b': {'a': 5, 'c': 7, 'd': 8},
    'c': {
        'a': 2,
        'b': 7,
        'd': 4,
        'e': 8,
        },
    'd': {
        'b': 8,
        'c': 4,
        'e': 6,
        'f': 4,
        },
    'e': {'c': 8, 'd': 6, 'f': 3},
    'f': {'e': 3, 'd': 4},
    }

source = 'a'
destination = 'f'

unvisited = graph
shortest_distances = {}
route = []
path_nodes = {}

for nodes in unvisited:
    shortest_distances[nodes] = math.inf
shortest_distances[source] = 0

while unvisited:
    min_node = None
    for current_node in unvisited:
        if min_node is None:
            min_node = current_node
        elif shortest_distances[min_node] \
            > shortest_distances[current_node]:
            min_node = current_node
    for (node, value) in unvisited[min_node].items():
        if value + shortest_distances[min_node] \
            < shortest_distances[node]:
            shortest_distances[node] = value \
                + shortest_distances[min_node]
            path_nodes[node] = min_node
    unvisited.pop(min_node)
node = destination

while node != source:
    try:
        route.insert(0, node)
        node = path_nodes[node]
    except Exception:
        print('Path not reachable')
        break
route.insert(0, source)

if shortest_distances[destination] != math.inf:
    print('Shortest distance is ' + str(shortest_distances[destination]))
    print('And the path is ' + str(route))