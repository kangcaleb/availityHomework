import csv

# Need an algorithm here

# 1. Prompt for csv
# 2. Read the header
# 3. Create a dictionary to hold insuranceCompony -> [] of rows in record
# 4. For each line in the csv, extract the insurance company. 
#       - add it as a key to the dict if it doesn't exit. if it does. add it to the list



# insuranceDict {
#   ins0: {
#       0 -> [],
#       1 -> []
#    },
#    ins1: {
#       0 -> [],
#       1 -> []
#     }
# }

#fileString = input('Enter a file: ')
#csvFile = open(fileString, 'r')
csvFile = open('data.csv', 'r')

reader = csv.reader(csvFile)
header = next(reader)

insuranceDict = {}

for row in reader:
    insurance = row[3]
    id = row[0]
    version = row[2]


    if insurance not in insuranceDict:
        insuranceDict[insurance] = {}
        # we have not seen this insurance company so create new entry in dict
    
    if id not in insuranceDict[insurance]:
        insuranceDict[insurance][id] = row
    else: # we have multiple userid in dictionary, so only replace it if we have a higher version
        if version > insuranceDict[insurance][id][2]:
            insuranceDict[insurance][id] = row

for insurance, usersDict in insuranceDict.items():
    users = list(usersDict.values())
    users.sort(key=lambda x:x[1])

    file = open(insurance+'.csv', 'w')
    for user in users:
        row = ''.join(user)
        file.write(row +'\n')

    file.close()