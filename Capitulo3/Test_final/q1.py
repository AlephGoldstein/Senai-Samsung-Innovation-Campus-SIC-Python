import math

# Função para calcular a distância entre dois pontos
def calcular_distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

# Entrada dos pontos pelo usuário
x1 = float(input("Digite a coordenada x1: "))
y1 = float(input("Digite a coordenada y1: "))
x2 = float(input("Digite a coordenada x2: "))
y2 = float(input("Digite a coordenada y2: "))

# Cálculo e exibição da distância
distancia = calcular_distancia(x1, y1, x2, y2)
print(f"A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é: {distancia:.2f}")
