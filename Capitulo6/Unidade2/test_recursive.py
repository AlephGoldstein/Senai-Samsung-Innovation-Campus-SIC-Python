
def sum(valor, c):
    if c == 16:
        return valor
    else:
        valor = sum(valor+1,c+1)
    return valor
print(sum(5,0))