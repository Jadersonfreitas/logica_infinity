palavra = str(input("Digite uma palavra: ")).strip()

invertida = palavra[::-1]

if palavra == invertida:
    print(f"{palavra} é um palindromo")
else:
    print(f"{palavra} não é um palindromo")