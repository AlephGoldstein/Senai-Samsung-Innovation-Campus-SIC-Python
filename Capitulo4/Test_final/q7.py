from hash import HashTable
table = HashTable(10)
books = [
    "O Pequeno Príncipe",
    "O Velho Homem e o Mar",
    "A Pequena Sereia",
    "A Bela e a Fera",
    "A Última Folha",
    "Alice do País das Maravilhas"
]
for book in books:
    key = sum(map(ord, book))
    table.put(key, book)
for key in table.table.keys():
    print(key, table.table[key])