from kubernetes import client, config
from kubernetes.client.rest import ApiException

# 集群内部加载配置
try:
    config.load_incluster_config()
except Exception as e:
    print(f"Failed to load in-cluster config: {e}")
    exit(1)

v1 = client.CoreV1Api()

def list_pods(namespace: str):
    try:
        pods = v1.list_namespaced_pod(namespace)
        return [pod.metadata.name for pod in pods.items]
    except ApiException as e:
        print(f"Error listing pods: {e}")
        return []

