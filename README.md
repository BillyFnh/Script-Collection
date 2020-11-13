# Script Collection

## JSON Filter (Splunk Add-On)

### Purpose

Filter duplicated entires in data exported via Splunk add-on database.

### Exporting Data From Splunk Add-On Database

```bash
# ssh into existing K8s Pod
kubectl -n production splunk-database exec -it production-mongodb-0 /bin/bash

# PV location
cd /data/db

# export data in JSON format
mongoexport --db admin --collection apps --out Splunk_TA_bluecoat-proxysg.bson --query '{"web-scraped-app.name": "Splunk Add-on for Symantec Blue Coat ProxySG"}'
```

### Script Configuration

```python
# Folder that contain raw JSON files are
targetFolder = './export-20201112/'

# Folder that the script will output to
exportFolder = './export-20201112-cleaned/'
```

### Script Execution

`./filter-json-splunk-add-on.py`

## Export GitLab Issues To CSV

### Purpose

Generate To-Do list (CSV) by fetching GitLab incomplete issues.

### Script configuration

```python
# set access token
headers = {'PRIVATE-TOKEN': 'iCYg1N3PpiGxS12CCRBm'}

# set GitLab endpoint & user ID
response = requests.get('http://172.31.38.73/api/v4/issues?assignee_id=2&state=opened&per_page=100&page=1', headers=headers)
```

### Script Execution

`./export-gitlab-issue.py`

## GitLab

### Daily Application Backup

Perform daily backup of Dockerized GitLab (ominious installation) and SCP the backup files to a save location.

### Semi-Auto GitLab Backup Restoration

Restore GitLab from Backup, require manual input at interactive CLI.

#### Script Execution

```bash
# start script part 1
./restore-gitlab-backup-1.sh

# copy script generated from above script, manually confirm twice in interactive CLI
docker exec -it gitlab-$backup_data_name gitlab-backup restore BACKUP=$backup_data_name

# continue with restoration with scrit part 2
./restore-gitlab-backup-1.sh
```

### Check Repository HTTP Response

Validate GitLab repositories are restored properly and have content inside.
