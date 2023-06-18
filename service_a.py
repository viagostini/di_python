from kink import inject

from repository import Repository
from service_b import ServiceB


@inject
class ServiceA:
    def __init__(self, repo: Repository, service_b: ServiceB) -> None:
        self.repo = repo
        self.service_b = service_b
