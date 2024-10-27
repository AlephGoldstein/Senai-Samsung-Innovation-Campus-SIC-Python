
maximum = int(input("Insira o valor máximo: "))
number = int(input("Insira o chute: "))
count = 0
low, high = 1, maximum
while low < high:
    mid = (low + high) // 2
    count += 1
    if mid == number:
        print(f"Seu número é {number}.")
        break
    elif mid > number:
        high = mid - 1
    else:
        low = mid + 1
print(f"Foram procuradas {count} vezes.!")