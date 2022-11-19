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
class dane(object):
  def __init__(self, v, p, d):
    self.odwiedzony = v
    self.poprzednik = p
    self.dystans = d
def szukajMinimum(tab):
  min = -1
  mindist = sys.maxsize
  for i in range(0, len(macierz)):
    if ((not tab[i].odwiedzony) and tab[i].dystans < mindist):
      min = i
      mindist = tab[i].dystans
  return min
def Dijkstra(macierz, start):
  tab = []
  for i in range(0, len(macierz)):
    tab.append(dane(False, -1, sys.maxsize))
  tab[start].dystans = 0
  u = start
  while(u != -1):
    tab[u].odwiedzony = True
    for i in range(0, len(macierz)):
      if (macierz[u][i] > 0 and tab[u].dystans + macierz[u][i] < tab[i].dystans):
        tab[i].dystans = tab[u].dystans + macierz[u][i]
        tab[i].poprzednik = u
    u = szukajMinimum(tab)
  return tab


n = int(input('Podaj ile węzłów ma graf\n n = '))
s = int(input('Podaj węzeł startowy\n s = '))
print('Podaj elementy macierzy:')
macierz = []
for i in range(0, n):
    tab = [int(x) for x in input().split()]
    macierz.append(tab)

tab = Dijkstra(macierz, s)
for i in range(0, n):
    wypiszDane(i, tab[i])
def wypiszDane(i, d):
  txt = str(i) + "\t"
  if (not d.odwiedzony):
    txt += "nieodwiedzony"
  else:
    if (d.poprzednik == -1):
      txt += "brak"
    else:
      txt += str(d.poprzednik)
    txt += "\t" + str(d.dystans)
  print(txt);


# Część 5:
# Wysyła żądanie o wysłanie pakietów najlepszą drogą
