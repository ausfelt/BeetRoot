class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def __contains__(self, key):
        bucket = hash(key) % self.size
        return any(key == k for k, v in self.table[bucket])

    def __len__(self):
        return self.count

    def insert(self, key, value):
        bucket = hash(key) % self.size
        for i, (k, v) in enumerate(self.table[bucket]):
            if k == key:
                self.table[bucket][i] = (key, value)
                break
        else:
            self.table[bucket].append((key, value))
            self.count += 1

    def get(self, key):
        bucket = hash(key) % self.size
        for k, v in self.table[bucket]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        bucket = hash(key) % self.size
        for i, (k, v) in enumerate(self.table[bucket]):
            if k == key:
                del self.table[bucket][i]
                self.count -= 1
                return
        raise KeyError(key)