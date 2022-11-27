import math
import requests
import json

# KOMENTARZ 1
# aplikacja wczytuje informacje o wezlach i lączach sieci

response2 = requests.get("http://192.168.8.172:8181/onos/v1/hosts", auth=("karaf", "karaf"))
response3 = requests.get("http://192.168.8.172:8181/onos/v1/links", auth=("karaf", "karaf"))


# KOMENTARZ 2
# funkcja definiujaca algorytm wyznaczajacy najbardziej optymalna droga

def algorithm(source, destination):
    graph = {
        'Warszawa': {'Krakow': 1.78, 'Lodz': 0.84, 'Bydgoszcz': 1.6, 'Lublin': 1.08, 'Gdansk': 2},
        'Krakow': {'Katowice': 0.49, 'Lodz': 1.36, 'Lublin': 1.6, 'Warszawa': 1.78},
        'Lodz': {'Warszawa': 0.84, 'Krakow': 1.36, 'Wroclaw': 1.29, 'Bydgoszcz': 1.27},
        'Bydgoszcz': {'Warszawa': 1.6, 'Lodz': 1.27, 'Gdansk': 1.01, 'Poznan': 0.75, 'Szczecin': 1.64},
        'Lublin': {'Warszawa': 1.08, 'Krakow': 1.6, },
        'Katowice': {'Krakow': 0.49, 'Wroclaw': 1.19},
        'Wroclaw': {'Katowice': 1.19, 'Lodz': 1.29, 'Poznan': 1.02},
        'Szczecin': {'Poznan': 3, 'Bydgoszcz': 1.64, 'Gdansk': 2.02},
        'Gdansk': {'Bydgoszcz': 1.01, 'Szczecin': 2.02, 'Warszawa': 2},
        'Poznan': {'Bydgoszcz': 0.75, 'Wroclaw': 1.02, 'Szczecin': 1.38},
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
    return route


# KOMENTARZ 3
# odpowiedzi otrzyamane po wykonaniu metody GET, z ktorych wyciągniete zostaną potrzebne informacje o topologii sieci


response_links = response3.json()
response_hosts = response2.json()
miasta = [
    {'nazwa': 'Warszawa', 'IPv4': '10.0.0.1/32', 'switch': 'of:0000000000000001'},
    {'nazwa': 'Krakow', 'IPv4': '10.0.0.2/32', 'switch': 'of:0000000000000002'},
    {'nazwa': 'Lodz', 'IPv4': '10.0.0.3/32', 'switch': 'of:0000000000000003'},
    {'nazwa': 'Bydgoszcz', 'IPv4': '10.0.0.4/32', 'switch': 'of:0000000000000004'},
    {'nazwa': 'Lublin', 'IPv4': '10.0.0.5/32', 'switch': 'of:0000000000000005'},
    {'nazwa': 'Katowice', 'IPv4': '10.0.0.6/32', 'switch': 'of:0000000000000006'},
    {'nazwa': 'Wroclaw', 'IPv4': '10.0.0.7/32', 'switch': 'of:0000000000000007'},
    {'nazwa': 'Szczecin', 'IPv4': '10.0.0.8/32', 'switch': 'of:0000000000000008'},
    {'nazwa': 'Gdansk', 'IPv4': '10.0.0.9/32', 'switch': 'of:0000000000000009'},
    {'nazwa': 'Poznan', 'IPv4': '10.0.0.10/32', 'switch': 'of:000000000000000a'},
]


# KOMENTARZ 4
# funkcja tworzaca pliki json oraz wysylajace okreslone zasady przeplywu pakietow

def tworzenie_jsona(deviceId, IN_PORT, OUTPUT, IPv4, nazwa):
    with open("Onos2.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['deviceId'] = deviceId
        data['treatment']['instructions'][0]['port'] = OUTPUT
        data['selector']['criteria'][0]['port'] = IN_PORT
        data['selector']['criteria'][2]['ip'] = IPv4
    with open(nazwa, "w") as jsonFile:
        json.dump(data, jsonFile)
    url = 'http://192.168.8.172:8181/onos/v1/flows/' + deviceId
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    r = requests.post(url, auth=("karaf", "karaf"), data=open(nazwa, 'rb'), headers=headers)
    if 200 <= r.status_code <= 299:
        print(r.text , r.status_code , " Success!")
    else:
        print('Boo!')


# KOMENTARZ 5
# funkcja tworzaca okreslone zasady przeplywu zapisaywane do plikow json dla konkretnych switchy


def POST(trasa):
    port_host_src = 404
    port_host_dst = 404
    ip_host_src = 404
    ip_host_dst = 404

    lista_switchy = []

    for przystanek in trasa:
        for miasto in miasta:
            if przystanek == miasto['nazwa']:
                lista_switchy.append(miasto['switch'])

    for miasto in miasta:
        if miasto['nazwa'] == trasa[0]:
            ip_host_src = miasto['IPv4']
            for element in response_hosts['hosts']:
                if element['locations'][0]['elementId'] == miasto['switch']:
                    port_host_src = element['locations'][0]['port']
        if miasto['nazwa'] == trasa[::-1][0]:
            ip_host_dst = miasto['IPv4']
            for element in response_hosts['hosts']:
                if element['locations'][0]['elementId'] == miasto['switch']:
                    port_host_dst = element['locations'][0]['port']

    for i in range(len(trasa)):
        # pierwszy switch
        if i == 0:
            port_in = port_host_src
            port_out = 404
            for link in response_links['links']:
                if link['src']['device'] == lista_switchy[i] and link['dst']['device'] == lista_switchy[i + 1]:
                    port_out = link['src']['port']
            tworzenie_jsona(lista_switchy[i], port_in, port_out, ip_host_dst, 'src_sent.json')
            tworzenie_jsona(lista_switchy[i], port_out, port_in, ip_host_src, 'src_rec.json')


        # ostatni switch
        elif i == len(trasa) - 1:
            port_out = port_host_dst
            port_in = 404
            for link in response_links['links']:
                if link['src']['device'] == lista_switchy[i - 1] and link['dst']['device'] == lista_switchy[i]:
                    port_in = link['dst']['port']
            tworzenie_jsona(lista_switchy[i], port_in, port_out, ip_host_dst, 'dst_sent.json')
            tworzenie_jsona(lista_switchy[i], port_out, port_in, ip_host_src, 'dst_rec.json')

        # srodkowe switche
        else:
            port_in = 404
            port_out = 404
            for link in response_links['links']:
                if link['src']['device'] == lista_switchy[i - 1] and link['dst']['device'] == lista_switchy[i]:
                    port_in = link['dst']['port']
                if link['src']['device'] == lista_switchy[i] and link['dst']['device'] == lista_switchy[i + 1]:
                    port_out = link['src']['port']
            tworzenie_jsona(lista_switchy[i], port_in, port_out, ip_host_dst, str(i) + 'sent.json')
            tworzenie_jsona(lista_switchy[i], port_out, port_in, ip_host_src, str(i) + 'rec.json')


if __name__ == '__main__':

    # KOMENTARZ 6
    # wywolanie funkcji, w pierwszej kolejnosci uzytkownik jest proszony o podanie trasy z jednego miasta do drugiego oraz wielkosci strumienia danych,
    # nastepnie tworzone sa pliki json i wyslane za pomoca metody POST
    iletras = int(input("Podaj ilość tras Któymi wysłane zostaną pakiety: "))
    while (iletras > 0):
        print("Wybierz miasto początkowe oraz miasto docelowe."
              "Twoje miasta do wyboru to: Warszawa, Krakow, Lodz, Bydgoszcz, Lublin, Katowice, Wroclaw, Szczecin, Gdansk, "
              "Poznan")
        miasto1 = input("Miasto początkowe: ")
        miasto2 = input("Miasto docelowe: ")
        print("Wybrałes trasę z miasta " + miasto1 + " do miasta " + miasto2)
        route = algorithm(miasto1, miasto2)
        print("Najkrotsza trasa:")
        print(route)
        POST(route)
        iletras -= 1
