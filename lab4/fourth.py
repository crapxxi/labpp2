import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print('='*90)
print("Interface Status")

print("Total count: " + str(data.get("totalCount")))
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<6}")
print('-'*50 + ' ' + '-'*20 + ' ' +'-'*10 + ' ' + '-'*6)
idata = data.get("imdata", [])
for info in idata:
    phinfo = info.get("l1PhysIf")
    attr = phinfo.get("attributes")    
    dn = attr.get('dn','')
    desc = attr.get('descr', '')
    speed = attr.get('speed','')
    mtu = attr.get('mtu','')
    print(f"{dn:<50} {desc:<20} {speed:<10} {mtu:<6}")