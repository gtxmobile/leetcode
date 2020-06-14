class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {}
        self.cnt2value = {}
        self.cap = capacity
        self.cnt = 0
        self.oldest = 0

    # @return an integer
    def get(self, key):
        if not self.cache.get(key):
            return -1
        else:
            v = self.cnt2value.pop(self.cache[key])
            self.cache[key] = self.cnt
            self.cnt2value[self.cnt] = v
            self.oldest = min(self.cache.values())
            self.cnt += 1
            return v

    def isoldest(self, key):
        return self.cache[key] == self.oldest

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if len(self.cache) == self.cap:
            for k in self.cache.keys():
                if self.isoldest(k):
                    self.cache.pop(k)
                    break
        self.cache[key] = self.cnt
        self.cnt2value[self.cnt] = value
        self.cnt += 1
        self.oldest = min(self.cache.values())


class LRU2:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {}
        self.cnt2value = {}
        self.cap = capacity
        self.cnt = 0
        self.oldest = 0

    # @return an integer
    def get(self, key):
        if not key in self.cache:
            return -1
        else:
            v = self.cnt2value.pop(self.cache[key])
            self.cnt2value[self.cnt] = v
            if self.isoldest(key): self.oldest = min(self.cnt2value.keys())
            self.cache[key] = self.cnt
            self.cnt += 1
            return v

    def isoldest(self, key):
        return self.cache.get(key) == self.oldest

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.isoldest(key):
            self.cache.pop(key)
            self.cnt2value.pop(self.oldest)
            if not self.cache:
                self.oldest += 1
            else:
                self.oldest = min(self.cache.values())
        elif key in self.cache:
            self.cnt2value.pop(self.cache[key])
        else:
            if len(self.cache) == self.cap:
                for k in self.cache:
                    if self.cache[k] == self.oldest:
                        self.cache.pop(k)
                        self.cnt2value.pop(self.oldest)
                        self.oldest = min(self.cache.values())
                        break
        self.cache[key] = self.cnt
        self.cnt2value[self.cnt] = value
        self.cnt += 1
