def sum(a,b):
    return a + b

def sub(a,b):
    return a - b
list = [sum,sub]
a = list[0](100,200)
b = list[1](400,500)
print(a)
print(b)