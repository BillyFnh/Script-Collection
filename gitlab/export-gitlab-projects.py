#!/usr/bin/python3

import requests
import sys

headers = {'PRIVATE-TOKEN': 'iCYg1N3PpiGxS12CCRBm'}
current_page = 0
last_page = False
project_per_page = 50

while last_page is not True:
  current_page += 1
  response = requests.get('http://172.31.38.73/api/v4/projects?' + 'per_page=' + str(project_per_page) + '&page=' + str(current_page), headers=headers)
  projects = response.json()

  if len(projects) < project_per_page or response.status_code != 200: last_page = True

  if response.status_code == 200:
    print('request successful')
    for project in projects:
      print(f'{project.get("visibility")}: {project.get("name_with_namespace")}, ssh_url_to_repo: {project.get("ssh_url_to_repo")}')
  else:
    print("API response code: ", response.status_code , "... Perhaps the private-token has expired?")

