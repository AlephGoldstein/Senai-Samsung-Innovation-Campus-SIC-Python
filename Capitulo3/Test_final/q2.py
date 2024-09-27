def eh_palindromo(s):
    s = s.replace(" ", "").lower()
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return eh_palindromo(s[1:-1])
    else:
        return False

string = input("Digite uma string: ")
if eh_palindromo(string):  
    print(f"'{string}' é um palíndromo!")
else:
    print(f"'{string}' não é um palíndromo.")