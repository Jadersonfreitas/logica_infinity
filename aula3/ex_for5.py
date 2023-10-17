soma = 0
for i in range(1,10):
    numero = float(input(f"Digite o {i}º numero: "))
    soma = soma + numero
    media = soma/10

print(f"A media entre os numeros é {media}")