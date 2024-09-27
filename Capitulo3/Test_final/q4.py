# Classe Vetor
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Método para multiplicação
    def __mul__(self, other):
        return Vetor(self.x * other.x, self.y * other.y)

    # Método para divisão
    def __truediv__(self, other):
        return Vetor(self.x / other.x, self.y / other.y)

    # Método para exibir o vetor como uma string
    def __repr__(self):
        return f"({self.x}, {self.y})"

# Inicializando os vetores
v1 = Vetor(30, 40)
v2 = Vetor(10, 20)

# Realizando a multiplicação e divisão
resultado_mul = v1 * v2
resultado_div = v1 / v2

# Exibindo os resultados
print(f"v1 * v2 = {resultado_mul}")
print(f"v1 / v2 = {resultado_div}")
