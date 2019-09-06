import configparser
import csv
import sys
import re


def removeDuplicates(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

# prep master-raw.conf 
print(sys.argv[1])
with open(sys.argv[1], 'r') as master:
    content = master.read()

cleanedContent = re.sub(r'\\$', '', content)
# print(cleanedContent)

with open('master-python.conf', 'w', newline='') as masterPython:
    masterPython.write(cleanedContent)

# # 1. Read all headers & values and save into an array (COMPLETED)
# config = configparser.RawConfigParser(strict=False)
# conf = config.read("master-python.conf")

# # Save all properties from all sections
# searches = []
# headers = []
# values = []

# for section in config.sections():
#     searches.append(section)
#     for property in config[section]:
#         # print(property + " = " + config[section][property])
#         headers.append(property)
#         values.append(config[section][property])

# # 2. Remove duplicates in the headers (COMPLETED)
# uniqueHeaders = removeDuplicates(headers)

# # print("**********DEBUG**********")
# # print("Number of sections extracted: ", len(searches))
# # print(searches)
# # print("There are a total of", len(headers), "headers extracted:")
# # print(headers)
# # print("Here are the respective values:")
# # for key in range(len(headers)):
# #     print(headers[key], ": ", values[key])
# # print("There are a total of", len(uniqueHeaders), "uniqueHeaders extracted:")
# # print(uniqueHeaders)
# # print("**********End of DEBUG**********")

# # Assign all unique header names as field names to csv
# #   Add section name into fieldnames
# uniqueHeaders.insert(0, "section.name")

# # Create CSV file with appropriate headers
# with open('result.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=uniqueHeaders)
#     writer.writeheader()
