# Kubernetes

## Cheatsheet

### Resource Management

#### Manually Create Cronjob

Manually create CronJob from existing Cronjob Definition

```bash
kubectl create job --from=cronjob/cronjob-correlation-search-extractor manual-job-20201110-correlation-search-extractor -n production-splunk-database
kubectl create job --from=cronjob/cronjob-splunkbase-scraper  manual-job-20201110-web-scraper -n production-splunk-database
```

#### Monitor Resources

```bash
# Overview
watch -n 1 "kubectl get pods,services,cronjob.batch,job.batch -n production-defacement-detection -o wide"
# Pods
watch -n 1 "kubectl get pods -A | grep -E 'splunk-database|defacement-detection' | grep -v 'Completed'"
# Jobs
watch -n 1 "kubectl get job.batch,cronjob.batch -A | grep -E 'splunk-database|defacement-detection'"
kubectl get jobs --sort-by=.status.startTime -A -o=custom-columns=JobName:.metadata.name,Succeeded:.status.succeeded,StartTime:.status.startTime,CompletionTime:.status.completionTime
# Services
watch -n 1 "kubectl get services -A | grep -E 'splunk-database|defacement-detection'"
# DB
watch -n 1 "kubectl get pods -A | grep -E 'mongodb'"
# PV
watch -n 1 "kubectl get pv -A | grep -E 'splunk-database|defacement-detection'"
# PVC
watch -n 1 "kubectl get pvc -A | grep -E 'splunk-database|defacement-detection'"
```

### Log Tracing

## Pod

```bash
kubectl -n <namespace> logs pod/<pod-name> --tail=10 -f

# examples
kubectl logs -f -n production-defacement-detection --tail=10
kubectl logs -f -n production-defacement-detection --since=10m --timestamps
```

### Deployment

It can be quite annoy to trace logs when you have a set of applications running in parallel, instead of having 3 searate terminals opened, each for one pod, you could try the following:

```bash
kubectl logs -n <namespace> -l <label-key>=<label-value>

# examples
kubectl logs -n production-defacement-detection -l service=rabbitmq-comparison-worker --max-log-requests=20 --tail=10
watch -n 1 'kubectl logs -n production-defacement-detection -l service=rabbitmq-comparison-worker --max-log-requests=20 --since=1m | grep -E "\[x\] Processing: " | sort -n -k 1'
```

## Stale Replicaset Clean-up

When updating deployments, sometimes the replica sets are left undeleted.
This isn't an issue when deployments are controlled manually, for example if you use the following commands to manually create and remove K8s resources:

```bash
kubectl apply -f resource.yaml
kubectl delete -f resource.yaml
```

However it is an issue when you setup pipelines to deploy your code, which only re-applies the resources with an updated image.
A better practice would be to handle the cleanup in the pipeline as well, but I've used Cronjob to cleanup stale Replica Sets daily as a temporary solution.
