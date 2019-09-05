import configparser
import csv
import json

# Steps for extracting .conf content into csv:
# 1. Read all sections, headers & values and save into an array
# 2. Configure CSV headers with uniqueHeaders.insert(0, "section.name") (uniqueHeaders = headers with duplicates removed)
# 3. Write to CSV section by section (each section is one row) with csv.Dictwriter
# 4. Loop through headers & values again and write (writerow with Dictwriter) them into csv according to field names


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

# 2. Remove duplicates in the variable (In Process)


def removeDuplicates(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

print("**********DEBUG**********")
print("There are a total of", len(headers), "headers extracted:")
# print(headers)
uniqueHeaders = removeDuplicates(headers)
# print("Here are the respective values:")
# for key in range(len(headers)):
#     print(headers[key], ": ", values[key])
print("There are a total of", len(uniqueHeaders), "uniqueHeaders extracted:")
# print(uniqueHeaders)
print("**********End of DEBUG**********")


# 3. Assign all unique header names as field names to csv

# 4. Loop through headers & values again and write (writerow with Dictwriter) them into csv according to field names
# refernce: https://docs.python.org/3/library/csv.html

# turn uniqueheaders and values into key value pairs grouped with section names
#   e.g. 403_by_clientip = {
#   'action.email.useNSSubject': 1,
#   'alert.track':  0
#   }
propertyDic = dict(zip(headers, values))

print("**********DEBUG**********")
print(propertyDic)
print("**********End of DEBUG**********")

# Add section name into fieldnames
uniqueHeaders.insert(0, "section.name")

# Create CSV file with appropriate headers
# with open('result.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=uniqueHeaders)
#     writer.writeheader()
    # writer.writerow(propertyDic)

# Append CSV file new entry of section, following the same fieldname order
with open('result.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=uniqueHeaders)
    writer.writerow(propertyDic)



# # Write all key pair values into csv 
# config = configparser.RawConfigParser()
# with open('result.csv', mode='w') as result_file:
#     result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     # Read .conf file
#     conf = config.read("searchLocalsavedsearches.conf")

#     # Print all properties from all sections
#     searches = []
#     headers = []
#     values = []

#     for section in config.sections():
#         # print("[" + section + "]")
#         searches.append(section)
#         for property in config[section]:
#             # print(property + " = " + config[section][property])
#             headers.append(property)
#             values.append(config[section][property])
#         # print(values)

#     result_writer.writerow(headers)
#     result_writer.writerow(values)