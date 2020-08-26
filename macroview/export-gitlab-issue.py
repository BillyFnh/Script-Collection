import requests
import csv
import sys


headers = {'PRIVATE-TOKEN': 'iCYg1N3PpiGxS12CCRBm'}
csv_fieldnames = ['id', 'project_id', 'project', 'title', 'description', 'created_at', 'updated_at', 'closed_at', 'due_date', 'web_url']
response = requests.get('http://172.31.38.73/api/v4/issues?assignee_id=2&state=opened', headers=headers)
issues = response.json()

# Create CSV file with appropriate headers
with open('issues.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_fieldnames)
    writer.writeheader()

if response.status_code == 200:
    for issue in issues:
        issue_dict = {
            'id': issue['id'],
            'project_id': issue['project_id'],
            'project': issue['references']['full'],
            'title': issue['title'],
            'description': issue['description'],
            'created_at': issue['created_at'],
            'updated_at': issue['updated_at'],
            'closed_at': issue['closed_at'],
            'due_date': issue['due_date'],
            'web_url': issue['web_url']
        }
        # read fieldnames from csv
        with open('./issues.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames

        # append csv with current section
        with open('./issues.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(issue_dict)


    print("exported issues to ./issues.csv")
else:
    print("API response code != 200")



# id:  8
# project_id:  4
# title:  Compose design documentation in README.MD
# description:  None
# created_at:  2019-10-24T11:50:21.403+08:00
# updated_at:  2020-08-25T12:10:27.240+08:00
# closed_at:  None
# due_date:  None
# web_url:  http://172.31.38.73/billynhfong/splunk-database/-/issues/1
# references:  {'short': '#1', 'relative': '#1', 'full': 'billynhfong/splunk-database#1'}