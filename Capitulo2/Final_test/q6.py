notas = (('Davi', 88, 95, 90), ('Felipe', 83, 98, 81), ('Luciano', 81, 97, 98), ('Rodrigo', 82, 89, 83))
notas_matematica = [nota[2] for nota in notas]
media_matematica = sum(notas_matematica) / len(notas_matematica)
print(f'A média das notas de matemática é: {media_matematica}')
