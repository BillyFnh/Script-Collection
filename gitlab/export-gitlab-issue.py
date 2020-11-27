#!/usr/bin/python3

import requests
import csv
import sys

headers = {'PRIVATE-TOKEN': 'iCYg1N3PpiGxS12CCRBm'}
assignee_id = 2
all_available_csv_fieldnames = ["id", "iid", "project_id", "title", "description", "state", "created_at", "updated_at", "closed_at", "closed_by", "labels", "milestone", "assignees", "author", "assignee", "user_notes_count", "merge_requests_count", "upvotes", "downvotes", "due_date", "confidential", "discussion_locked", "web_url", "time_stats", "task_completion_status", "has_tasks", "_links", "references", "moved_to_id"]
export_csv_fieldnames = ['id', 'project_id', 'project', 'title', 'description', 'created_at', 'updated_at', 'closed_at', 'due_date', 'web_url', 'author', 'assignee']
issue_counter = 0
current_page = 0
last_page = False
issue_per_page = 100

# Create new CSV with appropriate fieldnames
with open('issues.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=export_csv_fieldnames)
    writer.writeheader()

while last_page is not True:
    current_page += 1
    response = requests.get('http://172.31.38.73/api/v4/issues?' + 'per_page=' + str(issue_per_page) + '&page=' + str(current_page), headers=headers)
    # response = requests.get('http://172.31.38.73/api/v4/issues?assignee_id=' + str(assignee_id) + '&per_page=' + str(issue_per_page) + '&page=' + str(current_page), headers=headers)
    issues = response.json()

    if len(issues) < issue_per_page or response.status_code != 200:
        last_page = True

    if response.status_code == 200:
        for issue in issues:
            if issue['assignee'] == None:
                issue['assignee'] = {'name': 'unassigned'}
                # print('no assignee --> project:', issue['references']['full'], ', issue ', ':', issue['title'])
            
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
                'author': issue['author']['name'],
                'assignee': issue['assignee']['name'],
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

            issue_counter = issue_counter + 1
            print('project:', issue['references']['full'], ', issue ', ':', issue['title'])
    else:
        print("API response code: ", response.status_code , "... Perhaps the private-token has expired?")
    
print('exported ', issue_counter, ' issues to ./issues.csv')