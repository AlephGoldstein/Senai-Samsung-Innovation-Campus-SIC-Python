class HashTable:
    
    def __init__(self,size):
        self.size = size
        self.table = {}
        for i in range(size):
            self.table[i] = []

    def hash(self,key):
        return key % self.size

    def get(self, key):
        return self.table[self.hash(key)]
    
    def put(self, key, value):
        bucket = self.table[self.hash(key)]
        if value not in bucket:
            bucket.append(value)
