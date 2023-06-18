from kink import inject
from repository import Repository
from service_c import ServiceC


@inject
class ServiceB:
    def __init__(self, repo: Repository, service_c: ServiceC) -> None:
        self.repo = repo
        self.service_c = service_c
