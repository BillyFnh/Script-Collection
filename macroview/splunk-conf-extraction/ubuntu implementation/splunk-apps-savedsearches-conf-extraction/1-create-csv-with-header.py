import configparser
import csv
import sys


def removeDuplicates(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

# 1. Read all headers & values and save into an array
config = configparser.RawConfigParser(strict=False)
conf = config.read("master.conf")

# Save all properties from all sections
searches = []
headers = []
values = []

for section in config.sections():
    searches.append(section)
    for property in config[section]:
        # print(property + " = " + config[section][property])
        headers.append(property)
        values.append(config[section][property])

# 2. Remove duplicates in the headers
uniqueHeaders = removeDuplicates(headers)

#   Add section name into fieldnames
uniqueHeaders.insert(0, "section.name")
uniqueHeaders.insert(0, "datamodel.with.duplicates")
uniqueHeaders.insert(0, "datamodel.without.duplicates")
uniqueHeaders.insert(0, "datamodel.with.duplicates.count")
uniqueHeaders.insert(0, "datamodel.without.duplicates.count")
# uniqueHeaders.insert(0, "splunk.app.name")

# Create CSV file with appropriate headers
with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=uniqueHeaders)
    writer.writeheader()
