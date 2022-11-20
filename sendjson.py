# url = 'http://192.168.8.166:8181/onos/v1/flows/'+ src_switch
# headers = {'Authorization' : ("karaf", "karaf")‘(’, 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
# r = requests.post(url, data=open('Onos2.json', 'rb'), headers=headers)
# response = requests.get("http://192.168.8.166:8181/onos/v1/flows", auth=("karaf", "karaf"))
#-d @Onos2.json -H "Content-Type: application/json" -H "Accept: application/json"
import json
jsonFile = open('Onos2.json')
data = json.load(jsonFile)
print(data)
