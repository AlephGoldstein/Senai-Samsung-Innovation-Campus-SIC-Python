from hash import HashTable
books = [
    "The Old Man and the Sea",
    "The Little Mermaid",
    "Beauty and the Beast",
    "The Last Leaf"
]
table = HashTable(8)
book = "The Little Prince"
key = sum(map(ord, book))
table.put(key, book)
for book in books:
    key = sum(map(ord, book))
    table.put(key, book)
for key in table.table.keys():
    print(key, table.table[key])
title = "The Last Leaf"
key = sum(map(ord, title))
bucket = table.get(key)
print(key, bucket)