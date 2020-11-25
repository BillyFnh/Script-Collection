# GitLab

## Daily Application Backup - [Script](./backup-gitlab.sh)

Perform daily backup of Dockerized GitLab (ominious installation) and SCP the backup files to a save location.

## Semi-Auto GitLab Backup Restoration - [Script (Part 1)](./restore-gitlab-backup-1.sh) / [Script (Part 2)](./restore-gitlab-backup-2.sh)

Restore GitLab from Backup, require manual input at interactive CLI.

### Script Execution

```bash
# start script part 1
./restore-gitlab-backup-1.sh

# copy script generated from above script, manually confirm twice in interactive CLI
docker exec -it gitlab-$backup_data_name gitlab-backup restore BACKUP=$backup_data_name

# continue with restoration with scrit part 2
./restore-gitlab-backup-2.sh
```

## Check Repository HTTP Response - [Script](./check-repo-response.sh)

Validate GitLab repositories are restored properly and have content inside.
Sometimes repositories are not backed up properly before version 12.10.14, which would result in an empty repository.

## Export GitLab Issues To CSV - [Script](./export-gitlab-issue.py)

This was used to generate To-Do lists (CSV) by fetching GitLab incomplete issues, and exporting them in CSV for further formatting via spreadsheet.

### Script configuration

```python
# set access token (you can obtain this token by logging into GitLab via a browser, the token will be saved as a cookie)
headers = {'PRIVATE-TOKEN': 'iCYg1N3PpiGxS12CCRBm'}

# set GitLab endpoint & user ID
response = requests.get('http://172.31.38.73/api/v4/issues?assignee_id=2&state=opened&per_page=100&page=1', headers=headers)
```
