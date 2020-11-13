#!/bin/python3

import os
import json

targetFolder = './export-20201112/'
exportFolder = './export-20201112-cleaned/'
filenameArr = os.listdir('./' + 'export-20201112')

for filename in filenameArr:
  filteredJson = []
  updateDateArr = []

  if filename.endswith('.json'):
    print('cleaning:', filename)

    with open(targetFolder + filename, 'rb') as file:
      data = json.load(file)

    print('  json length (before):', len(data))

    for element in data:
      updateDate = element['web-scraped-app']['updated']
      if updateDate not in updateDateArr:
        updateDateArr.append(updateDate)
        filteredJson.append(element['web-scraped-app'])
    
    print('  json length (after): ', len(filteredJson),'\n')

    with open(exportFolder + filename, 'w') as file:
      json.dump(filteredJson, file)