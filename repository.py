class Repository:
    def __init__(self):
        self.data = {"a": 2, "b": 5}

    def get(self, key: str) -> int:
        return self.data[key]
        