# Docker

## Cheatsheet

### Persistent Docker Attach

```bash
while true; do clear; docker attach <container-name>; sleep 1; done

# examples
while true; do clear; docker attach rabbitmq-worker-dev-1; sleep 1; done
```

### Docker Stats (Short)

```bash
docker stats --format "{{.CPUPerc}}: {{.Name}}"

# output
0.00%: rabbitmq-worker-dev-1
0.00%: defacement-backend-dev
2.30%: rabbitmq-server
0.00%: defacement-job-trigger-dev
0.50%: defacement-database
0.36%: mongo-image-test
0.01%: defacement-frontend-dev
```
