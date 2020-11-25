#!/bin/bash
# Cron Schedule: 15 4 * * *

# cleanup namespace: splunk-database & production-splunk-database
IFS=" " read -r -a rsNameSpaceSplunk <<< `echo $(kubectl get replicaset.apps --all-namespaces | grep -E -o ".*splunk-database.*0\s+0" | grep -E -o "^\S+")`
IFS=" " read -r -a rsNameSplunk <<< `echo $(kubectl get replicaset.apps --all-namespaces | grep -E -o "splunk-database.*0\s+0" | grep -E -o "\s+\S{3,99}\s+" | grep -E -o "\S*")`

for (( i=0 ; i<${#rsNameSplunk[@]} ; i++ ));do
    echo $(kubectl delete replicaset.apps/${rsNameSplunk[i]} -n ${rsNameSpaceSplunk[i]})
done

# cleanup namespace: defacement-detection & production-defacement-detection
IFS=" " read -r -a rsNameSpaceDefacement <<< `echo $(kubectl get replicaset.apps --all-namespaces | grep -E -o ".*defacement-detection.*0\s+0" | grep -E -o "^\S+")`
IFS=" " read -r -a rsNameDefacement <<< `echo $(kubectl get replicaset.apps --all-namespaces | grep -E -o "defacement-detection.*0\s+0" | grep -E -o "\s+\S{3,99}\s+" | grep -E -o "\S*")`

for (( i=0 ; i<${#rsNameDefacement[@]} ; i++ ));do
    echo $(kubectl delete replicaset.apps/${rsNameDefacement[i]} -n ${rsNameSpaceDefacement[i]})
done

curl -X POST -H 'Content-type: application/json' --data '{"text": "*Cleanup Stale Replica Sets*\n*Target Namespaces*:\t\t splunk-database\n\t\t\t\t\t\t\t\t\t\t\tproduction-splunk-database\n\t\t\t\t\t\t\t\t\t\t\tdefacement-detection\n\t\t\t\t\t\t\t\t\t\t\tproduction-defacement-detection\n"}' https://hooks.slack.com/something