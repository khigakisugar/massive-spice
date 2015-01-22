import json, pprint

fh = open("/Users/khigaki/massive-spice/data/output.json")
totalData = json.load(fh)
fh.close()

validFields = {
    'description':True,
    'amount':True,
    #'base_rate':True,
    'amount_usdollar':True,
    'probability':True,
    'best_case':True,
    'worst_case':True
}
statuses = ['Closed Won', 'Closed Lost']
dropStatuses = []

for status in totalData.keys():
    if status not in statuses:
        dropStatuses.append(status)

for drop in dropStatuses:
    del totalData[drop]

dropFields = []
for field in totalData['Closed Won'].keys():
    try:
        validFields[field]
    except KeyError:
        dropFields.append(field)

for status in totalData.keys():
    for drop in dropFields:
        del totalData[status][drop]

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(totalData)
