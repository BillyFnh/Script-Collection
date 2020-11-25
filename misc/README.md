# Misc

## RabbitMQ Server

### Queue Management

```bash
# docker
docker exec -it rabbitmq-server rabbitmqctl purge_queue comparison_queue
watch -n 1 "docker exec rabbitmq-server rabbitmqctl list_queues"

# kubernetes
watch -n 1 "kubectl exec -n production-defacement-detection rabbitmq-server rabbitmqctl list_queues"
watch -n 1 "kubectl exec -n production-defacement-detection rabbitmq-server purge_queue comparison_queue"
```
