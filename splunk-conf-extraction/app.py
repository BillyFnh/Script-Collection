import configparser
import csv
import json

# Steps for extracting .conf content into csv:
# 1. Read all headers & values and save into an array
# 2. Remove duplicates in the variable
# 3. Assign all unique header names as field names to csv
# 4. Loop through headers & values again and write (writerow with Dictwriter) them into csv according to field names


# 1. Read all headers & values and save into an array (COMPLETED)
config = configparser.RawConfigParser()
conf = config.read("searchLocalsavedsearches.conf")

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
# https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
# Using this as reference to remove duplicates

print("There are a total of" , len(headers) , "headers extracted:")
print(headers)
duplicatedHeaders = list(set(headers))
uniqueHeaders = list(set(headers) - set(duplicatedHeaders))
print("There are a total of" , len(uniqueHeaders) , "uniqueHeaders extracted:")
print(uniqueHeaders)

# 3. Assign all unique header names as field names to csv

# 4. Loop through headers & values again and write (writerow with Dictwriter) them into csv according to field names
# refernce: https://docs.python.org/3/library/csv.html






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