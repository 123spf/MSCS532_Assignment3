class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        # empty buckets
        self.table = [[] for _ in range(capacity)]