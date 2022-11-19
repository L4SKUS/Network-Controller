import requests

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

# Część 5:
# Wysyła żądanie o wysłanie pakietów najlepszą drogą
