class Node:
    def __init__(self, key=-1, value=-1):
        self.value = value
        self.key = key
        self.prv = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.head = Node()
        self.tail = self.head
        self.age = 0
        self.key_map = {}

    def insert_head(self, n):
        n.prv = self.head
        sec = self.head.next
        n.next = sec
        if sec:
            sec.prv = n
        self.head.next = n

    def remove(self):
        n = self.head.next
        if n:
            sec = n.next
            if sec:
                sec.prv = self.head
            self.head.next = sec
            self.key_map[n.key] = None
            return n

    def append(self, n):
        n.prv = self.tail
        self.tail.next = n
        self.tail = n
        n.next = None

    def update(self, i):
        p = i.prv
        n = i.next
        p.next = n
        if n:
            n.prv = p
        else:
            self.tail = p
        self.append(i)

    def get(self, key):
        i = self.key_map.get(key, None)
        if i:
            self.update(i)
            return i.value
        return -1

    def put(self, key, value):
        i = self.key_map.get(key, None)
        if i:
            i.value = value
            self.update(i)
        else:
            if self.cap > 0:
                n = Node(key, value)
                self.cap -= 1
            else:
                n = self.remove()
                n.key = key
                n.value = value
            self.append(n)
            self.key_map[key] = n

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
