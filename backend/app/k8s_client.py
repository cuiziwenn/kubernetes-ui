from kubernetes import client, config

def load_k8s_config():
    try:
        config.load_incluster_config()  # 集群内部
    except:
        config.load_kube_config()  # 本地测试

v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()
networking_v1 = client.NetworkingV1Api()

# 示例：获取所有 pod
def list_pods(namespace="default"):
    load_k8s_config()
    pods = v1.list_namespaced_pod(namespace)
    return [{"name": p.metadata.name, "status": p.status.phase} for p in pods]

