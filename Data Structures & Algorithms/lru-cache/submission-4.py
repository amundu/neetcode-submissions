class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = self.next  = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.cap = capacity
        self.start, self.end = Node(), Node()
        self.end.prev, self.start.next = self.start, self.end
    
    def print(self):
        start = self.start.next
        output = []
        while start != self.end:
            output.append(start.key)
            start = start.next
        print(output)

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        prev, next = self.end.prev, self.end
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        
        new_node = Node(key, value)
        self.mp[key] = new_node
        self.insert(new_node)

        if len(self.mp) > self.cap:
            self.mp.pop(self.start.next.key)
            self.remove(self.start.next)
        