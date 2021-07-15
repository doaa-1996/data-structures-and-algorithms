class HashTable:

    class _LinkedList:
    
        class _Node:
           
            def __init__(self, key, value, next_=None):
                self.key = key
                self.value = value
                self.next = next_

        def __init__(self):
            self.head = None

        def add(self, key, value):
            if not self.head:
                self.head = self._Node(key, value)
                return
            current = self.head
            while isinstance(current.next, self._Node):
                current = current.next
            current.next = self._Node(key, value)

        def contains(self, key):
            current = self.head
            while isinstance(current, self._Node):
                if current.key == key:
                    return True
                current = current.next
            return False

        def get(self, key):
            current = self.head
            while isinstance(current, self._Node):
                if current.key == key:
                    return current.value
                current = current.next
            raise LookupError

    def __init__(self, length=1024):
        self._buckets = length
        self._table = [None] * self._buckets

    def _hash(self, key):
        key_sum = 0

        if isinstance(key, bool):
            raise ValueError

        if isinstance(key, str):
            for char in key:
                key_sum += ord(char)
        elif isinstance(key, int):
            key_sum = key
        else:
            raise ValueError

        key_sum *= 619
        key_sum %= self._buckets
        return key_sum

    def add(self, key, value):
        index = self._hash(key)
        if self._table[index] == None:
            self._table[index] = self._LinkedList()
        self._table[index].add(key, value)

    def contains(self, key):
        index = self._hash(key)
        if isinstance(self._table[index], self._LinkedList):
            return self._table[index].contains(key)
        return False

    def get(self, key):
        index = self._hash(key)
        if isinstance(self._table[index], self._LinkedList):
            return self._table[index].get(key)
        raise ValueError
