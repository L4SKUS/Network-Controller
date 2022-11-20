import requests
import json

response_links = {'links': [{'src': {'port': '2', 'device': 'of:0000000000000004'}, 'dst': {'port': '1', 'device': 'of:0000000000000008'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '2', 'device': 'of:0000000000000002'}, 'dst': {'port': '1', 'device': 'of:0000000000000006'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '3', 'device': 'of:0000000000000004'}, 'dst': {'port': '1', 'device': 'of:0000000000000009'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '2', 'device': 'of:0000000000000007'}, 'dst': {'port': '1', 'device': 'of:000000000000000a'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '5', 'device': 'of:0000000000000001'}, 'dst': {'port': '2', 'device': 'of:0000000000000009'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '2', 'device': 'of:000000000000000a'}, 'dst': {'port': '5', 'device': 'of:0000000000000004'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '2', 'device': 'of:0000000000000009'}, 'dst': {'port': '5', 'device': 'of:0000000000000001'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '1', 'device': 'of:000000000000000a'}, 'dst': {'port': '2', 'device': 'of:0000000000000007'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '1', 'device': 'of:0000000000000009'}, 'dst': {'port': '3', 'device': 'of:0000000000000004'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '1', 'device': 'of:0000000000000008'}, 'dst': {'port': '2', 'device': 'of:0000000000000004'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '1', 'device': 'of:0000000000000006'}, 'dst': {'port': '2', 'device': 'of:0000000000000002'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '4', 'device': 'of:0000000000000004'}, 'dst': {'port': '4', 'device': 'of:0000000000000003'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '3', 'device': 'of:0000000000000003'}, 'dst': {'port': '3', 'device': 'of:0000000000000002'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '1', 'device': 'of:0000000000000001'}, 'dst': {'port': '1', 'device': 'of:0000000000000002'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '3', 'device': 'of:0000000000000007'}, 'dst': {'port': '2', 'device': 'of:0000000000000006'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '3', 'device': 'of:0000000000000009'}, 'dst': {'port': '2', 'device': 'of:0000000000000008'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '2', 'device': 'of:0000000000000006'}, 'dst': {'port': '3', 'device': 'of:0000000000000007'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '2', 'device': 'of:0000000000000008'}, 'dst': {'port': '3', 'device': 'of:0000000000000009'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '2', 'device': 'of:0000000000000001'}, 'dst': {'port': '1', 'device': 'of:0000000000000003'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '3', 'device': 'of:0000000000000001'}, 'dst': {'port': '1', 'device': 'of:0000000000000004'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '2', 'device': 'of:0000000000000003'}, 'dst': {'port': '1', 'device': 'of:0000000000000007'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '4', 'device': 'of:0000000000000002'}, 'dst': {'port': '2', 'device': 'of:0000000000000005'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '4', 'device': 'of:0000000000000001'}, 'dst': {'port': '1', 'device': 'of:0000000000000005'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '3', 'device': 'of:0000000000000008'}, 'dst': {'port': '3', 'device': 'of:000000000000000a'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '5', 'device': 'of:0000000000000004'}, 'dst': {'port': '2', 'device': 'of:000000000000000a'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '3', 'device': 'of:000000000000000a'}, 'dst': {'port': '3', 'device': 'of:0000000000000008'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '1', 'device': 'of:0000000000000005'}, 'dst': {'port': '4', 'device': 'of:0000000000000001'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '2', 'device': 'of:0000000000000005'}, 'dst': {'port': '4', 'device': 'of:0000000000000002'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '1', 'device': 'of:0000000000000004'}, 'dst': {'port': '3', 'device': 'of:0000000000000001'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '1', 'device': 'of:0000000000000007'}, 'dst': {'port': '2', 'device': 'of:0000000000000003'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '1', 'device': 'of:0000000000000003'}, 'dst': {'port': '2', 'device': 'of:0000000000000001'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '1', 'device': 'of:0000000000000002'}, 'dst': {'port': '1', 'device': 'of:0000000000000001'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '3', 'device': 'of:0000000000000002'}, 'dst': {'port': '3', 'device': 'of:0000000000000003'}, 'type': 'DIRECT', 'state': 'ACTIVE'}, {'src': {'port': '4', 'device': 'of:0000000000000003'}, 'dst': {'port': '4', 'device': 'of:0000000000000004'}, 'type': 'DIRECT', 'state': 'ACTIVE'}]}
response_hosts = {'hosts': [{'id': '4E:1C:87:4A:21:10/None', 'mac': '4E:1C:87:4A:21:10', 'vlan': 'None', 'innerVlan': 'None', 'outerTpid': '0x0000', 'configured': False, 'suspended': False, 'ipAddresses': [], 'locations': [{'elementId': 'of:0000000000000003', 'port': '5'}]}, {'id': '7E:85:B5:76:B6:E4/None', 'mac': '7E:85:B5:76:B6:E4', 'vlan': 'None', 'innerVlan': 'None', 'outerTpid': '0x0000', 'configured': False, 'suspended': False, 'ipAddresses': [], 'locations': [{'elementId': 'of:0000000000000006', 'port': '3'}]}, {'id': '5E:46:E2:07:97:53/None', 'mac': '5E:46:E2:07:97:53', 'vlan': 'None', 'innerVlan': 'None', 'outerTpid': '0x0000', 'configured': False, 'suspended': False, 'ipAddresses': [], 'locations': [{'elementId': 'of:0000000000000004', 'port': '6'}]}, {'id': '3E:43:17:DA:E3:CC/None', 'mac': '3E:43:17:DA:E3:CC', 'vlan': 'None', 'innerVlan': 'None', 'outerTpid': '0x0000', 'configured': False, 'suspended': False, 'ipAddresses': [], 'locations': [{'elementId': 'of:0000000000000008', 'port': '4'}]}, {'id': '92:75:AC:AF:88:EC/None', 'mac': '92:75:AC:AF:88:EC', 'vlan': 'None', 'innerVlan': 'None', 'outerTpid': '0x0000', 'configured': False, 'suspended': False, 'ipAddresses': [], 'locations': [{'elementId': 'of:0000000000000002', 'port': '5'}]}, {'id': 'C2:8A:BC:70:24:D9/None', 'mac': 'C2:8A:BC:70:24:D9', 'vlan': 'None', 'innerVlan': 'None', 'outerTpid': '0x0000', 'configured': False, 'suspended': False, 'ipAddresses': [], 'locations': [{'elementId': 'of:0000000000000001', 'port': '6'}]}, {'id': 'AA:D2:94:64:DB:DC/None', 'mac': 'AA:D2:94:64:DB:DC', 'vlan': 'None', 'innerVlan': 'None', 'outerTpid': '0x0000', 'configured': False, 'suspended': False, 'ipAddresses': [], 'locations': [{'elementId': 'of:0000000000000009', 'port': '4'}]}, {'id': '62:36:01:4C:AF:21/None', 'mac': '62:36:01:4C:AF:21', 'vlan': 'None', 'innerVlan': 'None', 'outerTpid': '0x0000', 'configured': False, 'suspended': False, 'ipAddresses': [], 'locations': [{'elementId': 'of:0000000000000005', 'port': '3'}]}, {'id': 'D6:45:3E:C8:CD:E7/None', 'mac': 'D6:45:3E:C8:CD:E7', 'vlan': 'None', 'innerVlan': 'None', 'outerTpid': '0x0000', 'configured': False, 'suspended': False, 'ipAddresses': [], 'locations': [{'elementId': 'of:000000000000000a', 'port': '4'}]}, {'id': 'F6:1F:BB:B1:F3:3E/None', 'mac': 'F6:1F:BB:B1:F3:3E', 'vlan': 'None', 'innerVlan': 'None', 'outerTpid': '0x0000', 'configured': False, 'suspended': False, 'ipAddresses': [], 'locations': [{'elementId': 'of:0000000000000007', 'port': '4'}]}]}

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


def tworzenie_jsona(deviceId, IN_PORT, OUTPUT, IPv4, nazwa):
    with open("Onos2.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data['deviceId'] = deviceId
        data['treatment']['instructions'][0]['port'] = OUTPUT
        data['selector']['criteria'][0]['port'] = IN_PORT
        data['selector']['criteria'][2]['ip'] = IPv4
    with open(nazwa, "w") as jsonFile:
        json.dump(data, jsonFile)


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
        #pierwszy switch
        if i == 0:
            port_in = port_host_src
            port_out = 404
            for link in response_links['links']:
                if link['src']['device'] == lista_switchy[i] and link['dst']['device'] == lista_switchy[i+1]:
                    port_out = link['src']['port']
            tworzenie_jsona(lista_switchy[i], port_in, port_out, ip_host_dst, 'src_sent.json')
            tworzenie_jsona(lista_switchy[i], port_out, port_in, ip_host_src, 'src_rec.json')


        #ostatni switch
        elif i == len(trasa)-1:
            port_out = port_host_dst
            port_in = 404
            for link in response_links['links']:
                if link['src']['device'] == lista_switchy[i-1] and link['dst']['device'] == lista_switchy[i]:
                    port_in = link['dst']['port']
            tworzenie_jsona(lista_switchy[i], port_in, port_out, ip_host_dst, 'dst_sent.json')
            tworzenie_jsona(lista_switchy[i], port_out, port_in, ip_host_src, 'dst_rec.json')

        #środkowe switche
        else:
            port_in = 404
            port_out = 404
            for link in response_links['links']:
                if link['src']['device'] == lista_switchy[i-1] and link['dst']['device'] == lista_switchy[i]:
                    port_in = link['dst']['port']
                if link['src']['device'] == lista_switchy[i] and link['dst']['device'] == lista_switchy[i+1]:
                    port_out = link['src']['port']
            tworzenie_jsona(lista_switchy[i], port_in, port_out, ip_host_dst, str(i)+'sent.json')
            tworzenie_jsona(lista_switchy[i], port_out, port_in, ip_host_src, str(i)+'rec.json')


if __name__ == '__main__':
    route = ['Szczecin', 'Bydgoszcz', 'Warszawa', 'Lublin']
    POST(route)






