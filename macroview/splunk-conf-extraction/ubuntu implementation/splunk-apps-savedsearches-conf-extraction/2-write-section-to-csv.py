import configparser
import csv
import sys
import re


def removeDuplicates(duplicate):
    final_list = []
    for datamodel in duplicate:
        if datamodel not in final_list and datamodel != "as data" and datamodel != "OUTPUT datamodel" and datamodel != "size" and datamodel != "mvdedup(datamodel" and datamodel != "name type" and datamodel != "app" and datamodel != "app size":
            final_list.append(datamodel)
    return final_list


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

# Extract datamodels used from search string
propertyDic["datamodel.without.duplicates"] = removeDuplicates(re.findall("datamodel[:=\s(]\"?(\w+\"?.?\"?\w+)", propertyDic["search"]))
propertyDic["datamodel.with.duplicates"] = re.findall("datamodel[:=\s(]\"?(\w+\"?.?\"?\w+)", propertyDic["search"])
propertyDic["datamodel.with.duplicates.count"] = len(propertyDic["datamodel.with.duplicates"])
propertyDic["datamodel.without.duplicates.count"] = len(propertyDic["datamodel.without.duplicates"])

# print(propertyDic["datamodel.count"])

# include new fields to represent datamodel name, and subset name

# read fieldnames from csv
with open('../result.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames

# append csv with current section
with open('../result.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(propertyDic)