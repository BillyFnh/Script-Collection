#!/bin/bash

# select backup files
backup_data_name=1601582584_2020_10_01_12.10.14
backup_data_file=1601582584_2020_10_01_12.10.14_gitlab_backup.tar
backup_config_file=gitlab_config_1601582691_2020_10_01.tar
restoration_host=172.31.38.111

sshpass -p "macroview" ssh -p 10022 $restoration_host << EOL

  # restart GitLab and check restoration status
  docker restart gitlab-$backup_data_name
  echo "restarting GitLab and wait 5 minutes for it to complete startup..."
  sleep 300
  docker exec gitlab-$backup_data_name gitlab-rake gitlab:check SANITIZE=true

  # restoring config files
  cd /root/gitlab-$backup_data_name
  docker-compose down
  echo "restoring config files..."
  chmod go+r $backup_config_file
  tar -xvf $backup_config_file
  mv -f ./etc/gitlab/* ./config/
  sleep 5
  docker-compose up -d
  echo "restoration completed"
EOL

# check repository restoration status 
  # write python script to get all project links via GitLab API
  # clone all projects?
  # open project page and check for status code?
  # meta data of project might show if project was restored successfully? 