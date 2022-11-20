import sys
import json
import requests
import bootle
import math

# Część 1:
# wczyatnie z pliku informacji o węzłach i łączach(wysyła żadanie GET, aby dostac informacje)

# response = requests.get("http://192.168.8.166:8181/onos/v1/flows", auth=("karaf", "karaf"))
# response2 = requests.get("http://192.168.8.166:8181/onos/v1/hosts", auth=("karaf", "karaf"))
# response3 = requests.get("http://192.168.8.166:8181/onos/v1/links", auth=("karaf", "karaf"))
# response4 = requests.get("http://192.168.8.166:8181/onos/v1/devices", auth=("karaf", "karaf"))
#
# # odpowiedni sposób przechowania informacji o węzłach i łączach
# # devices id
# device_IDs = []
# for dictionary in response4.json()['devices']:
#     device_IDs.append(dictionary['id'])
# print("Devices id:"+ device_IDs)
# #links


#print(sorted(device_IDs))
# Część 3:
# żądanie użytkownika skąd i gdzie chce wysłać pakiety
print("Wybierz miasto,z którego wyslesz pakiety oraz miasto docelowe")
miasto1 = input("Miasto wysyłające pakiety: ")
miasto2 = input("Miasto odbierające pakiety: ")
print("Wybrałes drogę z miasta " + miasto1 + " do miasta  " + miasto2)

Warszawa = '10.0.0.1'
Krakow = '10.0.0.2'
Lodz = '10.0.0.3'
Bydgoszcz = '10.0.0.4'
Lublin = '10.0.0.5'
Katowice = '10.0.0.6'
Wroclaw = '10.0.0.7'
Szczecin = '10.0.0.8'
Gdansk = '10.0.0.9'
Poznan = '10.0.0.10'


# Część 4:
# Wyznaczenie najbardziej optymalnej ścieżki za pomocą algorytmu
# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
def algorithm(source, destination):
    graph = {
        'Warszawa': {'Krakow': 1.78, 'Lodz': 0.84, 'Bydgoszcz':1.6,'Lublin':1.08,'Gdansk':2},
        'Krakow': {'Katowice': 0.49, 'Lodz': 1.36, 'Lublin': 1.6,'Warszawa':1.78},
        'Lodz': {'Warszawa': 0.84,'Krakow': 1.36,'Wroclaw': 1.29,'Bydgoszcz': 1.27},
        'Bydgoszcz': {'Warszawa': 1.6,'Lodz': 1.27,'Gdansk': 1.01,'Poznan': 0.75,'Szczecin':1.64},
        'Lublin': {'Warszawa': 1.08,'Krakow': 1.6,},
        'Katowice': {'Krakow': 0.49, 'Wroclaw': 1.19},
        'Wroclaw': {'Katowice': 1.19, 'Lodz': 1.29, 'Poznan': 1.02},
        'Szczecin': {'Poznan': 3, 'Bydgoszcz': 1.64, 'Gdansk': 2.02},
        'Gdansk': {'Bydgoszcz': 1.01, 'Szczecin': 2.02,'Warszawa':2},
        'Poznan': {'Bydgoszcz': 0.75, 'Wroclaw': 1.02, 'Szczecin':1.38},
        }


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

algorithm(miasto1,miasto2)
# Część 5:
# Wysyła żądanie o wysłanie pakietów najlepszą drogą
