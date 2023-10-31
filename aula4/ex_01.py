
while True:
    nota = float(input("Avalie nosso aplicativo com uma nota de 0 a 10: "))

    if nota >= 0 and nota <= 10:
        print("Obrigado pela avaliaçao!")
        break
    else:
        print("Favor escolher entre 0 e 10.")
