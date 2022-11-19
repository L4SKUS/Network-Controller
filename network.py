import sys
import json
import requests
import bootle

# Część 1:
# wczyatnie z pliku informacji o węzłach i łączach(wysyła żadanie GET, aby dostac informacje)

response = requests.get("http://192.168.8.166:8181/onos/v1/flows", auth=("karaf", "karaf"))
response2 = requests.get("http://192.168.8.166:8181/onos/v1/hosts", auth=("karaf", "karaf"))
response3 = requests.get("http://192.168.8.166:8181/onos/v1/links", auth=("karaf", "karaf"))
response4 = requests.get("http://192.168.8.166:8181/onos/v1/devices", auth=("karaf", "karaf"))
response5 = requests.get("http://192.168.8.166:8181/onos/v1/flows/of:0000000000000002", auth=("karaf", "karaf"))

if (response.status_code == 200):
    print("The request was a success!")
    print(response.json())
elif (response.status_code == 404):
    print("Result not found!")

if (response2.status_code == 200):
    print("The request was a success!")
    print(response2.json())
elif (response2.status_code == 404):
    print("Result not found!")

if (response3.status_code == 200):
    print("The request was a success!")
    print(response3.json())
elif (response3.status_code == 404):
    print("Result not found!")

if (response4.status_code == 200):
    print("The request was a success!")
    print(response4.json())
elif (response4.status_code == 404):
    print("Result not found!")

if (response5.status_code == 200):
    print("The request was a success!")
    print(response5.json())
elif (response5.status_code == 404):
    print("Result not found!")

# odpowiedni sposób przechowania informacji o węzłach i łączach
response4.json()
device_IDs = []

for dictionary in response4.json()['devices']:
    device_IDs.append(dictionary['id'])

print(sorted(device_IDs))
# Część 3:
# żądanie użytkownika skąd i gdzie chce wysłać pakiety
print("Witaj Arturze, wybierz miasto,z którego wyslesz pakiety oraz miasto docelowe")
miasto1 = input("Miasto pierwsze: ")
miasto2 = input("Miasto drugie: ")
print("Wybrałes drogę z miasta "+ miasto1 + " do miasta  "+ miasto2)

Warszawa = '10.0.0.1'
Krakow = '10.0.0.2'
Lodz = '10.0.0.3'
Bydgoszcz ='10.0.0.4'
Lublin ='10.0.0.5'
Katowice ='10.0.0.6'
Wroclaw ='10.0.0.7'
Szczecin ='10.0.0.8'
Gdansk ='10.0.0.9'
Poznan ='10.0.0.10'


# Część 4:
# Wyznaczenie najbardziej optymalnej ścieżki za pomocą algorytmu
# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex \t Distance from Source")
		for node in range(self.V):
			print(node, "\t\t", dist[node])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = 1e7

		# Search not nearest vertex not in the
		# shortest path tree
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	# Function that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minDistance(dist, sptSet)

			# Put the minimum distance vertex in the
			# shortest path tree
			sptSet[u] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)

# Driver program
g = Graph(10)

g.graph = [[0, 1.78, 0.84, 1.60, 1.08, 0, 0, 0, 2.00, 0],
           [1.78, 0, 1.36, 0, 1.60, 0.49, 0, 0, 0, 0],
           [0.84, 1.36, 0, 1.27, 0, 0, 1.29, 0, 0, 0],
           [1.60, 0, 1.27, 0, 0, 0, 0, 1.64, 1.01, 0.75],
           [1.08, 1.60, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0.49, 0, 0, 0, 0, 1.19, 0, 0, 0],
           [0, 0, 1.29, 0, 0, 1.19, 0, 0, 0, 1.02],
           [0, 0, 0, 1.64, 0, 0, 0, 0, 2.02, 1.38],
           [2.00, 0, 0, 1.01, 0, 0, 0, 2.02, 0, 0],
           [0, 0, 0, 0.75, 0, 0, 1.02, 1.38, 0, 0]
           ]

g.dijkstra(4)






# Część 5:
# Wysyła żądanie o wysłanie pakietów najlepszą drogą
