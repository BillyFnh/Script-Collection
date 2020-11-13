#!/bin/bash

# # Generate backup files
docker exec -i gitlab gitlab-backup create >> /root/gitlab-backup/data-backup-log.txt # backup content
echo "exit code = $?"
docker exec -i gitlab gitlab-ctl backup-etc  >> /root/gitlab-backup/config-backup-log.txt # backup config
echo "exit code = $?"

# # Move backup file to netapp
# # mv /srv/gitlab/data/backups/*.tar /mnt/netappgitlab/ >> /dev/null
# # mv /srv/gitlab/config/config_backup/*.tar /mnt/netappgitlab/ >> /dev/null

# # SCP files to to another VM (172.31.38.111)
sshpass -p "macroview" scp -P 10022 -r /srv/gitlab/data/backups/*.tar 172.31.38.111:/root/gitlab-backup/
echo "exit code = $?"
sshpass -p "macroview" scp -P 10022 -r /srv/gitlab/config/config_backup/*.tar 172.31.38.111:/root/gitlab-backup/
echo "exit code = $?"

# # Remove local backup copies 
rm -f /srv/gitlab/data/backups/*.tar
echo "exit code = $?"
rm -f /srv/gitlab/config/config_backup/*.tar
echo "exit code = $?"

# Remove old backups on VM (172.31.38.111)
sshpass -p "macroview" ssh -p 10022 172.31.38.111 << EOL
  cd /root/gitlab-backup
  echo "these backup files are > 2 days old:"
  find ./ -maxdepth 1 -type f -name '*.tar'
  echo "exit code = $?"
  find ./ -maxdepth 1 -type f -mtime +1 -name '*.tar' -delete
EOL