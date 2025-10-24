from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from kubernetes import client, config

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Pod 内使用 in-cluster config
config.load_incluster_config()
v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()
networking_v1 = client.NetworkingV1Api()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    pods = v1.list_pod_for_all_namespaces().items
    deployments = apps_v1.list_deployment_for_all_namespaces().items
    services = v1.list_service_for_all_namespaces().items
    pvcs = v1.list_persistent_volume_claim_for_all_namespaces().items
    pvs = v1.list_persistent_volume().items
    ingresses = networking_v1.list_ingress_for_all_namespaces().items
    return templates.TemplateResponse("index.html", {
        "request": request,
        "pods": pods,
        "deployments": deployments,
        "services": services,
        "pvcs": pvcs,
        "pvs": pvs,
        "ingresses": ingresses
    })

@app.post("/delete_pod")
async def delete_pod(name: str = Form(...), namespace: str = Form(...)):
    v1.delete_namespaced_pod(name=name, namespace=namespace)
    return {"status": "success"}
