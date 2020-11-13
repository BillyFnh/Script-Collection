import requests
import csv
import sys

headers = {'PRIVATE-TOKEN': 'iCYg1N3PpiGxS12CCRBm'}
assignee_id = 2 # 
all_available_csv_fieldnames = ["id", "iid", "project_id", "title", "description", "state", "created_at", "updated_at", "closed_at", "closed_by", "labels", "milestone", "assignees", "author", "assignee", "user_notes_count", "merge_requests_count", "upvotes", "downvotes", "due_date", "confidential", "discussion_locked", "web_url", "time_stats", "task_completion_status", "has_tasks", "_links", "references", "moved_to_id"]
export_csv_fieldnames = ['id', 'project_id', 'project', 'title', 'description', 'created_at', 'updated_at', 'closed_at', 'due_date', 'web_url', 'author', 'assignee']
response = requests.get('http://172.31.38.73/api/v4/issues?assignee_id=2&state=opened&per_page=100&page=1', headers=headers)
issue_counter = 0
issues = response.json()

# Create new CSV  with appropriate fieldnames
with open('issues.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=export_csv_fieldnames)
    writer.writeheader()

if response.status_code == 200:
    for issue in issues:
        issue_counter = issue_counter + 1
        if issue['assignee'] != None:
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
        else:
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
                'assignee': 'unassigned',
                'web_url': issue['web_url']
            } 
            
        print('project:', issue_dict['project'], ', issue ', ':', issue['title'])
        # read fieldnames from csv
        with open('./issues.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames

        # append csv with current section
        with open('./issues.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(issue_dict)

    print('exported ', issue_counter, ' issues to ./issues.csv')
else:
    print("API response code != 200")