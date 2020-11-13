# Bash Script Collection

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

```/root/project/bashscript-collection/macroview/filter-json-splunk-add-on.py```