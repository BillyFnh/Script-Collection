import configparser
import csv
import sys

# read conf file and store into dictionary
config = configparser.RawConfigParser(strict=False)
conf = config.read(sys.argv[1])

sectionName = []
headers = []
values = []

for section in config.sections():
    # print("Processing: [" + section + "]")
    sectionName.append(section)
    for property in config[section]:
        # print(property + " = " + config[section][property])
        headers.append(property)
        values.append(config[section][property])

# Generate section dictionary
propertyDic = dict(zip(headers, values))
propertyDic["section.name"] = sectionName

# read fieldnames from csv
with open('../result.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames

# append csv with current section
with open('../result.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(propertyDic)
