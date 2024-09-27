# Lista original
n_list = [10, 20, 30]

# Usando map() para multiplicar os elementos por 2 e 3
dobro = list(map(lambda x: x * 2, n_list))
triplo = list(map(lambda x: x * 3, n_list))

# Exibindo os resultados
print("Valores 2x da lista:", dobro)
print("Valores 3x da lista:", triplo)
