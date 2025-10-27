from fastapi import APIRouter
from app.k8s_client import list_pods

router = APIRouter(prefix="/api")

# 健康检查
@router.get("/health")
async def health():
    return {"status": "ok"}

# 获取命名空间 pods
@router.get("/pods")
async def get_pods(namespace: str = "default"):
    pods = list_pods(namespace)
    return {"namespace": namespace, "pods": pods}

