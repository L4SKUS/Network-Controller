#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

graph = {
    'Warszawa': {'Krakow': 1.78, 'lodz': 0.84, 'Bydgoszcz':1.6,'Lublin':1.08,'Gdansk':2},
    'Krakow': {'Katowice': 0.49, 'Lodz': 1.36, 'Lublin': 1.6},
    'Lodz': {'Warszawa': 0.84,'Krakow': 1.36,'Wroclaw': 1.29,'Bydgoszcz': 1.27},
    'Bydgoszcz': {'Warszawa': 1.6,'Lodz': 1.27,'Gdansk': 1.01,'Poznan': 0.75,'Szczecin':1.64},
    'Katowice': {'Krakow': 0.49, 'Wroclaw': 1.19},
    'Wroclaw': {'Katowice': 1.19, 'Lodz': 1.29, 'Poznan': 1.02},
    'Szczecin': {'Poznan': 3, 'Bydgoszcz': 1.64, 'Gdansk': 2.02},
    'Gdansk': {'Bydgoszcz': 1.01, 'Szczecin': 2.02,'Warszawa':2},
    'Poznan': {'Bydgoszcz': 0.75, 'Wroclaw': 1.02, 'Szczecin':1.38},
    }

source = 'Lodz'
destination = 'Gdansk'

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