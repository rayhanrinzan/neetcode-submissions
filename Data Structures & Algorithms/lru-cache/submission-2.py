class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}
        self.used = []
    def get(self, key: int) -> int:
        if key in self.table:
            if key in self.used:
                self.used.remove(key)
            self.used.append(key)
            return self.table[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.table[key] = value
        if len(self.table) > self.capacity and len(self.used) > 0:
            least_recent = self.used.pop(0)
            del self.table[least_recent]
        if key in self.table:
            if key in self.used:
                self.used.remove(key)
            self.used.append(key)
        

