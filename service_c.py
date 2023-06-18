from kink import inject
from repository import Repository


@inject
class ServiceC:
    def __init__(self, repo: Repository) -> None:
        self.repo = repo
