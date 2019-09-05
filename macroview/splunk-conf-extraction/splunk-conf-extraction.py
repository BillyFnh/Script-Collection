import configparser
import csv


# Steps for extracting .conf content into csv:
# 1. Read all sections, headers & values and save into an array
# 2. Configure CSV headers with uniqueHeaders.insert(0, "section.name") (uniqueHeaders = headers with duplicates removed)
# 3. Write to CSV section by section (each section is one row) with csv.Dictwriter
# 4. Loop through headers & values again and write (writerow with Dictwriter) them into csv according to field names


def removeDuplicates(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

# 1. Read all headers & values and save into an array (COMPLETED)
config = configparser.RawConfigParser()
conf = config.read("single-section.conf")

# Save all properties from all sections
searches = []
headers = []
values = []

for section in config.sections():
    # print("[" + section + "]")
    searches.append(section)
    for property in config[section]:
        # print(property + " = " + config[section][property])
        headers.append(property)
        values.append(config[section][property])

# 2. Remove duplicates in the variable (COMPLETED)
uniqueHeaders = removeDuplicates(headers)

# print("**********DEBUG**********")
# print("There are a total of", len(headers), "headers extracted:")
# print(headers)
# print("Here are the respective values:")
# for key in range(len(headers)):
#     print(headers[key], ": ", values[key])
# print("There are a total of", len(uniqueHeaders), "uniqueHeaders extracted:")
# print(uniqueHeaders)
# print("**********End of DEBUG**********")

# Generate section dictionary
propertyDic = dict(zip(headers, values))

# print("**********DEBUG**********")
# print(propertyDic)
# print("**********End of DEBUG**********")

# Assign all unique header names as field names to csv
#   Add section name into fieldnames
uniqueHeaders.insert(0, "section.name")

# Create CSV file with appropriate headers
# with open('result.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=uniqueHeaders)
#     writer.writeheader()
    # writer.writerow(propertyDic)

# Write 1 section into CSV in a row
with open('result.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=uniqueHeaders)
    writer.writerow(propertyDic)