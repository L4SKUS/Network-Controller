import bootle
import requests
# Część 1:
# wczyatnie z pliku informacji o węzłach i łączach(wysyła żadanie GET, aby dostac informacje)

response = requests.get("http://192.168.8.166:8181/onos/v1/flows" , auth=("karaf", "karaf"))
response2 = requests.get("http://192.168.8.166:8181/onos/v1/hosts" , auth=("karaf", "karaf"))
response3 = requests.get("http://192.168.8.166:8181/onos/v1/links" , auth=("karaf", "karaf"))

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

# odpowiedni sposób przechowania informacji o węzłach i łączach


# Część 3:
# żądanie użytkownika skąd i gdzie chce wysłać pakiety


# Część 4:
# Wyznaczenie najbardziej optymalnej ścieżki za pomocą algorytmu

# Część 5:
# Wysyła żądanie o wysłanie pakietów najlepszą drogą