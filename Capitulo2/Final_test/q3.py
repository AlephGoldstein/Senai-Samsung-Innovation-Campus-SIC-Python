list = [5, 61, 3, 9, 2, 12, 3, 8]
for i in range(len(list)-1):
    if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
print(list)