#!/bin/bash

# you can obtain a new session token by manually logging to GitLab via browser, and copying the _gitlab_session token

echo "checking repository response for http://172.31.38.111"
echo "http://172.31.38.111/web-security-service/livi-fake-web-monitoring-service"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/web-security-service/livi-fake-web-monitoring-service | grep HTTP
echo "http://172.31.38.111/splunk/splunk-add-on-version-control"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/splunk/splunk-add-on-version-control | grep HTTP
echo "http://172.31.38.111/billynhfong/splunk-correlation-search-extraction"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/billynhfong/splunk-correlation-search-extraction | grep HTTP
echo "http://172.31.38.111/billynhfong/splunk-database"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/billynhfong/splunk-database | grep HTTP
echo "http://172.31.38.111/billynhfong/network-traffic-monitor"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/billynhfong/network-traffic-monitor | grep HTTP
echo "http://172.31.38.111/angelawong/prism-fireeye"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/angelawong/prism-fireeye | grep HTTP
echo "http://172.31.38.111/billynhfong/workflow-demo"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/billynhfong/workflow-demo | grep HTTP
echo "http://172.31.38.111/billynhfong/splunk-add-on-monitor"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/billynhfong/splunk-add-on-monitor | grep HTTP
echo "http://172.31.38.111/splunk/splunk-base-web-scraper"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/splunk/splunk-base-web-scraper | grep HTTP
echo "http://172.31.38.111/billynhfong/splunk-use-case-reference-tool"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/billynhfong/splunk-use-case-reference-tool | grep HTTP
echo "http://172.31.38.111/billynhfong/gitlab-guide"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/billynhfong/gitlab-guide | grep HTTP
echo "http://172.31.38.111/billynhfong/splunk-add-on-monitor-with-ci"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/billynhfong/splunk-add-on-monitor-with-ci | grep HTTP
echo "http://172.31.38.111/billynhfong/splunk-database-project-k8s-deployment"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/billynhfong/splunk-database-project-k8s-deployment | grep HTTP
echo "http://172.31.38.111/hello-world/sandbox"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/hello-world/sandbox | grep HTTP
echo "http://172.31.38.111/data-platform/sunlife---grafana-version-control"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/data-platform/sunlife---grafana-version-control | grep HTTP
echo "http://172.31.38.111/angelawong/jira"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/angelawong/jira | grep HTTP
echo "http://172.31.38.111/data-platform/cli2json"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/data-platform/cli2json | grep HTTP
echo "http://172.31.38.111/jeffchwong/vulnerability-check"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/jeffchwong/vulnerability-check | grep HTTP
echo "http://172.31.38.111/data-platform/cnp-data-analyser-and-grafana-dashboard"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/data-platform/cnp-data-analyser-and-grafana-dashboard | grep HTTP
echo "http://172.31.38.111/klauswong/traceroute"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/klauswong/traceroute | grep HTTP
echo "http://172.31.38.111/old-projects/SAFPSrvPortal"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/old-projects/SAFPSrvPortal | grep HTTP
echo "http://172.31.38.111/old-projects/CBI"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/old-projects/CBI | grep HTTP
echo "http://172.31.38.111/doc/Grafana-Dashboard"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/doc/Grafana-Dashboard | grep HTTP
echo "http://172.31.38.111/old-projects/Liferay"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/old-projects/Liferay | grep HTTP
echo "http://172.31.38.111/web-based-defacement-detection-service/backend-server"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/web-based-defacement-detection-service/backend-server | grep HTTP
echo "http://172.31.38.111/report-automation/pm-report-automation"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/report-automation/pm-report-automation | grep HTTP
echo "http://172.31.38.111/report-automation/noc-jasper-reports-server"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/report-automation/noc-jasper-reports-server | grep HTTP
echo "http://172.31.38.111/jackslchan/dns-demo-lab"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/jackslchan/dns-demo-lab | grep HTTP
echo "http://172.31.38.111/jackslchan/reusable-ansible-scripts"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/jackslchan/reusable-ansible-scripts | grep HTTP
echo "http://172.31.38.111/jackslchan/improved-dns-demo-lab"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/jackslchan/improved-dns-demo-lab | grep HTTP
echo "http://172.31.38.111/jackslchan/config-files-for-dns-lab"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/jackslchan/config-files-for-dns-lab | grep HTTP
echo "http://172.31.38.111/splunk/advs-internal-splunk"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/splunk/advs-internal-splunk | grep HTTP
echo "http://172.31.38.111/web-based-defacement-detection-service/frontend"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/web-based-defacement-detection-service/frontend | grep HTTP
echo "http://172.31.38.111/splunk/splunk-stream-notes"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/splunk/splunk-stream-notes | grep HTTP
echo "http://172.31.38.111/web-based-defacement-detection-service/deployment"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/web-based-defacement-detection-service/deployment | grep HTTP
echo "http://172.31.38.111/jackslchan/ap-vulnerabilities-search"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/jackslchan/ap-vulnerabilities-search | grep HTTP
echo "http://172.31.38.111/web-based-defacement-detection-service/job-trigger"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/web-based-defacement-detection-service/job-trigger | grep HTTP
echo "http://172.31.38.111/kevinling/wifi-assessment"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/kevinling/wifi-assessment | grep HTTP
echo "http://172.31.38.111/ivankam/bocm-cyberark"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/ivankam/bocm-cyberark | grep HTTP
echo "http://172.31.38.111/ivankam1/bocm-cyberark"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/ivankam1/bocm-cyberark | grep HTTP
echo "http://172.31.38.111/old-projects/SAFPQuestionnaire-portlet"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/old-projects/SAFPQuestionnaire-portlet | grep HTTP
echo "http://172.31.38.111/soc-core/SOC-Newsletter"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/soc-core/SOC-Newsletter | grep HTTP
echo "http://172.31.38.111/security-operations/VulnerabilityCheck"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/security-operations/VulnerabilityCheck | grep HTTP
echo "http://172.31.38.111/jackslchan/feedrank"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/jackslchan/feedrank | grep HTTP
echo "http://172.31.38.111/pen-testing/zaproxy"
curl -b _gitlab_session=21c35597f5bb80b21c64edf7535fde76 -I http://172.31.38.111/pen-testing/zaproxy | grep HTTP