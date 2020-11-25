#!/bin/bash

# select backup files
backup_data_name=1601582584_2020_10_01_12.10.14
backup_data_file=1601582584_2020_10_01_12.10.14_gitlab_backup.tar
backup_config_file=gitlab_config_1601582691_2020_10_01.tar
restoration_host=172.31.38.111

echo "restoring GitLab with the following backup files..."
echo "  - $backup_data_file"
echo "  - $backup_config_file"
echo ""
echo ""
echo ""

# setup 172.31.38.111 directories
echo "setting up directories in $restoration_host..."
sshpass -p "macroview" ssh -p 10022 $restoration_host << EOL
    cd /root
    mkdir gitlab-$backup_data_name
    cd gitlab-$backup_data_name
    mkdir data
    mkdir config
    mkdir logs
    echo "version: '3.7'

services:
  gitlab:
    container_name: gitlab-$backup_data_name
    # image: gitlab/gitlab-ce:12.4.0-ce.0
    image: gitlab/gitlab-ce:12.10.14-ce.0
    # image: gitlab/gitlab-ce:13.0.0-ce.0
    # image: gitlab/gitlab-ce:13.2.4-ce.0
    restart: always
    hostname: '172.31.38.73'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://172.31.38.73'
        gitlab_rails['time_zone'] = 'Hong Kong'
        gitlab_rails['gitlab_shell_ssh_port'] = 22
        letsencrypt['enable'] = false
        # metrics
        logging['udp_log_shipping_host'] = '172.31.50.53'
        logging['udp_log_shipping_port'] = 514
        gitlab_rails['monitoring_whitelist'] = ['127.0.0.0/8', '172.0.0.0/8', '172.31.38.103', '172.20.26.35']
        prometheus['enable'] = true
        node_exporter['enable'] = true
        # prometheus['listen_address'] = '172.31.38.111:9090'
        grafana['enable'] = true
        # grafana['admin_password'] = 'macroview123'
        # email
        # gitlab_rails['smtp_enable'] = true
        # gitlab_rails['smtp_address'] = 'smtp.gmail.com'
        # gitlab_rails['smtp_port'] = 587
        # gitlab_rails['smtp_user_name'] = 'macroview.advs.gitlab@gmail.com'
        # gitlab_rails['smtp_password'] = 'M@croview123'
        # gitlab_rails['smtp_domain'] = 'smtp.gmail.com'
        # gitlab_rails['smtp_authentication'] = 'login'
        # gitlab_rails['smtp_enable_starttls_auto'] = true
        # gitlab_rails['smtp_tls'] = false
        # gitlab_rails['smtp_openssl_verify_mode'] = 'none' # Can be: 'none', 'peer', 'client_once', 'fail_if_no_peer_cert', see http://api.rubyonrails.org/classes/ActionMailer/Base.html
        # microsoft active directory
        gitlab_rails['ldap_enabled'] = true
        gitlab_rails['ldap_servers'] = YAML.load <<-'EOS'
          main: # 'main' is the GitLab 'provider ID' of this LDAP server
            label: 'Macroview'
            host: 'hcs-dc01-dc-2.hcs-dc01.com'
            port: 389
            uid: 'sAMAccountName'
            bind_dn: 'CN=GitLabAuthentication,CN=Users,DC=hcs-dc01,DC=com'
            password: 'M@croview1'
            encryption: 'plain' # 'start_tls' or 'simple_tls' or 'plain'
            verify_certificates: true
            smartcard_auth: false
            active_directory: true
            allow_username_or_email_login: true
            lowercase_usernames: false
            block_auto_created_users: false
            base: 'DC=hcs-dc01,DC=com'
            user_filter: ''
        EOS
    ports:
      - '80:80'
      - '443:443'
      - '22:22'
      - '9090:9090'
    # command: /bin/bash
    # tty: true
    volumes:
      - type: bind
        source: /root/gitlab-$backup_data_name/config
        target: /etc/gitlab
      - type: bind
        source: /root/gitlab-$backup_data_name/logs
        target: /var/log/gitlab
      - type: bind
        source: /root/gitlab-$backup_data_name/data
        target: /var/opt/gitlab" > docker-compose.yaml
    echo "starting GitLab and wait 5 minutes for it to complete startup..."
    docker-compose up -d
    sleep 300
    docker-compose down
EOL


# Start restore process
sshpass -p "macroview" ssh -p 10022 $restoration_host << EOL

  echo "transfering backup files to GitLab directory..."
  cp /root/gitlab-backup/$backup_data_file /root/gitlab-$backup_data_name/data/backups/
  echo $?
  cp /root/gitlab-backup/$backup_config_file /root/gitlab-$backup_data_name
  echo $?

  echo "stopping gitlab services in preperation for backup..."

    cd /root/gitlab-$backup_data_name/data/backups
    ls -lh
    chmod ugo+r $backup_data_file
    ls -lh

    cd /root/gitlab-$backup_data_name
    docker-compose down
    echo "starting GitLab and wait 5 minutes for it to complete startup..."
    docker-compose up -d
    sleep 300

    docker exec gitlab-$backup_data_name gitlab-ctl stop unicorn
    docker exec gitlab-$backup_data_name gitlab-ctl stop puma
    docker exec gitlab-$backup_data_name gitlab-ctl stop sidekiq
    docker exec gitlab-$backup_data_name gitlab-ctl status

    echo "restoration preperation has been completed, you may now ssh into $restoration_host and execute the following command:"
    echo "sshpass -p 'macroview' ssh -p 10022 $restoration_host"
    echo "docker exec -it gitlab-$backup_data_name gitlab-backup restore BACKUP=$backup_data_name"
    # /root/gitlab-backup/launch-automated-gitlab-backup.sh $backup_data_name

    echo "execute restore-gitlab-backup-2.sh next to restore configurations"
EOL