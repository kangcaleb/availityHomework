import csv

fileString = input('Enter a file: ')
csvFile = open(fileString, 'r')

reader = csv.reader(csvFile)
header = next(reader)

insuranceDict = {}

for row in reader:
    insurance = row[3]
    id = row[0]
    version = int(row[2])

    if insurance not in insuranceDict:
        insuranceDict[insurance] = {}
    
    if id not in insuranceDict[insurance]:
        insuranceDict[insurance][id] = row
    else:
        if version > int(insuranceDict[insurance][id][2]):
            insuranceDict[insurance][id] = row

for insurance, usersDict in insuranceDict.items():
    users = list(usersDict.values())
    users.sort(key=lambda x:x[1])

    separator = ','
    file = open(insurance+'.csv', 'w')
    file.write(separator.join(header))
    file.write('\n')

    for user in users:
        row = separator.join(user)
        file.write(row +'\n')

    file.close()

print('Done')