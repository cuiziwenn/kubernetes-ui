from fastapi import APIRouter
from app.k8s_client import list_pods

router = APIRouter()

@router.get("/pods")
def get_pods(namespace: str = "default"):
    return list_pods(namespace)

