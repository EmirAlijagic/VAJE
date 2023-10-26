import json

with open('C:/Users/ekobe/OneDrive/Namizje/DN3/zacetniData.json', 'r') as f:
    zacetniData = json.load(f)

with open('C:/Users/ekobe/OneDrive/Namizje/DN3/updateData.json', 'r') as f:
    updateData = json.load(f)

zacetniSlovar = [x for x in zacetniData['persons']]

i = 0
for x in updateData['persons']:
    if (x['name'] == zacetniData['persons'][i]['name']):
        zacetniSlovar[i].update(updateData['persons'][i])
    i = i+1

with open('C:/Users/ekobe/OneDrive/Namizje/DN3/koncniData.json', 'w') as f:
    json.dump(zacetniData, f, indent=2)
