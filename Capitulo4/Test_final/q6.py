from hash import HashTable
table = HashTable(8)
book = "Alice in Wonderland"
key = sum(map(ord, book))
print(key, table.hash(key))