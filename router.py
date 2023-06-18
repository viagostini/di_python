from fastapi import APIRouter, Depends
from kink import di

from repository import Repository
from service_a import ServiceA

router = APIRouter()

@router.get("/")
async def index(
    repo: Repository = Depends(lambda: di[Repository]),
    service: ServiceA = Depends(lambda: di[ServiceA]),
):
    return {
        "data_from_repo": repo.data,
        "data_from_service_a": service.repo.data,
        "data_from_service_b": service.service_b.repo.data,
        "data_from_service_c": service.service_b.service_c.repo.data,
    }