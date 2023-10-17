palavra = str(input("Digite uma palavra: ")).lower()

tem_a = False
quantidade = 0

for letra in palavra:
    if letra == "a":
        tem_a = True
        quantidade = quantidade + 1

if tem_a == True:
    print(f"Sua palavra possui {quantidade} letras A!")     
else:
    print("sua palavra nao tem uma letra A")   
           