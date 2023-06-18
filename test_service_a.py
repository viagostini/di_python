from service_a import ServiceA

class StubRepo:
    def get(self, key: str) -> int:
        return 42
    
class StubServiceB:
    pass

def test_service_a():
    # @inject is not intrusive and allows for stubbing/mocking classes normally
    service = ServiceA(StubRepo(), StubServiceB())

    assert service.repo.get("test") == 42