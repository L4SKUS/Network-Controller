import requests
import json

f = open(requests.get("http://192.168.8.166:8181/onos/v1/devices" , auth=("karaf", "karaf")))
response4 = json.load(f)
#response4 = {'devices': [{'id': 'of:000000000000000a', 'type': 'SWITCH', 'available': True, 'role': 'MASTER', 'mfr': 'Nicira, Inc.', 'hw': 'Open vSwitch', 'sw': '2.13.1', 'serial': 'None', 'driver': 'ovs', 'chassisId': 'a', 'lastUpdate': '1668880972572', 'humanReadableLastUpdate': 'connected 14m22s ago', 'annotations': {'channelId': '192.168.8.166:36696', 'managementAddress': '192.168.8.166', 'protocol': 'OF_14'}}, {'id': 'of:0000000000000003', 'type': 'SWITCH', 'available': True, 'role': 'MASTER', 'mfr': 'Nicira, Inc.', 'hw': 'Open vSwitch', 'sw': '2.13.1', 'serial': 'None', 'driver': 'ovs', 'chassisId': '3', 'lastUpdate': '1668880972773', 'humanReadableLastUpdate': 'connected 14m21s ago', 'annotations': {'channelId': '192.168.8.166:36694', 'managementAddress': '192.168.8.166', 'protocol': 'OF_14'}}, {'id': 'of:0000000000000004', 'type': 'SWITCH', 'available': True, 'role': 'MASTER', 'mfr': 'Nicira, Inc.', 'hw': 'Open vSwitch', 'sw': '2.13.1', 'serial': 'None', 'driver': 'ovs', 'chassisId': '4', 'lastUpdate': '1668880973437', 'humanReadableLastUpdate': 'connected 14m21s ago', 'annotations': {'channelId': '192.168.8.166:36706', 'managementAddress': '192.168.8.166', 'protocol': 'OF_14'}}, {'id': 'of:0000000000000001', 'type': 'SWITCH', 'available': True, 'role': 'MASTER', 'mfr': 'Nicira, Inc.', 'hw': 'Open vSwitch', 'sw': '2.13.1', 'serial': 'None', 'driver': 'ovs', 'chassisId': '1', 'lastUpdate': '1668880972173', 'humanReadableLastUpdate': 'connected 14m22s ago', 'annotations': {'channelId': '192.168.8.166:36690', 'managementAddress': '192.168.8.166', 'protocol': 'OF_14'}}, {'id': 'of:0000000000000002', 'type': 'SWITCH', 'available': True, 'role': 'MASTER', 'mfr': 'Nicira, Inc.', 'hw': 'Open vSwitch', 'sw': '2.13.1', 'serial': 'None', 'driver': 'ovs', 'chassisId': '2', 'lastUpdate': '1668880973143', 'humanReadableLastUpdate': 'connected 14m21s ago', 'annotations': {'channelId': '192.168.8.166:36698', 'managementAddress': '192.168.8.166', 'protocol': 'OF_14'}}, {'id': 'of:0000000000000007', 'type': 'SWITCH', 'available': True, 'role': 'MASTER', 'mfr': 'Nicira, Inc.', 'hw': 'Open vSwitch', 'sw': '2.13.1', 'serial': 'None', 'driver': 'ovs', 'chassisId': '7', 'lastUpdate': '1668880973079', 'humanReadableLastUpdate': 'connected 14m21s ago', 'annotations': {'channelId': '192.168.8.166:36704', 'managementAddress': '192.168.8.166', 'protocol': 'OF_14'}}, {'id': 'of:0000000000000008', 'type': 'SWITCH', 'available': True, 'role': 'MASTER', 'mfr': 'Nicira, Inc.', 'hw': 'Open vSwitch', 'sw': '2.13.1', 'serial': 'None', 'driver': 'ovs', 'chassisId': '8', 'lastUpdate': '1668880972842', 'humanReadableLastUpdate': 'connected 14m21s ago', 'annotations': {'channelId': '192.168.8.166:36700', 'managementAddress': '192.168.8.166', 'protocol': 'OF_14'}}, {'id': 'of:0000000000000005', 'type': 'SWITCH', 'available': True, 'role': 'MASTER', 'mfr': 'Nicira, Inc.', 'hw': 'Open vSwitch', 'sw': '2.13.1', 'serial': 'None', 'driver': 'ovs', 'chassisId': '5', 'lastUpdate': '1668880973311', 'humanReadableLastUpdate': 'connected 14m21s ago', 'annotations': {'channelId': '192.168.8.166:36708', 'managementAddress': '192.168.8.166', 'protocol': 'OF_14'}}, {'id': 'of:0000000000000006', 'type': 'SWITCH', 'available': True, 'role': 'MASTER', 'mfr': 'Nicira, Inc.', 'hw': 'Open vSwitch', 'sw': '2.13.1', 'serial': 'None', 'driver': 'ovs', 'chassisId': '6', 'lastUpdate': '1668880972106', 'humanReadableLastUpdate': 'connected 14m22s ago', 'annotations': {'channelId': '192.168.8.166:36692', 'managementAddress': '192.168.8.166', 'protocol': 'OF_14'}}, {'id': 'of:0000000000000009', 'type': 'SWITCH', 'available': True, 'role': 'MASTER', 'mfr': 'Nicira, Inc.', 'hw': 'Open vSwitch', 'sw': '2.13.1', 'serial': 'None', 'driver': 'ovs', 'chassisId': '9', 'lastUpdate': '1668880973259', 'humanReadableLastUpdate': 'connected 14m21s ago', 'annotations': {'channelId': '192.168.8.166:36702', 'managementAddress': '192.168.8.166', 'protocol': 'OF_14'}}]}

device_IDs = []

for dictionary in response4['devices']:
    device_IDs.append(dictionary['id'])

f.close()

print(sorted(device_IDs))

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

