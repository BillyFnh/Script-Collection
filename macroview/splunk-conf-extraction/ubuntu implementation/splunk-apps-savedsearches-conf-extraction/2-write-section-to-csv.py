import configparser
import csv
import sys

# read conf file and store into dictionary
config = configparser.RawConfigParser(strict=False)
conf = config.read(sys.argv[1])
# Save all properties from all sections
sectionName = []
headers = []
values = []

for section in config.sections():
    print("[" + section + "]")
    sectionName.append(section)
    for property in config[section]:
        # print(property + " = " + config[section][property])
        headers.append(property)
        values.append(config[section][property])


# print("**********DEBUG**********")
# print("There are a total of", len(headers), "headers extracted:")
# # print(headers)
# print("Here are the respective values:")
# for key in range(len(headers)):
#     print(headers[key], ": ", values[key])

# for elements in range(len(sys.argv)):
#     print(elements, ": ", sys.argv[elements])

# print(sys.argv[1])
# print(sys.argv[2:13])
# print("**********End of DEBUG**********")

# Generate section dictionary
propertyDic = dict(zip(headers, values))
propertyDic["section.name"] = sectionName

# read fieldnames from csv
with open('../result.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames

# append csv with current section (BUG: Need to handle special character *, check cron_schedle: */5 * * * *  )
with open('../result.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(propertyDic)
